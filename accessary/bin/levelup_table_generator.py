#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
虹アクセサリーのスキルレベル UP に必要なアクセサリーの数を出力します
"""
def print_rows():
    ts = 0
    tg = 0
    for i in range(1, 20):
        s = i * 2
        g = 0
        while s > 30:
            s -= 5
            g += 1
        ts += s
        tg += g
        print("| {0} -> {1} | {2} | {3} |".format(i, i + 1, s, g))
    print("| 合計 | {0} | {1} |".format(ts, tg))


def main():
    print_rows()


if __name__ == '__main__':
    main()
