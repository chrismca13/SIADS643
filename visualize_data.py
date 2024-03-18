import matplotlib.pyplot as plt

def plot_data(cleaned_data, image_path):
    
    plt.plot(cleaned_data['time'].values, cleaned_data['tavg'].values, color = 'b');
    plt.plot(cleaned_data['time'].values, cleaned_data['moving_avg'].values, color = 'r'); 
    
    plt.xlabel('Year');
    plt.ylabel('Monthly Weather (C)');
    plt.title('Monthly Weather in ' + cleaned_data['City'].iloc[0]);
    
    fig = plt.gcf();
    fig.set_size_inches(10, 6);
    
    fig = plt.gcf();
    fig.savefig(image_path, dpi=100);
    plt.close();