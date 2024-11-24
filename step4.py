import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split
import numpy as np

# بارگذاری داده‌های آماده شده
# Load the prepared data
X = np.load("X.npy")
y = np.load("y.npy")

# تقسیم داده‌ها به بخش‌های آموزش و تست
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# طراحی مدل LSTM
# Design the LSTM model
model = Sequential(
    [
        LSTM(64, input_shape=(100, 16), return_sequences=True, activation="tanh"),
        Dropout(0.2),
        LSTM(32, activation="tanh"),
        Dropout(0.2),
        Dense(1, activation="sigmoid"),
    ]
)

# کامپایل کردن مدل
# Compile the model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"],
)

# نمایش خلاصه مدل
# Display the model summary
model.summary()

# آموزش مدل
# Train the model
history = model.fit(
    X_train,
    y_train,
    validation_data=(X_test, y_test),
    epochs=10,
    batch_size=128,
    verbose=2,
)

# ارزیابی مدل
# Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=2)
print(f"Test Accuracy: {test_accuracy:.2%}")

# ذخیره مدل
# Save the model
model.save("rnn_model.h5")

# رسم نمودارها
# Plot accuracy and loss graphs
import matplotlib.pyplot as plt

# رسم نمودار دقت
# Accuracy plot
plt.figure(figsize=(12, 6))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Model Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.grid()
plt.show()

# رسم نمودار Loss
# Loss plot
plt.figure(figsize=(12, 6))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Model Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.grid()
plt.show()
