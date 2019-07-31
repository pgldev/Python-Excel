# Python with pandas
# This script will merge all .xlsx files in the folder to one excel file.
# Also using glob here for getting the files from the system
import pandas
import glob

# this list creates a list with the filepath
list = glob.glob("*.xlsx")
#list where we will append the files from the folder
all_excel_files = []
#loop for the appending itself
for f in list:
    all_excel_files.append(pd.read_excel(f))
#Merges the xlsx files from the all_excel_files with concat.
join = pd.concat(all_excel_files)
# this till make the excel file. temp name is merge_01.xlsx
join.to_excel("merge_01.xlsx")

