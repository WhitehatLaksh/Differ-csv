import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Define the scope and credentials to access Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Authenticate and access the Google Sheets API
gc = gspread.authorize(credentials)

# Open the Google Sheet by its URL
sheet_url = 'YOUR_GOOGLE_SHEET_URL'
worksheet = gc.open_by_url(sheet_url).sheet1  # Assuming the data is in the first sheet

# Read data from Google Sheet into a pandas DataFrame
df1 = pd.DataFrame(worksheet.get_all_records())

# Load the second CSV file into a pandas DataFrame
df2 = pd.read_csv('file2.csv')

# Perform a left join on the two DataFrames using 'phone' and 'terminating_number' as keys
merged_df = pd.merge(df1, df2, how='left', left_on='phone', right_on='terminating_number')

# Save the merged DataFrame to a third CSV file
merged_df.to_csv('merged_result.csv', index=False)

# Display a message indicating successful CSV creation
print("Merged result saved to 'merged_result.csv'")
