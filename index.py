# Sample Python Code to Analyze Abu Dhabi Hotel Operations Dataset
import pandas as pd

# Load the dataset
file_path = 'Abu_Dhabi_Hotel_Operations_Dataset.xlsx'
dataset = pd.read_excel(file_path)

# Display basic information about the dataset
def explore_data(data):
    print('--- Dataset Overview ---')
    print(f'Total Records: {len(data)}')
    print(f'Columns: {list(data.columns)}')
    print('\n--- First 5 Records ---')
    print(data.head())

# Analyze occupancy rates
# Function to calculate average occupancy rate per year
def analyze_occupancy(data):
    data['Year'] = pd.DatetimeIndex(data['Date']).year
    occupancy_by_year = data.groupby('Year')['Occupancy Rate'].mean()
    print('\n--- Average Occupancy Rate Per Year ---')
    print(occupancy_by_year)

# Run the functions
explore_data(dataset)
analyze_occupancy(dataset)
