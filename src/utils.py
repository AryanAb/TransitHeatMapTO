from coordinates import coast


def is_point_below_coast(lat, lon):
    """Returns true if the point `(lat, lon)` is below the coastline defined by the list of points `coast`."""
    for i in range(len(coast) - 1):
        y0, x0 = coast[i]
        y1, x1 = coast[i + 1]
        if (x0 <= lon <= x1) or (x1 <= lon <= x0):
            # Linear interpolation
            if x1 == x0:
                return lat < min(y0, y1)
            slope = (y1 - y0) / (x1 - x0)
            y_curve = y0 + slope * (lon - x0)
            return lat < y_curve
    return False
