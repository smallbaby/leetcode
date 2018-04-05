# -*- coding: utf-8 -*-
# __author__ = 'kai.zhang01'
# create date = 2018/04/02


def quick_sort(lists,left,right):
    if left > right:
        return lists
    low,high = left,right
    key = lists[left] #key即是标准数
    while left < right:
        while left < right and lists[right] >= key:
            right-=1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left+=1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists,low,left-1)
    quick_sort(lists,right+1,high)
    return lists


def qs(li, l, r):
    if l > r:
        return li
    low, high = l, r
    key = li[l]
    while l < r:
        while l < r and li[r] >= key:
           r = r - 1
        li[l] = li[r]
        while l < r and li[l] <= key:
            l = l + 1
        li[r] = li[l]
    li[r] = key
    qs(li, low, l - 1)
    qs(li, r + 1, high)
    return li



def q_s(li, l, r):
    if l > r:
        return li
    key = li[l]
    low, high = l, r
    while l < r:
        while l < r and li[r] >= key:
            r = r - 1
        li[l] = li[r]
        while l < r and li[l] <= key:
            l = l + 1
        li[r] = li[l]
    li[l] = key
    q_s(li, low, l -1)
    q_s(li, r + 1, high)
    return li

a=[5,7,4,1,8,2,4,3,20]


# f = lambda x:x+3
# print f(3)
#
# f= lambda x,y:x+y
# print f(1,2)

key = 3
small = [x for x in a if x < key]
big = [x for x in a if x > key]

qs = lambda X: [] if len(X) == 0 else qs([i for i in X if i < X[0]]) + [X[0]] + qs([i for i in X if i > X[0]])
qs = lambda x:[]  if len(x) == 0 else qs([i for i in x if i < x[0]]) + [x[0]] + qs([i for i in x if i > x[0]])





def q_s(li, l, r):
    if l > r:
        return li
    key = li[l]
    low,high = l, r
    while l < r:
        while l < r and li[r] >= key:
            r = r - 1
        li[l] = li[r]
        while l < r and li[l] <= key:
            l = l + 1
        li[r] = li[l]
    li[l] = key
    q_s(li, low, l -1)
    q_s(li, r + 1, high)
    return li








#
# print q_s(a, 0, len(a)-1)








f = lambda x: [] if len(x) == 0 else f([i for i in x if i < x[0]]) + [x[0]] + f([i for i in x if i > x[0]])










f = lambda x: [] if len(x) == 0 else f([i for i in x if i < x[0]]) + [x[0]] + f([i for i in x if i >x[0]])
















f = lambda x: [] if len(x) == 0 else f([i for i in x if i < x[0]]) + [x[0]] + f([i for i in x if i > x[0]])



def s_q(li, l, r):
    if l > r:
        return li
    key = li[l]
    low, high = l, r
    while l < r:
        while l < r and li[r] >= key:
            r = r - 1
        li[l] = li[r]
        while l < r and li[l] < key:
            l = l + 1
        li[r] = li[l]
    li[l] = key
    s_q(li, low, l - 1)
    s_q(li, r + 1, high)
    return li
print s_q(a, 0, len(a)-1)






