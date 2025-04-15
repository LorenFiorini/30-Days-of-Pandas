# Schema definition
data = [[1, 'aLice'], [2, 'bOB']]
users = pd.DataFrame(
    data, columns=['user_id', 'name']
).astype({'user_id':'Int64', 'name':'object'})