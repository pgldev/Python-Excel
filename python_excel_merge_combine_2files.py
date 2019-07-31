# this python scrpt combindes 2 excel sheets (.xlsx) with the famous vlooup function on a specific colum in the excel sheet.

#importing pandas here as pd
import pandas as pd


# dataframe 1 gets the first xlsx file here with the sheet in excel as Table 1
df1 = pd.read_excel("file01.xlsx", sheet_name="Table1")


# dataframe 3 opens the second xlsx file here with the sheet in excel Table 2
df3 = pd.read_excel("file02.xlsx", sheet_name="Table2")


# here we merge the excel sheets on the speficic colum b wich matches in both Table1 and Table2. (almost same as the vlookup function in excel) 
results2 = df1.merge(df3, on="B", how="left")

# makes a new excel file with the result
results2.to_excel("combined_merged.xlsx")


