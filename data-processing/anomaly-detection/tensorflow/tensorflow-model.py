import tensorflow as tf

# Load dataset
data = tf.data.Dataset.range(100)

# Create a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

print("TensorFlow model initialized for anomaly detection.")
