from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np
import pandas as pd

file_path = "kddcup.datacopy.corrected"

# تعریف ستون‌های ضروری
# Define necessary columns
selected_columns = [
    "duration",
    "protocol_type",
    "service",
    "flag",
    "src_bytes",
    "dst_bytes",
    "same_srv_rate",
    "diff_srv_rate",
    "serror_rate",
    "srv_serror_rate",
    "dst_host_count",
    "dst_host_srv_count",
    "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate",
    "dst_host_serror_rate",
    "dst_host_srv_serror_rate",
    "label",
]

# بارگذاری و فیلتر کردن ستون‌ها
# Load and filter the selected columns
data = pd.read_csv(file_path, header=None)
columns = [
    "duration",
    "protocol_type",
    "service",
    "flag",
    "src_bytes",
    "dst_bytes",
    "land",
    "wrong_fragment",
    "urgent",
    "hot",
    "num_failed_logins",
    "logged_in",
    "num_compromised",
    "root_shell",
    "su_attempted",
    "num_root",
    "num_file_creations",
    "num_shells",
    "num_access_files",
    "num_outbound_cmds",
    "is_host_login",
    "is_guest_login",
    "count",
    "srv_count",
    "serror_rate",
    "srv_serror_rate",
    "rerror_rate",
    "srv_rerror_rate",
    "same_srv_rate",
    "diff_srv_rate",
    "srv_diff_host_rate",
    "dst_host_count",
    "dst_host_srv_count",
    "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate",
    "dst_host_srv_serror_rate",
    "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate",
    "label",
]
data.columns = columns
data = data[selected_columns]

# تبدیل ستون label به عددی
# Convert the label column to numeric
data["label"] = data["label"].apply(lambda x: 0 if x == "normal." else 1)

# پردازش ستون‌های متنی
# Process categorical columns
categorical_columns = ["protocol_type", "service", "flag"]
encoder = LabelEncoder()
for col in categorical_columns:
    data[col] = encoder.fit_transform(data[col])

# مقیاس‌بندی داده‌های عددی
# Scale numeric data
scaler = MinMaxScaler()
numeric_columns = data.columns.drop("label")
data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

# ایجاد توالی‌های زمانی
# Create time sequences
sequence_length = 100
X, y = [], []

for i in range(len(data) - sequence_length):
    X.append(data.iloc[i : i + sequence_length, :-1].values)  # ورودی
    y.append(data.iloc[i + sequence_length, -1])  # برچسب

X = np.array(X)
y = np.array(y)

# ذخیره داده‌های پیش‌پردازش‌شده
# Save preprocessed data
np.save("X.npy", X)
np.save("y.npy", y)

from sklearn.model_selection import train_test_split

# تقسیم داده‌ها به آموزش و تست
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# نمایش ابعاد داده‌های تقسیم‌شده
# Display the shapes of the split data
print(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
print(f"X_test shape: {X_test.shape}, y_test shape: {y_test.shape}")


# نمایش ابعاد نهایی
# Display the final shapes
print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")
