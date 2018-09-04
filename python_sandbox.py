# -*- coding: utf-8 -*-
import sys


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
