import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame: 
    red_company = company[company['name'] == 'RED']
    # print(red_company)
    ans = pd.DataFrame(columns=['name'])
    if red_company.empty:
        return sales_person[['name']]
        # return ans
    red_com_id = red_company['com_id'].iloc[0]
    sales_with_red_orders = orders[orders['com_id'] == red_com_id]['sales_id'].unique()
    salespeople_without_red_orders = sales_person[~sales_person['sales_id'].isin(sales_with_red_orders)]
    return salespeople_without_red_orders[['name']]
