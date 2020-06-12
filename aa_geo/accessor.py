import pandas as pd
import numpy as np

LON = 'longitude'
LAT = 'latitude'

@pd.api.extensions.register_dataframe_accessor('geo')
class GeoAccessor:
    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj

    @staticmethod
    def _validate(obj):
        # Verify that the LON and LAT columns exist.
        #
        if LON not in obj.columns or LAT not in obj.columns:
            raise AttributeError(f"Must have '{LON}' and '{LAT} columns.")

        for col in [LON, LAT]:
            d = obj[col].dtype
            if d.type not in [np.float, np.int64]:
                raise AttributeError(f"The {col} column must be float or int64, not {d.type}.")
            # print(f'@@ {dir(d)} {d.type} {d}')

    @property
    def mean(self):
        """Return the specified subnet of each value."""
        lon = self._obj[LON]
        lat = self._obj[LAT]

        mean_lon = lon.mean()
        mean_lat = lat.mean()

        return mean_lon, mean_lat
