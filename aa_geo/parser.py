from pandas.api.types import is_list_like

def to_geo(*, lon, lat):
    if not is_list_like(lon):
        lon = [lon]
    if not is_list_like(lat):
        lat = [lat]

    if len(lon)!=len(lat):
        raise AttributeError('Longitude and latitude lengths must be equal')
