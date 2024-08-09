import pandas as pd

# Step 1: Load the dataset
file_path = 'example_dataset.csv'
df = pd.read_csv(file_path)

# Step 2: Perform basic data cleaning
# Handling missing values
df.ffill(inplace=True)

# Removing duplicates
df.drop_duplicates(inplace=True)

# Step 3: Engineer new features
# Print column names to verify
print(df.columns)

# Example: Creating a new feature by combining existing features
# Update 'feature_1' and 'feature_2' with actual column names from your dataset
df['new_feature'] = df['feature_1'] + df['feature_2']

# Step 4: Save the preprocessed dataset
preprocessed_file_path = 'preprocessed_example_dataset.csv'
df.to_csv(preprocessed_file_path, index=False)

print("Data preprocessing complete. Preprocessed dataset saved as 'preprocessed_example_dataset.csv'.")


