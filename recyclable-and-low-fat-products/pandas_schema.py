# Schema definition
data = [
    ['0', 'Y', 'N'],
    ['1', 'Y', 'Y'],
    ['2', 'N', 'Y'],
    ['3', 'Y', 'Y'],
    ['4', 'N', 'N']
]
products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype({'product_id':'int64', 'low_fats':'category', 'recyclable':'category'})