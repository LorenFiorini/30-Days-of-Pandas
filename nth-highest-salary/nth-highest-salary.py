import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    # print(unique_salaries)
    unique_salaries_sorted = unique_salaries.sort_values(ascending = False)
    # print(unique_salaries_sorted)
    ans = None
    if 0 < N <= len(unique_salaries_sorted):
        ans = unique_salaries_sorted.iloc[N - 1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [ans] })
