# Schema definition
data = [
    ['1', '2020-11-28', '4', '32'],
    ['1', '2020-11-28', '55', '200'],
    ['1', '2020-12-3', '1', '42'],
    ['2', '2020-11-28', '3', '33'],
    ['2', '2020-12-9', '47', '74']
]
employees = pd.DataFrame(
    data,
    columns=['emp_id', 'event_day', 'in_time', 'out_time']
).astype({
    'emp_id': 'Int64',
    'event_day': 'datetime64[ns]',
    'in_time': 'Int64',
    'out_time': 'Int64'
})
