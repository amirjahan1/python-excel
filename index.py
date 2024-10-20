import pandas as pd
from khayyam import JalaliDate

 
file_path = "excel.xlsx"  
df = pd.read_excel(file_path)

 
def calculate_date_difference(row):
    try:
        start_date = JalaliDate.strptime(row['تاریخ الحاق اول'], '%Y/%m/%d')
        end_date = JalaliDate.strptime(row['تاریخ پیاده شدن'], '%Y/%m/%d')
        return (end_date - start_date).days
    except:
        return None   

 
df['اختلاف روز'] = df.apply(calculate_date_difference, axis=1)

 
output_file_path = "your_output_excel_file.xlsx"  
df.to_excel(output_file_path, index=False)

print(f" file saved successfully {output_file_path}  ")