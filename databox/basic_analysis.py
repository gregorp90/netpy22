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

df_counts_top = df_counts.iloc[0:1000, ]

df_out_SBM_1000 = df_unq[df_unq['space_id'].isin(df_counts_top['space_id'])]
df_out = pd.DataFrame({
    'space_id': df_out_SBM_1000['space_id'],
    'data_source': df_out_SBM_1000['key']
})
df_out.to_csv('SBM_1000.csv')
