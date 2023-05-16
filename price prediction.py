import pandas as pd
import yfinance as yf
from datetime import date, timedelta
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
import plotly.graph_objects as go

today = date.today()
end_date = today.strftime("%Y-%m-%d")
start_date = (today - timedelta(days=5000)).strftime("%Y-%m-%d")

data = yf.download('XU100.IS', start=start_date, end=end_date, progress=False)
data.reset_index(drop=True, inplace=True)

# Prepare the data for modeling
X = data[["Open", "High", "Low", "Volume"]].values
y = data["Close"].values
y = y.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the model
model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.compile(optimizer="adam", loss="mean_squared_error")

# Train the model
model.fit(X_train, y_train, batch_size=1, epochs=10)

# Make predictions on the test dataset
y_pred = model.predict(X_test)

# Evaluate the model on the test dataset
loss = model.evaluate(X_test, y_test)

# Calculate MAE
mae = mean_absolute_error(y_test, y_pred)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Print MAE and RMSE values
print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)
# Print the loss value
print("Loss:", loss)


"""
# Plot the candlestick chart
figure = go.Figure(data=[go.Candlestick(x=data.index,
                                        open=data["Open"],
                                        high=data["High"],
                                        low=data["Low"],
                                        close=data["Close"])])
figure.update_layout(title="BIST 100")
figure.update_xaxes(rangeslider_visible=False)
figure.show()"""