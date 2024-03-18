
# from load_data import load_data
# from clean_data import clean_data
# from visualize_data import plot_data


if __name__ == '__main__':
    
    from load_data import load_data
    from clean_data import clean_data
    from visualize_data import plot_data
    
    import argparse

    parser = argparse.ArgumentParser()

    # inputs: Coordinates and city name
    parser.add_argument('longitude', help = '(float) Longitude of city. If South, make negative')
    parser.add_argument('latitude', help = '(float) Latitude of city. If West, make negative')
    parser.add_argument('altitude', help = '(float) Altitude of city.')
    parser.add_argument('city', help = 'Name of the city (stripng)')
    
    # Output: path of image / chart as .png
    parser.add_argument('output_path', help = "file path of resulting image. Ex) 'out.png'")

    args = parser.parse_args()

    # Load data from meteostat API
    data = load_data(args.longitude, args.latitude, args.altitude, args.city)

    # Clean data - add rolling average
    cleaned_data = clean_data(data)

    # Plot data and output to .png
    plot_data(cleaned_data, args.output_path)