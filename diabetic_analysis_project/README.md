
# Diabetic Patient Data Analysis 🩺📊

## 📌 Project Overview
This project focuses on analyzing and preprocessing a medical dataset related to diabetic patients. It includes physical measurements, blood-related parameters, and demographic attributes like age and gender. The aim is to handle missing values, encode categorical data, and prepare training/testing datasets for further modeling or analysis.

---

## 📂 Dataset Description
The dataset includes columns such as:
- chol, stab.glu, hdl, ratio, glyhb, bp.1s, bp.1d, bp.2s, bp.2d (blood measurements)
- height, weight, waist, hip, frame (physical data)
- location, age, gender (categorical/demographic)

---

## 🛠️ Tasks Performed
1. Imported Excel file using `pandas.read_excel()`
2. Calculated percentage of missing values across all columns
3. Converted categorical data to numerical form using one-hot encoding (`location`, `gender`, `frame`)
4. Performed two training/testing splits:
   - 60% Training / 40% Testing
   - 70% Training / 30% Testing
5. Exported one version of the split data as `mysubmission3.csv`

---

## 🔍 Missing Value Handling
- Detected missing values using `.isnull().sum()`
- Found high missingness in `bp.2s` and `bp.2d` columns (65%)
- These can be imputed or replaced with dummy values if needed before modeling

---

## 📊 Tools & Libraries
- Python
- Pandas
- Scikit-learn

---

## 💡 Learning Outcomes
- Data quality profiling and missing value analysis
- Categorical encoding for medical/demographic attributes
- Train/test split strategies for modeling pipelines

---

## 📁 Files Included
- `main.py` – Full pipeline with missing data analysis, encoding, and splitting
- `diabetes.xlsx` – Source dataset
- `mysubmission3.csv` – Processed test dataset output

---

## 👨‍💻 Author
- Ganesh Paparaju

---

## 📬 Contact
For questions, feedback, or collaboration, feel free to reach out via GitHub or LinkedIn.
