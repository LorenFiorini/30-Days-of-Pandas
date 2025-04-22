import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # ans['employee_id'] = employees['employee_id']
    # print(ans)
    # ans['bonus'] = employees[
    # ans = employees[
    #     (employees['employee_id'] % 2 == 1) &
    #     (employees['name'].str.startswith('M'))
    #     ]
    def compute_bonus(employee):
        # if employee['employee_id'] % 2 == 1 and employee['name'].str.startswith('M') == False:
        if employee['employee_id'] % 2 == 1 and employee['name'].startswith('M') == False:
            return employee['salary']
        return 0
    employees['bonus'] = employees.apply(compute_bonus, axis=1) 
    # axis=1 or axis=column or to go row by row
    # return employees[['employee_id', 'bonus']]
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')
