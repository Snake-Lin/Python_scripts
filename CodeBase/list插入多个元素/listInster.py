# -*- coding:utf-8 -*-
"""
@author: lin
@file: listInster.py
@software: PyCharm
@project: CodeBase
@time: 18-3-29 下午6:00
@desc: 在列表特定位置插入特定的数据
"""
lis_A = ['A', 'B2', 'C', 'D', 'E']

col = dict(A=['a1', 'a2', 'a3'],
           B=['b1', 'b2','b3'],
           C=['c1', 'c2'])

import copy


def func01(fields):
    lis_M = copy.copy(fields)
    for i in fields:
        if i in col.keys():

            index = lis_M.index(i)
            [lis_M.insert(index, d) for d in col[i]]
            lis_M.remove(i)

    return lis_M


def func02(fields):
    lis_M = copy.copy(fields)
    for i in fields:
        if i in col.keys():
            index = lis_M.index(i)
            lis_M = lis_M[:index] + col[i] + lis_M[index:]

            lis_M.remove(i)

    return lis_M


def func03(fields):
    lis_M = copy.copy(fields)
    for i in fields:
        if i in col.keys():
            index = lis_M.index(i)
            for j in col[i]:
                lis_M.insert(index, j)
                index += 1
            lis_M.remove(i)

    return lis_M

returns = func01(lis_A)
print(returns)

returns = func02(lis_A)
print(returns)

returns = func03(lis_A)
print(returns)


