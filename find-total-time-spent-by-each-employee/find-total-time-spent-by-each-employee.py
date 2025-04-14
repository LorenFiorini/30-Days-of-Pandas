import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['time_spent'] = employees['out_time'] - employees['in_time']
    ans = employees.groupby(['event_day', 'emp_id'])['time_spent'].sum()
    print(ans)
    ans = ans.reset_index()
    print(ans)
    # ans.rename(columns={'event_day': 'day', 'time_spent': 'total_time'}, inplace=True)
    
    ans.rename(
        columns={
            'event_day' : 'day',
            'time_spent' : 'total_time'
        },
        inplace=True
    )
    print(ans)
    return ans
