# **Diabetes Risk Predictor**

### **Bridging Health Equity Gaps with Random Forest Machine Learning: Predicting Diabetes Risk Using Non-Laboratory Metrics**

## **Overview**

Diabetes is a major public health concern, but identifying individuals at risk often relies on clinical measurements such as blood glucose and A1C levels. These tests may not always be easily accessible, especially in communities with limited healthcare resources.

This project explores whether **non-laboratory health and lifestyle indicators** can be used to predict diabetes risk through machine learning. Using data from the **2015 CDC Behavioral Risk Factor Surveillance System (BRFSS)**, I developed a **Random Forest classification model** to identify patterns associated with diabetes while relying on information that can be collected without laboratory testing.

## **Research Paper**

This project was developed alongside an independent research paper:

📄 [**Read the Full Research Paper**](https://docs.google.com/document/d/1U6VxUDySUsW4MW0OIUbcaDIIamV0W6srLGFGeqyPLqQ/edit?tab=t.dh5v6gcn4hd6)

**Title:**  
*Bridging Health Equity Gaps with Random Forest Machine Learning: Predicting Diabetes Risk Using Non-Laboratory Metrics*

**Author:**  
Aditi Chaugule

The paper discusses the dataset, preprocessing, model development, evaluation, feature relationships, and potential applications of the project.

*This is an independent, unpublished research paper.*

## **Dataset**

The project uses a modified version of the **2015 CDC Behavioral Risk Factor Surveillance System (BRFSS)** dataset.

The dataset contains **70,693 records**, balanced between:

* **35,346 individuals with diabetes**  
* **35,346 individuals without diabetes**

The model uses non-laboratory indicators such as:

* High blood pressure  
* High cholesterol  
* BMI  
* Smoking  
* History of stroke  
* Heart disease or heart attack  
* Physical activity  
* Fruit consumption  
* Vegetable consumption  
* Heavy alcohol consumption  
* General health  
* Mental health days  
* Physical health days  
* Difficulty walking  
* Sex  
* Age group

## **Methodology**

### **1\. Data Selection**

Relevant variables were selected from the original BRFSS dataset while removing unnecessary features.

### **2\. Data Preprocessing**

The dataset was prepared for machine learning through several preprocessing steps:

* Selected relevant health and demographic variables  
* Grouped mental and physical health days into five severity categories  
* Applied label encoding to categorical variables  
* Applied `MinMaxScaler` to normalize numerical features  
* Balanced the dataset so that the diabetic and non-diabetic classes contained an equal number of records

### **3\. Train/Test Split**

The dataset was divided into:

* **90% training data**  
* **10% testing data**

### **4\. Model**

A **Random Forest Classifier** from `scikit-learn` was used for classification.

The model was configured with:

* **100 estimators**  
* `class_weight='balanced'`  
* **Maximum depth of 7**

Random Forest was selected because it can capture relationships between multiple health-related variables while providing feature importance information that can help interpret the model.

## **Results**

The model achieved the following results on the test set:

| Metric | Result |
| ----- | ----- |
| Accuracy | **75.3%** |
| Precision | **73.9%** |
| Recall | **80.3%** |

The model's **80.3% recall** indicates that it was able to correctly identify a relatively high proportion of individuals classified as diabetic in the test data.

## **Model Insights**

Feature analysis showed that several variables had particularly strong relationships with diabetes risk.

### **Strongest Feature Relationships**

| Feature | Correlation |
| ----- | ----- |
| General Health | **0.41** |
| High Blood Pressure | **0.38** |
| High Cholesterol | **0.29** |
| BMI | **0.29** |
| Age | **0.28** |
| Physical Activity | **\-0.16** |

General health, high blood pressure, BMI, high cholesterol, and age were among the strongest predictors identified by the model.

Physical activity showed the strongest negative correlation with the diabetes outcome among the listed variables.

## **Technologies**

This project was developed using:

* **Python**  
* **Pandas**  
* **NumPy**  
* **Scikit-learn**  
* **Matplotlib**  
* **Seaborn**

## **Project Structure**

The repository currently contains:

Diabetes\_Predictor\_AC/

│

├── .gitignore

├── .replit

├── 2split.csv

├── README.md

├── diabetes\_dataset\_even\_split.csv

├── full.csv

├── head.csv

├── main.py

├── pyproject.toml

├── small.csv

├── util.py

└── uv.lock

### **File Descriptions**

| File | Description |
| ----- | ----- |
| `.gitignore` | Specifies files and directories that Git should ignore |
| `.replit` | Replit project configuration |
| `2split.csv` | Dataset file used during data preparation |
| `README.md` | Documentation for the project |
| `diabetes_dataset_even_split.csv` | Balanced diabetes dataset used for modeling |
| `full.csv` | Full dataset used during the data preparation process |
| `head.csv` | Subset containing the beginning of the dataset |
| `main.py` | Main Python file containing the project code |
| `pyproject.toml` | Python project configuration and dependency information |
| `small.csv` | Smaller dataset used during development/testing |
| `util.py` | Utility functions used by the project |
| `uv.lock` | Locked Python dependency versions |

## **Future Applications**

This project could serve as a foundation for exploring more accessible diabetes risk assessment tools.

Potential future directions include:

* Comparing model performance across different demographic groups  
* Incorporating additional datasets  
* Developing a user-facing risk assessment application

## **Author**

**Aditi Chaugule**

This project represents an independent exploration of machine learning, healthcare accessibility, and data science.

---

### **Disclaimer**

This project is intended for **educational and research purposes only**. It is not a medical diagnostic tool and should not be used to make healthcare decisions.