import pandas as pd
from pandas.api.extensions import ExtensionDtype
import numpy as np

from .lonlat import LonLat

@pd.api.extensions.register_extension_dtype
class GeoType(ExtensionDtype):
    kind = 'O'
    na_value = None
    name = 'lonlat'
    # names = ['longitude', 'latitude']
    type = LonLat

    _record_type = np.dtype([('lon', 'f'), ('lat', 'f')])

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
        print(f'@@ construct_from_string {cls}')
        comma = string.find(',')
        if comma==-1:
            return None

        lonlat = string.split(',')
        if len(lonlat)!=2:
            return None

        return cls(float(lonlat[0]), float(lonlat[1]))

    #
    # End: must implement.

    # def construct_array_type(self):
    #     pass

    # def is_dtype(self, dtype):
    #     print(f'@is_dtype {dtype}')
    #     return False

    def __repr__(self):
        return f"dtype('{GeoType.name}')"
