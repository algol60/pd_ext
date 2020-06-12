# Test the geo array.
#

import pandas as pd
import numpy as np

from aa_geo import GeoArray, GeoType, LonLat

from nose.tools import raises

def test_array():
    arr = GeoArray([(1,2), (3,4), (5,6)])
    assert (arr.data['lon'] == [1, 3, 5]).all()
    assert (arr.data['lat'] == [2, 4, 6]).all()

def test_item():
    arr = GeoArray([(1,2), (3,4), (5,6), (7,8)])
    assert arr[1]==LonLat(3,4)

@raises(ValueError)
def test_item_bad():
    _ = GeoArray([(1,2, 3), (4, 5, 6)])

def test_len():
    arr = GeoArray([(1,2), (3,4), (5,6)])
    assert len(arr)==3

def test_str_repr():
    arr = GeoArray([(1,2), (3,4), (5,6)])
    assert str(arr.dtype)=='lonlat'
    assert repr(arr.dtype)=="dtype('lonlat')"

def test_nbytes():
    points = [(1,2), (3,4), (5,6)]
    arr = GeoArray(points)

    # The dat ais stored as a numpy structured array,
    # so it should be the same size as the equivalent numpy array.
    # This is testing that GeoArray.nbytes returns the right number,
    # rather than the actual number.
    #
    assert arr.nbytes==np.array(points).nbytes
