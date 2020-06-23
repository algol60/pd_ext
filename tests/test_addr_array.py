# Test the IPAddress array.
#

import pandas as pd
import numpy as np
import sys

from netaddr import IPAddress
from netaddr_ext import AddrArray
from netaddr_ext import to_ipaddress

from nose.tools import raises

def test_array():
    arr = AddrArray([IPAddress('1.1.1.1'), IPAddress('2.2.2.2')])
    assert arr.data[0] == IPAddress('1.1.1.1')
    assert arr.data[1] == IPAddress('2.2.2.2')

def test_item():
    arr = AddrArray([IPAddress('1.1.1.1'), IPAddress('2.2.2.2')])
    assert arr.data[1] == IPAddress('2.2.2.2')

# @raises(ValueError)
# def test_item_bad():
#     _ = AddrArray([(1,2, 3), (4, 5, 6)])

def test_len():
    arr = AddrArray([IPAddress('1.1.1.1'), IPAddress('2.2.2.2'), IPAddress('3.3.3.3')])
    assert len(arr)==3

def test_str_repr():
    arr = AddrArray([IPAddress('1.1.1.1'), IPAddress('2.2.2.2')])
    assert str(arr.dtype)=='ipaddress'
    assert repr(arr.dtype)=="dtype('ipaddress')"

def test_nbytes():
    arr = AddrArray([IPAddress('1.1.1.1'), IPAddress('2.2.2.2'), IPAddress('3.3.3.3')])

    assert arr.nbytes==sum(sys.getsizeof(i) for i in arr)

def test_isna2():
    arr = AddrArray([None, IPAddress('1.1.1.1')])
    assert (arr.isna()==np.array([True, False])).all()

def test_isna3():
    arr = AddrArray([IPAddress('1.1.1.1'), IPAddress('2.2.2.2'), None])
    assert (arr.isna()==np.array([False, False, True])).all()

def test_eq():
    ip1 = to_ipaddress(['1.1.1.1', '2.2.2.2'])
    ip2 = AddrArray([IPAddress('1.1.1.1'), IPAddress('2.2.2.2')])
    assert (ip1==ip2).all()

def test_nan():
    ip1 = to_ipaddress(['1.1.1.1', '2.2.2.2', None])
