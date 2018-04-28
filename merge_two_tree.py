# RSI

# 导入系统接口函数
from api.ApiTool import *
# 导入系统自带的量化分析函数
from api.QuantAPI import *

# 定义回测使用的全局变量，如果用户未定义，则使用系统默认参数
account = 100e6                   # 回测初始资金
benchmark = '000300.HSZS'       # 参考业绩基准
begin_date = '2017-01-01'       # 回测起始时间
stop_date = '2017-10-01'        # 回测结束时间
stock_pool = ['000001.HSGP','000068.HSGP']      # 回测使用的股票池，如果stock_pool 是列表，则使用用户指定的股票组合，如果stock_pool是字符串，则为指数成分股（包括综合指数和行业指数）
fields = ['close', 'chg']  # 策略中需要使用的股票因子字段
right_type = -1                   # 回测数据的复权方式，0：除权，-1：前复权，1：后复权

# 如果用户希望自定义印花税交易手续费等内容请定义，否则为系统默认值
order_cost = {'bid_tax': 0,                 # 买入时印花税
              'ask_tax': 0.001,             # 卖出时印花税
              'bid_commission': 0.0003,    # 买入佣金
              'ask_commission': 0.0003,    # 卖出佣金
              'min_commission': 5,         # 最低佣金，元
              'slippage': 0.001,            # 滑点
              'type': 'stock',              # 股票分类
              'bid_limit': 100              # 买入最小份额限制
              }

# 初始化函数，用户在执行回测之前进行初始化工作，比如自定义参数的初始化
def init(user_account):
    user_account.param.stocknum = 2
    user_account.param.RSI_Period = 14
    user_account.param.RSI_High = 70
    user_account.param.RSI_Low = 30
    pass

# 策略函数，用户在该函数中输入每日执行的操作，系统读取该函数进行回测
def handle_one_day(user_account):
    '''
    策略函数
    :param user_account: 用户账户，类型为系统定义的 UserAccount 类
    :return: 无
    '''
    stocknum = user_account.param.stocknum
    RSI_Period = user_account.param.RSI_Period
    RSI_High = user_account.param.RSI_High
    RSI_Low = user_account.param.RSI_Low
    eachdate = user_account.date
    print(eachdate)

    if not isTradeDate(eachdate):
        print ("%s is not trading date" % eachdate)
        return

    stock_selected = [['init'] for i in range(2)]
    stock_data = getMarketData(sec_code=stock_pool, fields=fields, begin_date='-' + str(RSI_Period)+'D', stop_date=eachdate, right_type=-1, key_type=0)
    for i in range(stocknum):
        code = stock_pool[i]
        stock_data_each = stock_data[code]
        RSI_UP = sum([tmp for tmp in stock_data_each['chg'] if tmp > 0])
        RSI_DOWN = -sum([tmp for tmp in stock_data_each['chg'] if tmp < 0])
        if RSI_UP == - RSI_DOWN:
            RSI = 0
        else:
            RSI = RSI_UP/(RSI_UP + RSI_DOWN)*100
        if RSI_UP != RSI_DOWN:
            RSI_UP = sum([tmp for tmp in stock_data_each['chg'] if tmp > 0])
            RSI_DOWN = -sum([tmp for tmp in stock_data_each['chg'] if tmp < 0])
            RSI = RSI_UP / (RSI_UP + RSI_DOWN) * 100

            # 计算买卖信号
            if RSI < RSI_Low:
                stock_selected[0].append(code)
            if RSI > RSI_High:
                stock_selected[1].append(code)

    hold_stocks = list(user_account.stocks_hold.index)
    stock_out = stock_selected[1][1:]
    stock_in = stock_selected[0][1:]
    stock_in = [item for item in stock_in if item not in hold_stocks]

    # 先以开盘价卖出命中信号股票
    if len(stock_out) > 0:
        for i in range(len(stock_out)):
            stock_hold = user_account.can_sell(sec_code=stock_out[i])
            user_account.order(sec_code=stock_out[i], count=-stock_hold, unit='share', price_type='open')

    # 再以收盘价买入非持仓且入选股票
    if len(stock_in) > 0:
        money_assign = user_account.cash * 0.99 / len(stock_in)
        for i in range(len(stock_in)):
            user_account.order(sec_code=stock_in[i], count=money_assign, unit='CNY', price_type='close')
    return