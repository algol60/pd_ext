import pandas as pd
from pandas.core.dtypes.common import is_dtype_equal
from . import AddrType, NetwType

import netaddr

_ACCESSOR = 'ipnet'

@pd.api.extensions.register_series_accessor(_ACCESSOR)
class NetaddrNetAccessor:
    def __init__(self, pd_obj):
        self._obj = pd_obj
        if str(pd_obj.dtype)!=NetwType.name:
            raise AttributeError(f'Can only use .{_ACCESSOR} accessor with ipnetwork values')

    def cidr(self):
        return pd.Series([ip.cidr for ip in self._obj])

    def broadcast(self):
        # print('@@', self._obj)
        return pd.Series([ip.broadcast for ip in self._obj])

    def hostmask(self):
        return pd.Series([ip.hostmask for ip in self._obj])

    def netmask(self):
        return pd.Series([ip.netmask for ip in self._obj])

    # @property
    def network(self):
        return pd.Series([ip.network for ip in self._obj])

    # def valid_ipv4(self):
    #     return [netaddr.valid_ip4(ip) for ip in self._obj]

    def words(self):
        return pd.Series([ip.words for ip in self._obj])
