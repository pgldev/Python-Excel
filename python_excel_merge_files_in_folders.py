# Python with pandas
# This script will merge all .xlsx files in the folder to one excel file.
# Also using glob here for getting the files from the system
import pandas
import glob

list = glob.glob("*.xlsx")
all_excel_files = []
for f in list:
    all_excel_files.append(pd.read_excel(f))
join = pd.concat(all_excel_files)
join.to_excel("merge_01.xlsx")
