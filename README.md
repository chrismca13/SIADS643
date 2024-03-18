**Introduction:**

The goal of this script is to return a chart of monthly temperatures given the coordinates of a city, the name of the city, and the file path the user wants their chart to be saved.

**Required Libraries:** 

A complete list of requirments is available in the requirments.txt file, but the following are absolutely essential:

* meteostat==1.6.5
* matplotlib==3.7.5
* pandas==2.0.3
* numpy==1.24.3

**Required Files:**

* clean_data.py
* load_data.py
* visualize_data.py
* main.py


**Example:**


Once you have those files saved in the same directory, you can run the following code to create a plot showing the monthly weather in San Francisco:

terminal\SIADS643:-$ python main.py 37.8 -122.4 50 "San Francisco" "out.png"

That line above is made up of 5 inputs:

* longitude: (float) Longitude of city of interest. If South, make negative. Round to the nearest 10th.
* latitude: (float) Latitude of city of interest. If West, make negative. Round to the nearest 10th.
* altitude: (int) Altitude of city of interest. Round to the nearest 10th.
* city: (string) Name of the city.
* output_path: (string) file path of resulting image. Example: "out.png"


