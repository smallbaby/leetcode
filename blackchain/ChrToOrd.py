

sex_d = {10:'A', 11:'B', 12:'C',13:'D',14:'E',15:'F'}
sex_s = {'0':0, '1':1, '2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A': 10, 'B':11,'C':12,'D':13,'E':14,'F':15}


def tr_16_to_10(code):
    res = 0
    code = code[::-1]
    for i,v in enumerate(code):
        l = sex_s.get(v.upper())
        res = res + l * pow(16,i)
    return res


def tr_10_16(code, is_comp = False):
    if isinstance(code, int):
        mid = code
        res = []
        while mid >= 1:
            remainder = mid % 16
            if remainder > 9:
                remainder = sex_d[remainder]
            res.insert(0, remainder)
            mid = mid / 16
        r = ''
        if not is_comp:
            r = '0' * (4 - len(res))
        for c in res:
            r += str(c)
        return r


def binary(code):
    if isinstance(code, basestring):
        mid = ord(code)
        res = []
        while mid >= 1:
            remainder = mid % 2
            res.insert(0, remainder)
            mid = mid / 2
        r = '0' * (8-len(res))
        for c in res:
            r += str(c)
        return r

def tr_10_to_2(code):
    mid = int(code)
    res = []
    while mid >= 1:
        remainder = mid % 2
        res.insert(0, remainder)
        mid = mid / 2
    r = '0' * (8 - len(res))
    for c in res:
        r += str(c)
    return r


def transform(code):
    res = []
    for c in code:
        res.append(binary(c))
    return res
print tr_10_to_2(115792089237316195423570985008687907853269984665640564039457584007913129639936)
print tr_10_to_2(110427941548649020598956093796432407239217743554726184882600387580788736)
# res = transform('abc')
# print ''.join(res)
#res = tr_10_16(23785)
# print tr_16_to_10(res)
# print tr_16_to_10('2AF5')
# print tr_16_to_10('ca07ca')
# print tr_10_16(13240266)
# import hashlib
# t = 'I like donuts'
# i = 0
# while True:
#     i = i + 1
#     o = tr_10_16(i, True)
#     oh = hashlib.sha256(t + o.lower()).hexdigest()
#     if oh[0:6] == '000000' or i % 1000000 == 0:
#         print i,o,oh,t+o.lower()
