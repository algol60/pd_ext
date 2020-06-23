import pandas as pd
from pandas.api.extensions import ExtensionDtype
import numpy as np

import netaddr

@pd.api.extensions.register_extension_dtype
class AddrType(ExtensionDtype):
    kind = 'O'
    na_value = None
    name = 'ipaddress'
    names = None
    type = netaddr.IPAddress

    # _record_type = np.dtype([('lon', 'f'), ('lat', 'f')])
    _record_type = np.dtype([('ipaddress', 'O')])

    # def __init__(self, lonlat):
    #     self.data = LonLat(lon=lonlat[0], lat=lonlat[1])

    # Begin: must implement.
    #

    # @property
    # def type(self):
    #     return Interval

    # @property
    # def name(self) -> str:
    #     """A string representation of the dtype."""
    #     return 'lonlat'

    @classmethod
    def construct_from_string(cls, string):
        print(f'@@ addr construct_from_string {cls} "{string}"')

        # return cls(float(lonlat[0]), float(lonlat[1]))
        return netaddr.IPAddress(string)

    #
    # End: must implement.

    # def construct_array_type(self):
    #     pass

    # def is_dtype(self, dtype):
    #     print(f'@is_dtype {dtype}')
    #     return False

    def __repr__(self):
        return f"dtype('{AddrType.name}')"
