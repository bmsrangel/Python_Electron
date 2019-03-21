#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

import unittest
from colorize import colorize


class ColorTests(unittest.TestCase):
    def test_getNormal(self):
        expected = '\033[m'

        self.assertEquals(colorize.Color.NORMAL, expected)

    def test_getBlack(self):
        sut = colorize.Color(foreground='black')
        expected = '\033[0;30m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getWhite(self):
        sut = colorize.Color(foreground='white')
        expected = '\033[0;37m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getBoldWhite(self):
        sut = colorize.Color(bold=True, foreground='white')
        expected = '\033[1;37m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getBlue(self):
        sut = colorize.Color(foreground='blue')
        expected = '\033[0;34m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getGreen(self):
        sut = colorize.Color(foreground='green')
        expected = '\033[0;32m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getCyan(self):
        sut = colorize.Color(foreground='cyan')
        expected = '\033[0;36m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getRed(self):
        sut = colorize.Color(foreground='red')
        expected = '\033[0;31m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getMagenta(self):
        sut = colorize.Color(foreground='magenta')
        expected = '\033[0;35m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getBrown(self):
        sut = colorize.Color(foreground='brown')
        expected = '\033[0;33m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getBoldBlue(self):
        sut = colorize.Color(foreground='blue', bold=True)
        expected = '\033[1;34m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getBoldGreen(self):
        sut = colorize.Color(foreground='green', bold=True)
        expected = '\033[1;32m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getBoldCyan(self):
        sut = colorize.Color(foreground='cyan', bold=True)
        expected = '\033[1;36m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getBoldRed(self):
        sut = colorize.Color(foreground='red', bold=True)
        expected = '\033[1;31m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getBoldMagenta(self):
        sut = colorize.Color(foreground='magenta', bold=True)
        expected = '\033[1;35m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getBoldBrown(self):
        sut = colorize.Color(foreground='brown', bold=True)
        expected = '\033[1;33m'
        current = str(sut)

        self.assertEquals(current, expected)

    def test_getBrownBackground(self):
        sut = colorize.Color(background='brown')
        expected = '\033[0;43m'
        current = str(sut)

        self.assertEquals(current, expected)


if __name__ == '__main__':
    for x in ['black', 'red', 'green', 'brown',
              'blue', 'magenta', 'cyan', 'white']:
        color = colorize.Color(foreground=x)
        print(color, x, colorize.Color.NORMAL)

    print('--')
    for x in ['black', 'red', 'green', 'brown',
              'blue', 'magenta', 'cyan', 'white']:
        color = colorize.Color(bold=True, foreground=x)
        print(color, x, colorize.Color.NORMAL)

    print('--')
    for x in ['black', 'red', 'green', 'brown',
              'blue', 'magenta', 'cyan', 'white']:
        color = colorize.Color(background=x)
        print(color, x, colorize.Color.NORMAL)
