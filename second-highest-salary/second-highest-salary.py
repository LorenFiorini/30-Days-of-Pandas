import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].unique()
    print(unique_salaries)
    # print(type(unique_salaries))
    np.sort(unique_salaries)
    unique_salaries[::-1].sort()
    # unique_salaries.flip()
    print(unique_salaries)
    if len(unique_salaries) < 2:
        return pd.DataFrame(
            {
                'SecondHighestSalary':[None]
            }
        )

    return pd.DataFrame(
        {
            'SecondHighestSalary': [unique_salaries[1]]
        }
    )