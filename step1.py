import pandas as pd

# مسیر فایل خود را وارد کنید
file_path = "kddcup.data.corrected"

# بارگذاری فایل با استفاده از pandas
data = pd.read_csv(file_path, header=None)

# نمایش نمونه‌ای از داده‌ها
print("نمونه‌ای از داده‌ها:")
print(data.head())

# نمایش اطلاعات اولیه
print("\nاطلاعات اولیه:")
print(data.info())

# بررسی تعداد رکوردها
print(f"\nتعداد کل رکوردها: {len(data)}")
