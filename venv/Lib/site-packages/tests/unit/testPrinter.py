import unittest
import doublex
from colorize import colorize
from tests.utils import FakeIO


class PrinterTests(unittest.TestCase):
    def test_reads_a_line_and_prints_it(self):
        line = 'foo'
        stdin = FakeIO(line)
        with doublex.Mock() as log:
            log.log(line)

        sut = colorize.Printer(stdin, {}, log.log)

        sut.process()

        doublex.assert_that(log, doublex.verify())

    def test_reads_two_lines_and_prints_them(self):
        line = '1\n2'
        stdin = FakeIO(line)
        with doublex.Mock() as log:
            log.log('1')
            log.log('2')

        sut = colorize.Printer(stdin, {}, log.log)

        sut.process()

        doublex.assert_that(log, doublex.verify())

    def test_replacement(self):
        line = 'foo'
        stdin = FakeIO(line)
        expected = 'ok'
        with doublex.Mock() as log:
            log.log(expected)
        regexps = {'foo': expected}

        sut = colorize.Printer(stdin, regexps, log.log)

        sut.process()

        doublex.assert_that(log, doublex.verify())
