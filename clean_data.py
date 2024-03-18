
def clean_data(data):
    """
    params:
    - data: the output from load_data()

    returns: cleaned data with rolling avg column 
    and removed years without enough data for rolling averge. 
    """
    
    data = data.reset_index()
    data['moving_avg'] = data['tavg'].rolling(12).mean().fillna(0)

    data =  data[data['time'] >= '2012-01-01']
    
    return data