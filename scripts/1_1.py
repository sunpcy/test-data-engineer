import pandas as pd

transaction_df = pd.read_csv('/workspaces/test-data-engineer/data/Transactions.csv')

count_session = transaction_df['userId'].value_counts().reset_index()

count_session.columns = ['userId', 'Number of Sessions']
print(count_session)

count_session_sorted_by_userid = count_session.sort_values(by='userId')
print(count_session_sorted_by_userid)