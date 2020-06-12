

class LonLat:
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

    def __eq__(self, other):
        return isinstance(other, LonLat) and self.lon==other.lon and self.lat==other.lat

    def __hash__(self):
        return hash(self.lon) * 17 + hash(self.lat)

    def __repr__(self):
        return f'LonLat({self.lon},{self.lat})'
