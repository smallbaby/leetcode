# -*- coding: utf-8 -*-

'''

要求：给一个有N个元素的字典，按照Value排序，输出对应的Key，相同的Value任意输出对应的Key
输入： {'a':1,'b':3, 'c':2}
输出：['b','c','a']
'''

def solution(di):
    re_di = dict([(v,k) for k,v in di.iteritems()])
    arr = []
    for x in sorted(re_di.keys(), reverse=True):
        arr.append(re_di[x])
    return arr

# 思路1：先反序，然后输出Value对应的key
d = {'a':5,'b':'10', 'c':4, 'd': 8, 'e' : 5}
print solution(d)

# 思路2：用API直接实现  倒序
# 2.1
print [x[0] for x in sorted(d.items(), lambda x,y : cmp(x[1], y[1]), reverse=True)]
# 2.2
print sorted(d.items(), key = lambda x:x[1], reverse=True)

'''
合并俩字典
相同的key，合并成list作为value
输入：d1 = {'a':1,'b':2} d2 = {'e':2, 'b':5}
d1 + d2
输出 {'a':1, 'b':[2,5], 'e': 2}
'''
d1 = {'a':1,'b':2}
d2 = {'e':2, 'b':5}

for k, v in d1.items():
    if k not in d2:
        d2[k] = v
    else:
        temp = d2[k]
        if isinstance(temp, list):
            temp.append(v)
            d2[k] = temp
        else:
            d2[k] = [temp,v]
    print d2




