# Schema definition
data = [
    [0, 95, 100, 105],
    [1, 70, None, 80]
]
products = pd.DataFrame(
    data, 
    columns=['product_id', 'store1', 'store2', 'store3']
).astype(
    {
        'product_id':'Int64',
        'store1':'Int64',
        'store2':'Int64',
        'store3':'Int64'
    }
)