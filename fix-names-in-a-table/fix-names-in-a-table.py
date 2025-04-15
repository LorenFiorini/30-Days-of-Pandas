
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    print(users)
    users.sort_values(['user_id'], inplace=True)
    return users

