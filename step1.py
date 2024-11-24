import pandas as pd

file_path = "kddcup.data.corrected"

# بارگذاری فایل با استفاده از pandas
# Load the file using pandas
data = pd.read_csv(file_path, header=None)

# نمایش نمونه‌ای از داده‌ها
# Display a sample of the data
print("Sample of the data:")
print(data.head())

# نمایش اطلاعات اولیه
# Display basic information
print("\nBasic Information:")
print(data.info())

# بررسی تعداد رکوردها
# Check the number of records
print(f"\nTotal number of records: {len(data)}")
