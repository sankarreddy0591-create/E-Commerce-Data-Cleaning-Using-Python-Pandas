# 🛍️ E-Commerce-Data-Cleaning-Using-Python-Pandas

E-commerce Cleaning Data

## 🛍️ E-Commerce Data Cleaning Using Python & Pandas

## 🧹 End-to-End Data Cleaning Project 🐍
---

 Technology: Python 🐼 Library: Pandas 📊 Dataset: Fashion E-Commerce Dataset 🎯 Objective: Clean, standardize, validate, and export an e-commerce dataset for further analysis.

## 📌 Project Overview
---
This project demonstrates a complete Data Cleaning workflow using Python and Pandas.

The project uses a fashion e-commerce dataset containing product-related information such as brand names, product details, sizes, discounts, and other attributes.

The main goal is to transform the raw dataset into a clean, consistent, and analysis-ready dataset.

### The project covers:
---
```
📂 Loading raw data
🔍 Exploring the dataset
🗑️ Removing unnecessary columns
✏️ Renaming incorrect column names
🔁 Detecting duplicate records
🧹 Removing duplicate records
❓ Identifying missing values
🗑️ Removing incomplete records
🔤 Standardizing text values
📏 Cleaning size information
💰 Cleaning discount information
💾 Exporting the cleaned dataset
✅ Validating the final output
```
### 🎯 Project Objective
---
The primary objective of this project is to improve the quality and consistency of the raw e-commerce dataset.

Before Cleaning
---

```
❌ Unwanted columns
❌ Incorrect column name
❌ Duplicate records
❌ Missing values
❌ Inconsistent text formatting
❌ Invalid size values
❌ Unclear discount values
```

After Cleaning
---
```
✅ Relevant columns
✅ Correct column names
✅ Duplicate-free records
✅ Missing values handled
✅ Standardized text
✅ Clean size values
✅ Clear discount information
✅ Analysis-ready dataset
```

## 🔄 Data Cleaning Workflow
---
```
📂 Load Dataset
      ↓
🔍 Explore Dataset
      ↓
📏 Check Dataset Shape
      ↓
📋 Check Column Names
      ↓
🗑️ Remove Unwanted Column
      ↓
✏️ Rename Column
      ↓
🔁 Detect Duplicate Rows
      ↓
📊 Visualize Duplicates
      ↓
🧹 Remove Duplicate Rows
      ↓
🔢 Reset Index
      ↓
❓ Check Missing Values
      ↓
🗑️ Remove Missing Records
      ↓
🔤 Standardize Text Values
      ↓
📏 Clean Size Values
      ↓
💰 Clean Discount Values
      ↓
💾 Save Clean Dataset
      ↓
✅ Validate Final Dataset
```

## 1️⃣ Import Required Libraries
---
The project starts by importing the required Python libraries.

🐼 Pandas

Pandas is the main library used for data manipulation and cleaning.

📊 Matplotlib

Matplotlib is used to visualize the number of duplicate and unique records.

🛠️ Technologies
🐍 Python
🐼 Pandas
📊 Matplotlib

## 2️⃣ Load the Dataset 📂
---
The raw fashion e-commerce dataset is loaded from a CSV file using Pandas.

The dataset is stored in a DataFrame named:

df
Data Flow

```
📄 FashionDataset.csv
        ↓
   pd.read_csv()
        ↓
🐼 Pandas DataFrame
        ↓
        df
```

## 3️⃣ Explore the Dataset 🔍
---
The dataset is initially explored to understand its structure and contents.

👀 First Five Records
The first five rows are displayed using head().

Purpose
Understand the dataset structure
Inspect the first records
Identify available information
👀 Last Five Records
The last five rows are displayed using tail().

Purpose
Check the ending records
Confirm that the dataset loaded correctly

## 4️⃣ Dataset Information 📋
---

The info() method is used to inspect:

Column names
Non-null values
Data types
Number of entries
This helps identify potential data-quality issues before cleaning.

## 5️⃣ Check Dataset Shape 📏
---

The dataset shape is checked to determine:

Number of Rows
+
Number of Columns
This provides a basic understanding of the dataset size.

## 6️⃣ Check Column Names 📋
---

All column names are displayed to identify:

Unwanted columns
Incorrect names
Columns requiring modification

## 7️⃣ Remove Unwanted Column 🗑️
---

The column:

Unnamed: 0
is removed from the dataset.

Why?
This column is an unnecessary index-like column and does not provide useful product information for analysis.

Result

```
❌ Unnamed: 0
       ↓
🗑️ Removed
```

## 8️⃣ Rename Incorrect Column ✏️
---

The dataset contains a spelling mistake:

❌ Deatils
It is corrected to:

✅ Details
Why?
Correct column names improve:

Readability
Data quality
Code consistency
Professional presentation

## 9️⃣ Detect Duplicate Records 🔁
---

Duplicate rows are checked using Pandas.

The project identifies both:

✅ Unique Rows
🔁 Duplicate Rows
The number of duplicate and non-duplicate records is calculated.

## 🔟 Visualize Duplicate Records 📊
---

Matplotlib is used to create a bar chart showing the distribution of:

Duplicate records
Unique records
🎯 Purpose
Visualization provides a quick understanding of how many duplicate records exist in the dataset.

## 1️⃣1️⃣ Count Duplicate Records 🔢
---

The total number of duplicate records is calculated.

This helps determine how much duplicate data needs to be removed.

## 1️⃣2️⃣ Remove Duplicate Records 🧹
---

Duplicate rows are removed from the DataFrame.

After removal, the dataset is checked again to confirm that duplicate records no longer exist.

```
Expected Result
Duplicate Rows
      ↓
   Removed
      ↓
0 Duplicate Rows
```

## 1️⃣3️⃣ Reset DataFrame Index 🔢
---

After removing duplicate rows, the DataFrame index may contain gaps.

The index is reset so that the cleaned dataset has a continuous index.

Before
```
0
1
2
5
7
8
```

After
```
0
1
2
3
4
5
```

This makes the cleaned DataFrame more organized.

## 1️⃣4️⃣ Identify Missing Values ❓
---

Missing values are checked using:

isna()
The total missing values in each column are calculated.

Purpose
To identify incomplete information that requires cleaning.

## 1️⃣5️⃣ Handle Missing Records 🧹
---

Rows containing missing values are removed from the dataset.

This creates a dataset containing complete records for the remaining fields.

```
Cleaning Process
❓ Missing Records
       ↓
🗑️ Remove
       ↓
✅ Complete Records

```

⚠️ In a production project, missing values should be analyzed before deciding whether to delete rows or use imputation. This project uses row removal as part of the data-cleaning workflow.

## 1️⃣6️⃣ Standardize Brand Names 🔤
---

Brand names are standardized using capitalization.

For example:

```
adidas
ADIDAS
Adidas
```

are standardized into a consistent text format.

## 🎯 Purpose
---

Consistent text formatting makes categorical data easier to analyze.

## 1️⃣7️⃣ Standardize Product Details 📝
---

The Details column is also standardized using capitalization.

This improves consistency in product descriptions.

Result

```
❌ Inconsistent formatting
        ↓
🔤 Standardized formatting
```

## 1️⃣8️⃣ Inspect Size Information 📏
---

The Sizes column is examined to identify unusual or invalid values.

The project specifically checks the data type and values of individual records to understand how missing-size information is represented.

## 1️⃣9️⃣ Handle Invalid Size Values 🧹
---

Some size records contain the text:

Nan
This value is replaced with:

NA VALUED
The records containing NA VALUED are then removed.

Cleaning Process
```

"Nan"
  ↓
"NA VALUED"
  ↓
🗑️ Remove
  ↓
✅ Valid Size Records

```

This ensures that the final dataset contains meaningful size information.

## 2️⃣0️⃣ Clean Discount Information 💰
---

Some discount values contain:

Nan
These values are replaced with:

No Discount
Why?
This provides a clearer business meaning for products where a discount value is not available.

```
Nan
 ↓
No Discount
```

## 2️⃣1️⃣ Save Cleaned Dataset 💾
---

After completing the cleaning process, the cleaned dataset is exported into two formats.

📄 CSV
Cleaned_Dataset.csv
📊 Excel
Cleaned_Data.xlsx
This makes the cleaned data available for:

Data Analysis
Visualization
Dashboard Development
Machine Learning
Reporting

## 2️⃣2️⃣ Verify the Output ✅
---

The saved CSV and Excel files are loaded again using Pandas.

This confirms that:

```
💾 Data was saved successfully
        ↓
📂 File can be loaded
        ↓
✅ Cleaning output verified
```

## 🧹 Data Cleaning Summary

Cleaning Task	Action
```
📂 Dataset Loading	CSV loaded using Pandas
🗑️ Unwanted Column	Unnamed: 0 removed
✏️ Column Name	Deatils → Details
🔁 Duplicate Detection	Duplicate rows identified
🧹 Duplicate Removal	Duplicate rows removed
🔢 Index	Index reset
❓ Missing Values	Missing records identified
🗑️ Missing Records	Incomplete rows removed
🔤 Brand Names	Capitalization standardized
📝 Details	Capitalization standardized
📏 Sizes	Invalid size values handled
💰 Discount	Nan → No Discount
💾 Export	CSV and Excel created
✅ Validation	Saved files loaded and checked
🛠️ Technologies Used
Technology	Purpose
🐍 Python	Programming Language
🐼 Pandas	Data Cleaning & Manipulation
📊 Matplotlib	Duplicate Data Visualization
📄 CSV	Raw & Cleaned Data Storage
📊 Excel	Cleaned Data Export
```
## 📚 Key Pandas Concepts Learned
---

This project provides practical experience with:

```
🐼 pd.read_csv()
🔍 head()
🔍 tail()
📋 info()
📏 shape
📋 columns
🗑️ drop()
✏️ rename()
🔁 duplicated()
🧹 drop_duplicates()
🔢 reset_index()
❓ isna()
🗑️ dropna()
🔤 apply()
🔄 replace()
💾 to_csv()
📊 to_excel()

```

## 🎯 Learning Outcomes
---

After completing this project, the following concepts are practiced:

✅ Loading datasets using Pandas
✅ Understanding DataFrame structure
✅ Inspecting rows and columns
✅ Identifying unwanted columns
✅ Correcting column names
✅ Detecting duplicate records
✅ Visualizing duplicate records
✅ Removing duplicates
✅ Resetting DataFrame indexes
✅ Identifying missing values
✅ Handling incomplete records
✅ Standardizing text data
✅ Cleaning categorical values
✅ Exporting cleaned data
✅ Validating the final dataset

## 📁 Project Structure
---

```
🛍️ E-Commerce Cleaning Data
│
├── 📁 Data
│   └── 📄 FashionDataset.csv
│
├── 📁 Notebook
|   📓 E-Commerce_Data_Cleaning.ipynb
│
├── 📁 Output
│   ├── 📄 Cleaned_Dataset.csv
│   └── 📄 Cleaned_Data.xlsx
|
├── 📁 Visualizations
|   └── 📊 duplicate_rows.png
│
├── 📖 README.md
│
├── Cleaned_data.py
│
└── 📖 README.md
```

## 🚀 Future Improvements
---

The project can be further improved by adding:

🔹 Missing-value percentage analysis
🔹 Outlier detection
🔹 Data-type validation
🔹 More advanced text cleaning
🔹 Standardization of all categorical columns
🔹 Data quality validation checks
🔹 Before-vs-after cleaning statistics
🔹 Exploratory Data Analysis
🔹 E-commerce sales analysis dashboard
🔹 Automated data-cleaning pipeline

## 🏆 Conclusion
---

This project demonstrates how Python and Pandas can be used to transform a raw e-commerce dataset into a cleaner and more consistent dataset.

The workflow covers the complete data-cleaning process, including dataset exploration, unwanted-column removal, column correction, duplicate handling, missing-value handling, text standardization, size cleaning, discount cleaning, and final dataset export.

The final cleaned datasets are saved in both CSV and Excel formats, making them ready for further Data Analysis, Visualization, Dashboard Development, or Machine Learning.

