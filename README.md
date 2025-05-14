# Abu Dhabi Hotel Operations Dataset Analysis

## Overview
This documentation guides users through analyzing the Abu Dhabi Hotel Operations Dataset, which includes data on occupancy rates, revenue, and customer demographics from January 2019 to June 2024. The aim is to provide insights into the hospitality industry trends and support strategic decision-making.

### Prerequisites
- Python 3.x
- pandas library
- An Excel file of the dataset named `Abu_Dhabi_Hotel_Operations_Dataset.xlsx`

### Setup and Execution

1. **Environment Setup**
   - Ensure Python is installed on your system.
   - Install the pandas library using pip:
     sh
     pip install pandas
     

2. **Download the Dataset**
   - Place the `Abu_Dhabi_Hotel_Operations_Dataset.xlsx` file in your working directory.

3. **Run the Analysis Script**
   - Copy the provided sample code into a Python file, e.g., `analyze_hotel_data.py`.
   - Execute the script:
     sh
     python analyze_hotel_data.py
     
   - The script will print an overview of the dataset and the average occupancy rate per year.

### Understanding the Output
- **Dataset Overview**: You'll see the total number of records and columns in the dataset, along with the first five records.
- **Average Occupancy Rate Per Year**: This section provides insights into how the occupancy rate has changed annually, helping stakeholders understand trends over time.

### Extending the Analysis
- **Revenue Analysis**: Modify the script to include revenue trends by changing the groupby column and aggregation method.
- **Customer Demographics**: Add analysis on customer age groups or booking sources by including relevant columns.

### Support
For further assistance, consider checking community forums or reaching out to the project maintainers through the repository's issue tracker.
