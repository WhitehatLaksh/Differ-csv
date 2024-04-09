import pandas as pd

df2 = pd.read_csv('/home/lakshaysaini/Downloads/telnyx-report.csv')
df1 = pd.read_csv('/home/lakshaysaini/Downloads/clientcsv.csv')

merged_df = pd.merge(df2, df1, how='inner', left_on='terminating_number', right_on='phone')

merged_df.to_csv('merged-csv.csv', index=False)


print("Merged result saved to 'merged-csv.csv'")
