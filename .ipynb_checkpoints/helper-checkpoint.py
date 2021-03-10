import pandas as pd

def join_df(left, right, left_on, right_on=None):
    if right_on is None: right_on = left_on
    return left.merge(right, how='left', left_on=left_on, right_on=right_on, suffixes=("", "_y"))

def get_missing_columns(df):
    return list(df.columns[df.describe(include = 'all').loc['count']<len(df)])

