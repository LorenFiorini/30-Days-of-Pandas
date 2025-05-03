import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    def is_big_country(row):
        if row['area'] >= 3e6:
            return True
        if row['population'] >= 25e6:
            return True
        return False
    big_countries_series = world.apply(is_big_country, axis=1)
    print(big_countries_series)
    return world[big_countries_series][['name', 'area', 'population']]