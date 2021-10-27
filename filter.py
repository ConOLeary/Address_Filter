import pandas as pd

df= pd.read_csv('addresses.csv')
df.fillna(0)
df= df.astype(str)

first_liners= df[df['Address Line1'].str.contains('Canada|Toronto|Ontario|Montreal|Montréal|Quebec|Québec|Vancouver|British Columbia|Ottawa|Alberta|British Columbia|Manitoba|New Brunswick|Newfoundland|Labrador|Nova Scotia|Ontario|Prince Edward Island|Quebec|Saskatchewan')]
second_liners= df[df['Address Line2'].str.contains('Canada|Toronto|Ontario|Montreal|Montréal|Quebec|Québec|Vancouver|British Columbia|Ottawa|Alberta|British Columbia|Manitoba|New Brunswick|Newfoundland|Labrador|Nova Scotia|Ontario|Prince Edward Island|Quebec|Saskatchewan')]
third_liners= df[df['Address Line3'].str.contains('Canada|Toronto|Ontario|Montreal|Montréal|Quebec|Québec|Vancouver|British Columbia|Ottawa|Alberta|British Columbia|Manitoba|New Brunswick|Newfoundland|Labrador|Nova Scotia|Ontario|Prince Edward Island|Quebec|Saskatchewan')]
forth_liners= df[df['Address Line4'].str.contains('Canada|Toronto|Ontario|Montreal|Montréal|Quebec|Québec|Vancouver|British Columbia|Ottawa|Alberta|British Columbia|Manitoba|New Brunswick|Newfoundland|Labrador|Nova Scotia|Ontario|Prince Edward Island|Quebec|Saskatchewan')]
fifth_liners= df[df['Address Line5'].str.contains('Canada|Toronto|Ontario|Montreal|Montréal|Quebec|Québec|Vancouver|British Columbia|Ottawa|Alberta|British Columbia|Manitoba|New Brunswick|Newfoundland|Labrador|Nova Scotia|Ontario|Prince Edward Island|Quebec|Saskatchewan')]

all_liners= first_liners.append([second_liners, third_liners, forth_liners, fifth_liners])


writer= pd.ExcelWriter('canadians.xlsx') 
df.to_excel(writer, sheet_name='canadians', index=False, na_rep='')

# Auto-adjust columns' width
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['canadians'].set_column(col_idx, col_idx, column_width)

writer.save()