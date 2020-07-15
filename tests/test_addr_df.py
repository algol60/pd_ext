import pandas as pd
import numpy as np
import sys

from netaddr import IPAddress
from netaddr_ext import AddrArray

def test_dtype():
    df = pd.DataFrame({'ip':AddrArray(['1.1.1.1', '2.2.2.2'])})
    assert str(df.ip.dtype)=='ipaddress'

def test_loc_type():
    df = pd.DataFrame({'ip':AddrArray(['1.1.1.1', '2.2.2.2'])})
    item = df.loc[0, 'ip']
    assert type(item)==IPAddress

def test_loc_value():
    ip_str = '1.2.3.4'
    df = pd.DataFrame({'ip':AddrArray([ip_str])})
    item = df.loc[0, 'ip']
    assert item==IPAddress(ip_str)

def test_loc_slice_all():
    ip_strs = ['1.2.3.4', '5.6.7.8', '9.10.11.12', '13.14.15.16']
    df = pd.DataFrame({'ip':AddrArray(ip_strs)})
    item = df.loc[:, 'ip']
    assert (item==[IPAddress(ip) for ip in ip_strs]).all()

def test_loc_slice():
    ip_strs = ['1.2.3.4', '5.6.7.8', '9.10.11.12', '13.14.15.16']
    df = pd.DataFrame({'ip':AddrArray(ip_strs)})
    item = df.loc[1:2, 'ip']
    assert (item==[IPAddress(ip) for ip in ip_strs[1:3]]).all()

def test_loc_seq():
    ip_strs = ['1.2.3.4', '5.6.7.8', '9.10.11.12', '13.14.15.16']
    df = pd.DataFrame({'ip':AddrArray(ip_strs)})
    items = df.loc[[0,2], 'ip']
    assert (items==[IPAddress(ip) for ip in [ip_strs[0], ip_strs[2]]]).all()

def test_iloc_value():
    ip_str = '1.2.3.4'
    df = pd.DataFrame({'ip':AddrArray([ip_str, '2.2.2.2'])})
    item = df.iloc[0]['ip']
    assert item==IPAddress(ip_str)

def test_iloc_slice_all():
    ip_strs = ['1.2.3.4', '5.6.7.8', '9.10.11.12', '13.14.15.16']
    df = pd.DataFrame({'ip':AddrArray(ip_strs)})
    item = df.iloc[:]['ip']
    assert (item==[IPAddress(ip) for ip in ip_strs]).all()

def test_iloc_slice():
    ip_strs = ['1.2.3.4', '5.6.7.8', '9.10.11.12', '13.14.15.16']
    df = pd.DataFrame({'ip':AddrArray(ip_strs)})
    item = df.iloc[1:2]['ip']
    assert (item==[IPAddress(ip) for ip in ip_strs[1:2]]).all()
