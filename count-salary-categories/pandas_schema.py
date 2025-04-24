# Schema definition
data = [[3, 108939],
    [2, 12747],
    [8, 87709],
    [6, 91796]
]
accounts = pd.DataFrame(
    data,
    columns=[
        'account_id',
        'income'
    ]
).astype(
    {
        'account_id':'Int64',
        'income':'Int64'
    }
)
