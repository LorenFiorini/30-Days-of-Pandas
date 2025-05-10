import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(
        employee,
        department,
        left_on='departmentId',
        right_on='id'
    )
    print(merged_df)
    max_salaries = merged_df.groupby('name_y').max().reset_index()
    print(max_salaries)
    max_salaries.rename(
        columns={
            'name_y': 'Department',
            'salary': 'MaxSalary'
        },
        inplace=True
    )
    print(max_salaries)
    ans_df = pd.merge(
        merged_df,
        max_salaries,
        left_on=['name_y', 'salary'],
        right_on=['Department', 'MaxSalary']    
    )
    print(ans_df)
    ans = ans_df[['Department', 'name_x_x', 'salary']]
    ans = ans.rename(
        columns={
            'name_x_x': 'Employee',
            'salary':'Salary'
        }
    )
    return ans
