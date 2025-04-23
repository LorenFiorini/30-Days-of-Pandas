import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    def has_diabetes_i(a: str) -> bool:
        print(a)
        ls = a.split(' ')
        for w in ls:
            if w.startswith('DIAB1'):
                return True
        return False
    # patients['has DIAB1'] = patients['conditions'].apply(has_diabetes_i)
    has_diabetes_i_series = patients['conditions'].apply(has_diabetes_i)
    return patients[has_diabetes_i_series][['patient_id', 'patient_name', 'conditions']]
