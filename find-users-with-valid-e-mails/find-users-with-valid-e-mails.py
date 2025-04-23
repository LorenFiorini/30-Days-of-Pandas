import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # df = users[users['mail'].str.endswith('@leetcode.com')]
    # print(df)
    def is_valid_mail(mail: str) -> bool:
        if not isinstance(mail, str):
            return 0
        if not mail.endswith('@leetcode.com'):
            return 0
        prefix = mail[: -len('@leetcode.com')]
        if not prefix or not prefix[0].isalpha():
            return False
        allowed = '_.-'
        for c in prefix:
            if not c.isalnum() and c not in allowed:
                return 0
        return 1
    users['is_valid_mail'] = users['mail'].apply(is_valid_mail)
    df = users[users['is_valid_mail'] == 1]
    return df[['user_id', 'name', 'mail' ]]
