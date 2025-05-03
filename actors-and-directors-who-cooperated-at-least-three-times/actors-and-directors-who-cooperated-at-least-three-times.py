import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # ans = actor_director.groupby(['actor_id', 'director_id']).count()
    cooperation_counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperation_count')
    ans = cooperation_counts[ cooperation_counts['cooperation_count'] >= 3 ][ ['actor_id', 'director_id'] ]
    return ans