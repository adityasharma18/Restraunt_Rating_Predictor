# 🍽️ Restaurant Rating Predictor

A Machine Learning project that predicts the **aggregate rating** of a restaurant based on various features like location, votes, cost, and online order availability. Built using Python, Pandas, and Scikit-learn.

---

## 🎯 Objective

To build a regression model that can predict restaurant ratings from a custom dataset.

---

## 📁 Dataset

- File: `Dataset.csv` (inside `Data/` folder)
- Features include:
  - `location`, `rest_type`, `cuisines`, `votes`
  - `approx_cost(for two people)`, `online_order`, `book_table`
- Target: `rate`

---

## 🧠 ML Pipeline

1. 📥 Load & explore dataset
2. 🧹 Handle missing values & clean data
3. 🔄 Encode categorical features
4. ✂️ Train-test split
5. 🤖 Train regression model (Linear Regression)
6. 📈 Evaluate using R² Score & MSE
7. 💾 Save model using `joblib`

---

## 📊 Model Result

- **R² Score (Loaded Model): `0.1562`**
- Model file saved as: `model.pkl`

---

## 🛠️ Tech Stack

- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Joblib

---

## 🚀 How to Run

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the notebook
jupyter notebook restaurant_rating.ipynb
