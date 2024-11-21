import pandas as pd
from datetime import datetime

now = datetime.now()
print(now)

transaction_df = pd.read_csv('/workspaces/test-data-engineer/data/Transactions.csv')

def convert_year(date_str):
    date_part, time_part = date_str.split(' ')
    month, day, year_be = date_part.split('/')
    year = int(year_be) - 543
    return f"{month}/{day}/{year} {time_part}"

transaction_df['date'] = transaction_df['date'].apply(convert_year)
transaction_df['date'] = pd.to_datetime(transaction_df['date'], format='%m/%d/%Y %H:%M:%S')
# print(transaction_df)
# print(transaction_df.dtypes)

latest_user_time = transaction_df.groupby('userId')['date'].max().reset_index()
# print(latest_user_time)

latest_user_time['days_since_latest_user_time'] = (now - latest_user_time['date']).dt.days
# print(latest_user_time)

print(latest_user_time[['userId', 'days_since_latest_user_time']])