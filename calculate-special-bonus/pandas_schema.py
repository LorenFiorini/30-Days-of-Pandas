
# Schema definition
data = [
    [2, 'Meir', 3000],
    [3, 'Michael', 3800],
    [7, 'Addilyn', 7400],
    [8, 'Juan', 6100],
    [9, 'Kannon', 7700]]
employees = pd.DataFrame(
    data,
    columns=['employee_id', 'name', 'salary']
    ).astype({
        'employee_id':'int64',
        'name':'object',
        'salary':'int64'}
    )
