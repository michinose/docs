#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
虹アクセサリーのスキルレベルごとの効果量を出力します
"""
def print_each_int_row(init, end):
    diff = end - init
    for i in range(0, 20):
        e = int(init + i * diff / 19)
        print("| {0} | {1} ({2}) |".format(i + 1, e, e))


def print_each_float_row(init, end):
    diff = end - init
    for i in range(0, 20):
        e = str(init + i * diff / 19)[:4]
        print("| {0} | {1} ({2}) |".format(i + 1, e, e[:3]))


def print_earring():
    print("earring")
    print_each_float_row(1.0, 2.0)
    print()


def print_necklace():
    print("Necklace")
    print_each_float_row(1.0, 2.0)
    print()


def print_broach():
    print("Broach")
    print_each_float_row(2.5, 5.0)
    print()


def print_keychain():
    print("Keychain")
    print_each_float_row(2.5, 5.0)
    print()


def print_bracelet():
    print("Bracelet")
    print_each_float_row(2.5, 5.0)
    print()


def print_hairpin():
    print("Hairpin")
    print_each_float_row(2.5, 5.0)
    print()


def print_ribbon():
    print("Ribbon")
    print_each_int_row(250, 500)
    print()


def print_pouch():
    print("Pouch")
    print_each_int_row(250, 500)
    print()


def print_wristband():
    print("Wristband")
    print_each_float_row(2.5, 5.0)
    print()


def print_towel():
    print("Towel")
    print_each_float_row(2.5, 5.0)
    print()


def print_all():
    print_earring()
    print_necklace()
    print_broach()
    print_keychain()
    print_bracelet()
    print_hairpin()
    print_ribbon()
    print_pouch()
    print_wristband()
    print_towel()


def main():
    print_all()


if __name__ == '__main__':
    main()
