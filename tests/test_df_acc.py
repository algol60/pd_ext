# Test the dataframe accessor.
#

import pandas as pd
import numpy as np
import aa_geo

def test_mean():
    df = pd.DataFrame({
        'longitude': list(range(10)),
        'latitude': list(range(10))
    })

    mean = df.geo.mean
    assert mean==(4.5, 4.5)
