# -*- coding: utf-8 -*-
import sys
import itertools


class ForSand():
    for i in range(3):  # 0 1 2
        print(i)

    for i in range(3, 5):  # 3 4
        print(i)

    enumList = ['taro', 'hana']
    for i, name in enumerate(enumList, 1):
        print(i, name)

    iteList1 = [1, 2, 3]
    iteList2 = [10, 20, 30]
    for i, j in itertools.product(iteList1, iteList2):
        print(i, j)

    info = {"a": "answer", "b": "block"}
    for key in info:
        print(key)  # a b

    for val in info.values:
        print(val)  # answer block

    for key, val in info.items:
        print(key, val)  # a answer  b block

    values = [val for val in info.values()]


class ExceptionSand():

    def hoge():
        print("hoge")

    try:
        hoge()
    except Exception:
        print(sys.exe_info())

    try:
        hoge()
    except Exception:
        import traceback
        traceback.print_exc()

    try:
        hoge()
    except ZeroDivisionError as e:
        print("except args:", e.args)
