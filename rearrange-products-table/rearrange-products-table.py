import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    melted = products.melt(
        id_vars=['product_id']
    )
    # print(melted)
    ans = melted.dropna()
    ans.rename(
        columns={
            'variable':'store',
            'value':'price'
        },
        inplace=True
    )
    return ans