
import numpy as np
from pandas.api.types import is_list_like

import ipaddress
from . import AddrArray


def to_ipaddress(values):
    """Convert values to AddrArray

    Parameters
    ----------
    values : int, str, bytes, or sequence of those

    Returns
    -------
    addresses : IPArray

    Examples
    --------
    Parse strings
    >>> to_ipaddress(['192.168.1.1',
    ...               '2001:0db8:85a3:0000:0000:8a2e:0370:7334'])
    <IPArray(['192.168.1.1', '0:8a2e:370:7334:2001:db8:85a3:0'])>

    Or integers
    >>> to_ipaddress([3232235777,
                      42540766452641154071740215577757643572])
    <IPArray(['192.168.1.1', '0:8a2e:370:7334:2001:db8:85a3:0'])>

    Or packed binary representations
    >>> to_ipaddress([b'\xc0\xa8\x01\x01',
                      b' \x01\r\xb8\x85\xa3\x00\x00\x00\x00\x8a.\x03ps4'])
    <IPArray(['192.168.1.1', '0:8a2e:370:7334:2001:db8:85a3:0'])>
    """

    if not is_list_like(values):
        values = [values]

    return AddrArray(values)
