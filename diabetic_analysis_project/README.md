# Diabetic Patient Data Analysis 🩺📊

## 📌 Project Overview
This project focuses on analyzing and classifying diabetic patient data based on various clinical and demographic features. It covers the entire data pipeline from cleaning and preprocessing to exploratory analysis, feature engineering, and binary classification using logistic regression and random forest classifiers.

---

## 📂 Dataset Description
The dataset includes columns such as:
- **Blood Measurements**: `chol`, `stab.glu`, `hdl`, `ratio`, `glyhb`, `bp.1s`, `bp.1d`, `bp.2s`, `bp.2d`
- **Physical Attributes**: `height`, `weight`, `waist`, `hip`, `frame`
- **Demographics**: `location`, `age`, `gender`

---

## 🛠️ Tasks Performed
1. Loaded and cleaned data from `diabetes.xlsx`, skipping metadata rows and stripping whitespace
2. Imputed missing numeric values using column means
3. Applied one-hot encoding to categorical features: `location`, `gender`, and `frame`
4. Created a binary classification target `glyhb_risk` (1 if `glyhb` > 7, else 0)
5. Split data into train/test sets using both 60/40 and 70/30 ratios
6. Built and evaluated two models:
   - Logistic Regression
   - Random Forest (with tuned hyperparameters)
7. Evaluated models with:
   - Confusion Matrix
   - Classification Report (Precision, Recall, F1-Score)
   - ROC Curve and AUC Score
   - Feature Importance Plot

---

## 🔍 Missing Value Handling
- Identified missing values using `.isnull().sum()`
- Noted high missingness in `bp.2s` and `bp.2d` (≈65%)
- Imputed numeric columns using `SimpleImputer(strategy='mean')`

---

## 📊 Tools & Libraries
- Python
- Pandas
- Scikit-learn
- Matplotlib, Seaborn (for visualization)

---

## 🧠 Models & Performance
- **Logistic Regression**
  - Accuracy: 93.2%
  - AUC: 0.92

- **Random Forest**
  - Accuracy: 93.2%
  - AUC: 0.92
  - Feature Importance: `stab.glu`, `age`, and `ratio` are top predictors

---

## 📈 Visual Outputs
- Feature Importance Bar Chart
- ROC Curve (AUC = 0.92)
- Clean Confusion Matrix & Metrics Report

---

## 📁 Files Included
- `main.py` – Initial processing pipeline: cleaning, encoding, train/test split
- `Diabetes_Risk_Classifier.ipynb` – Full end-to-end notebook with model training, evaluation, and visualizations
- `diabetes.xlsx` – Source dataset
- `mysubmission3.csv` – Exported version of the processed dataset
- `README.md` – Project documentation

---

## 👨‍💻 Author
**Ganesh Paparaju**

---

## 📬 Contact
For questions, feedback, or collaboration, connect via [GitHub](https://github.com/GaneshPaparaju) or LinkedIn.
