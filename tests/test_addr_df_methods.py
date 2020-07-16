import pandas as pd
import numpy as np
import sys

from netaddr import IPAddress
from netaddr_ext import AddrArray

from nose.tools import raises

def test_bin():
    df = pd.DataFrame({'ip':AddrArray(['1.1.1.1', '2.2.2.2'])})
    s = df['ip'].ipaddr.bin()
    actual = ['0b1000000010000000100000001', '0b10000000100000001000000010']
    assert (s==actual).all()

def test_bits():
    df = pd.DataFrame({'ip':AddrArray(['1.1.1.1', '2.2.2.2'])})
    s = df['ip'].ipaddr.bits()
    actual = ['00000001.00000001.00000001.00000001', '00000010.00000010.00000010.00000010']
    assert (s==actual).all()

def test_hex():
    df = pd.DataFrame({'ip':AddrArray(['1.1.1.1', '2.2.2.2'])})
    s = df['ip'].ipaddr.hex()
    actual = ['0x1010101', '0x2020202']
    assert (s==actual).all()

def test_words():
    df = pd.DataFrame({'ip':AddrArray(['1.1.1.1', '2.2.2.2'])})
    s = df['ip'].ipaddr.words()
    actual = pd.Series([(1, 1, 1, 1), (2, 2, 2, 2)])
    assert (s==actual).all()

def test_words_6():
    df = pd.DataFrame({'ip':AddrArray(['::1', '::2'])})
    s = df['ip'].ipaddr.words()
    actual = pd.Series([(0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 0, 0, 2)])
    assert (s==actual).all()

@raises(AttributeError)
def test_wrong_type():
    df = pd.DataFrame({'ip':['1.1.1.1', '2.2.2.2']})
    df['ip'].ipaddr.hex()
