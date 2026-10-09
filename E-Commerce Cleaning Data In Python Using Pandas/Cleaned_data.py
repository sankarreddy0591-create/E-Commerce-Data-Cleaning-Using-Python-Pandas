
# Cleaning Data E-commerce

# import required libraries
import pandas as pd

# load dataset into  a pandas
df=pd.read_csv("Data/FashionDataset.csv")
print("Dataset loaded successful:", df)

# finding the number of rows and columns
print(" Final Shape:", df.shape)

# checking the columns names
print("Check Columns Name:", df.columns)

# Remove Unwantede Columns in the df
df.drop(columns="Unnamed: 0", inplace=True)
print("Remove Unwanted Coulmn Successful:", df)

# Renaming the columns "Deatils" to "Details" in the df
df.rename(columns={"Deatils" : "Details"}, inplace=True)
print("The Columns Rename Comlpeted ", df)

# Checking The Duplicated In The df
df.duplicated().value_counts()
print("display the duplicated values", df.duplicated().value_counts())

# checking the total of duplictes
df.duplicated().sum()

print(" Total Duplicates:", df.duplicated().sum())

# drop the duplictes in the df
df.drop_duplicates(inplace=True)
print("Remove Duplicated successful:", df.duplicated().sum())

# reset the index columns
df=df.reset_index()
print("reset the index columns:", df)

# remove reset the index columns
df=df.drop(columns="index")
print("Remove reset the index columns completed :", df)

#checking the null or missing values in the df
df.isna().sum()
print("Check the null valeus:", df.isna().sum())

# dropna the the null or missing values in the df
df.dropna(inplace=True)
print("Dropna the null valued successful:", df)

# the first latte to capitals
df["BrandName"]=df["BrandName"].apply(lambda x: x.capitalize())
df["Details"]=df["Details"].apply(lambda x : x.capitalize())

print("the first letter to caplitals:", df)

# Change "Nan" to " NA VALUED" values from the "Sizes"
df["Sizes"]=df["Sizes"].replace("Nan", "NA VALUED")
print("Changed the valued Nan to NA VALUED:", df)

# check the not " NA VALUED" from the Sizes in the df
df=df[df["Sizes"] !="NA VALUED"]

print("Check not NA VLUED:", df)

# Change "Nan" to "No Discount" from the Discount column
df["Discount"]=df["Discount"].replace("Nan" , "No Discount")
print("Changed Disconts Successful:", df)

# reset the columns index
df.reset_index()
print("Reset the index:", df)

#remove the index column
df=df.reset_index().drop(columns="index")
print("Remove the index coulmn Seccessful:", df)