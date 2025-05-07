import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    def low_fat_recyclable(row):
        if row['low_fats'] == 'Y' and row['recyclable'] == 'Y':
            return True
        return False
    ans = products.apply(low_fat_recyclable, axis = 1)
    return products[ans][['product_id']]