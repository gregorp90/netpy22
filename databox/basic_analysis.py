import pandas as pd

df = pd.read_csv('./databox/databox_data/query-20220118.csv', sep=';',
                 decimal=',')
df.count

df.groupby(['space_id']).size().reset_index(name='counts').sort_values(
    by=['counts'])

df2 = df.loc[df['space_id'] == 263771, :]
df2.sort_values(by=['type'])

df_unq = df.drop_duplicates()
df_counts = df_unq.groupby(['space_id']).size().reset_index(
    name='counts').sort_values(by='counts', ascending=False)
