import pandas as pd
from pandas.core.dtypes.common import is_dtype_equal
from . import AddrType

import netaddr

_ACCESSOR = 'ipaddr'

@pd.api.extensions.register_series_accessor(_ACCESSOR)
class NetaddrIPAccessor:
    def __init__(self, pd_obj):
        self._obj = pd_obj
        if str(pd_obj.dtype)!=AddrType.name:
            raise AttributeError(f'Can only use .{_ACCESSOR} accessor with ipnetwork values')

    def bin(self):
        return pd.Series([ip.bin for ip in self._obj])

    def bits(self):
        return pd.Series([ip.bits() for ip in self._obj])

    # @property
    def hex(self):
        return pd.Series([hex(ip) for ip in self._obj])

    def packed(self):
        return pd.Series([ip.packed for ip in self._obj])

    # def valid_ipv4(self):
    #     return [netaddr.valid_ip4(ip) for ip in self._obj]

    def words(self):
        return pd.Series([ip.words for ip in self._obj])
