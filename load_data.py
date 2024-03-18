import matplotlib.pyplot as plt

def load_data(lat, long, alt, city_name):

    import pandas as pd
    from datetime import datetime
    from meteostat import Monthly, Point

    """
    params -
    long: Longitudinal coordinate of your city of interest (if West, convert to negative value)
    lat: latitude coordinate of your city (if South, convert to negative value)
    altitude: altiude of city
    city_name: name of the city

    returns: daily weather data for the city from 2010 - 2024
    """

    start = datetime(2010, 1, 1)
    end = datetime(2024, 1, 1)

    # Do this so that user can input any data type for coordinates
    coords = [lat, long, alt]
    coords_2 = []
    for i in coords:
        coords_2.append(float(i))

    city = Point(*coords_2)
    city_data = Monthly(city, start, end)
    df = city_data.fetch()
    df['City'] = city_name
    df = df.reset_index()

    # Select only a few of the columns
    df = df[['time','tavg', 'tmin', 'tmax', 'prcp', 'wspd', 'pres', 'City']]

    return df