#Load The Data
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("AmesHousing.csv")
df.head()

#Data Cleaning
df.isnull().sum().sort_values(ascending=False)
df = df.dropna(subset=['SalePrice'])  
df.fillna(method='ffill', inplace=True)  

#Visualize Price Dist.
import seaborn as sns
sns.histplot(df['SalePrice'], kde=True)
plt.show()

#Visualize Relationships
sns.scatterplot(data=df, x="Gr Liv Area", y="SalePrice")
plt.show()

#Feature Engineering: Convert categorical variables to numerical
categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

#Feature Engineering: Log transformation of SalePrice and create HouseAge feature
import numpy as np
df['SalePrice'] = np.log1p(df['SalePrice']) 

#Feature Engineering: Create HouseAge feature
df['HouseAge'] = df['Yr Sold'] - df['Year Built']

#Train and Test Split
from sklearn.model_selection import train_test_split
X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Fit Model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

#Evaluate the model
from sklearn.metrics import r2_score, root_mean_squared_error
y_pred = model.predict(X_test)
rmse = root_mean_squared_error(y_test, y_pred)
print("R²:", r2_score(y_test, y_pred))
print("RMSE:", rmse)

# Plot Actual vs Predicted Prices
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, label="Predictions", alpha=0.6)
# Plot the y = x line
min_val = min(min(y_test), min(y_pred))
max_val = max(max(y_test), max(y_pred))
plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', label="Ideal: Actual = Predicted")
# Add + or - RMSE bands
plt.plot([min_val, max_val], [min_val + rmse, max_val + rmse], color='green', linestyle='--', label=f'y = x + RMSE ({rmse:.2f})')
plt.plot([min_val, max_val], [min_val - rmse, max_val - rmse], color='green', linestyle='--', label=f'y = x - RMSE ({rmse:.2f})')
# Labels, title, legend
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

