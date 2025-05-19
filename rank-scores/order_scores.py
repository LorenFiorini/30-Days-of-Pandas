
import pandas as pd

# Commented solution
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Step by step solution
    # 1. Sort the scores in descending order
    scores = scores.sort_values(by='score', ascending=False)
    # 2. Add a rank column
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    ''' Available methods:
    - 'average': average rank of tied values
    - 'min': lowest rank
    - 'max': highest rank
    - 'first': ranks assigned in order they appear
    - 'dense': same as 'min' but consecutive ranks
    '''
    # 3. Return the result
    return scores[['score', 'rank']]

# Test the function
scores = pd.read_csv('scores.csv')
print(order_scores(scores))
