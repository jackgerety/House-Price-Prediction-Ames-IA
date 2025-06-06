# 🏠 Ames Housing Price Prediction

This project uses **linear regression** to predict house prices in Ames, Iowa, based on a dataset from Kaggle. It's a beginner-friendly regression project aimed at applying core data science and machine learning skills, including data preprocessing, feature engineering, model training, and evaluation.

---

## 📁 Dataset

- **Source**: [Kaggle - House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)
- **Target variable**: `SalePrice` (USD)
- **Features**: 79 explanatory variables (categorical + numerical)

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Environment**: Jupyter Notebook (recommended) or Python scripts
- **Libraries**:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`

---

## 🧪 Features & Workflow

### 1. **Data Preprocessing**
- Handle missing values
- Encode categorical features (One-Hot Encoding, Ordinal Mapping)
- Normalize/scale numerical features

### 2. **Exploratory Data Analysis**
- Visualize feature relationships (e.g., `GrLivArea` vs. `SalePrice`)
- Check feature correlations
- Remove outliers if needed

### 3. **Modeling**
- Train a **Linear Regression** model using `scikit-learn`
- Optionally compare with Ridge, Lasso, or DecisionTreeRegressor

### 4. **Evaluation**
- Evaluate using:
  - **R² score**
  - **Root Mean Squared Error (RMSE)**
- Plot **predicted vs. actual prices**

---

## 📊 Sample Results

| Metric | Value (Example) |
|--------|-----------------|
| R² Score | 0.85 |
| RMSE     | \$20,000 |

> *Note: Your results may vary depending on preprocessing choices.*

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/ames-housing-regression.git
cd ames-housing-regression
