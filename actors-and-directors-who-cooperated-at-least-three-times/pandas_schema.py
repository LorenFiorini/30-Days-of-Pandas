# Schema definition
data = [
    [1, 1, 0],
    [1, 1, 1],
    [1, 1, 2],
    [1, 2, 3],
    [1, 2, 4],
    [2, 1, 5],
    [2, 1, 6]
]

actor_director = pd.DataFrame(
    data, 
    columns=[
        'actor_id',
        'director_id',
        'timestamp'
    ]
    ).astype({
        'actor_id':'int64',
        'director_id':'int64',
        'timestamp':'int64'
    }
    )