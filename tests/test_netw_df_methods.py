import pandas as pd
import numpy as np
import sys

from netaddr import IPAddress, IPNetwork
from netaddr_ext import NetwArray

from nose.tools import raises

def test_broadcast():
    # df = pd.DataFrame({'net':NetwArray(['16.0.0.0/8', '192.168.0.0/24'])})
    df = pd.DataFrame({'net':NetwArray(['192.168.11.0/24', '192.168.0.0/24'])})
    print(df)
    s = df['net'].ipnet.broadcast()
    actual = [IPAddress('16.255.255.255'), IPAddress('192.168.0.255')]
    assert (s==actual).all()