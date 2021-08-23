# -*- coding: utf-8 -*-
import sys
import itertools
import os
from operator import itemgetter, attrgetter


class ListSand():
    # sort dic in list
    listBeforeSort = [{"name": "taro", "age": 10}, {"name": "hanako", "age": 7}]
    sortedList = sorted(listBeforeSort, key=itemgetter("dic_key_name"))

    # sort obj in list
    listBeforeSort = [("taro", "A", 10), ("hanako", "B", 7), ("jiro", "C", 3)]
    sortedList = sorted(listBeforeSort, key=attrgetter("obj_item_name"))


class ForSand():
    for i in range(3):  # 0 1 2
        print(i)

    for i in range(3, 5):  # 3 4
        print(i)

    # get index and value
    enumList = ['taro', 'hana']
    for index, name in enumerate(enumList, 1):  # start from index 1
        print(index, name)

    # get two array value
    iteList1 = [1, 2, 3]
    iteList2 = [10, 20, 30]
    for i, j in itertools.product(iteList1, iteList2):
        print(i, j)

    # get map key and value
    info = {"a": "answer", "b": "block"}
    for key in info:
        print(key)  # a b

    for val in info.values:
        print(val)  # answer block

    for key, val in info.items:
        print(key, val)  # a answer  b block

    # create value list
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

class SettingSand():
    # 環境変数取得
    print(os.environ.get('LANG')) # ja_JP.UTF-8
    print(os.environ.get('NEW_KEY')) # None
    print(os.environ.get('NEW_KEY', 'default')) # default

    # 設定(プログラム内で有効。実際のシステム環境変数は書き換わらない)
    os.environ['NEW_KEY'] = 'test'
    print(os.environ['NEW_KEY'])
    # test
