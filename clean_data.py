
def clean_data(data):
    """
    params:
    - data: the output from load_data()

    returns: cleaned data with rolling avg column 
    and removed years without enough data for rolling averge. 
    """

    # Create a moving average column so we can plot
    # alongside the actual values
    data = data.reset_index()
    data['moving_avg'] = data['tavg'].rolling(12).mean().fillna(0)

    # Excluded records pre-2012 to remove weirdness with rolling avg.
    data =  data[data['time'] >= '2012-01-01']
    
    return data