import pandas as pd

# 1. Read Excel File
excel_file_path = 'C:\\Users\\starb\\PycharmProjects\\pythonProject\\diabetes (3).xlsx'
data = pd.read_excel(excel_file_path)

# 2. Calculate Percentage of Missing Data
missing_data_percentage = (data.isnull().sum() / len(data)) * 100

# 3. Convert Categorical Data to Numerical (One-Hot Encoding)
'''data = pd.get_dummies(data, columns=['id', 'chol', 'stab.glu', 'hdl', 'ratio', 'glyhb', 'location', 'age', 'gender',
                                     'height', 'weight', 'frame', 'bp.1s', 'bp.1d', 'bp.2s', 'bp.2d', 'waist', 'hip',
                                     'time.ppn'
 
print(                                    ])'''
data = pd.get_dummies(data)
data.head(5)
exit(0)
# 4. Split the Data into Training and Testing Sets (60-40 and 70-30)
from sklearn.model_selection import train_test_split

# 60-40 Split
train_data_60, test_data_40 = train_test_split(data, test_size=0.4, random_state=42)

# 70-30 Split
train_data_70, test_data_30 = train_test_split(data, test_size=0.3, random_state=42)

# Print the results
print("Percentage of Missing Data:")
print(missing_data_percentage)
print("\nSample Training and Testing Data Shapes (60-40 Split):")
print("Training Data (60%):", train_data_60.shape)
print("Testing Data (40%):", test_data_40.shape)
print("\nSample Training and Testing Data Shapes (70-30 Split):")
print("Training Data (70%):", train_data_70.shape)
print("Testing Data (30%):", test_data_30.shape)
