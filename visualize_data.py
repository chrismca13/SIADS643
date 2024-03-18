import matplotlib.pyplot as plt

def plot_data(cleaned_data, image_path):
    
    # matplotlib dual axis of actuals (tavg) and moving averages
    plt.plot(cleaned_data['time'].values, cleaned_data['tavg'].values, color = 'b');
    plt.plot(cleaned_data['time'].values, cleaned_data['moving_avg'].values, color = 'r'); 
    
    # Label axis and chart
    plt.xlabel('Year');
    plt.ylabel('Monthly Weather (C)');
    plt.title('Monthly Weather in ' + cleaned_data['City'].iloc[0]);
    
    # Format to reasonable size
    fig = plt.gcf();
    fig.set_size_inches(10, 6);
    
    # Save to specified path
    fig = plt.gcf();
    fig.savefig(image_path, dpi=100);
    plt.close();