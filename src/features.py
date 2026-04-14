import pandas as pd

def add_features(df):
    """Add composite competitive features to a Pokémon stats DataFrame."""
    df = df.copy()

    df['offense_score'] = df['attack'] + df['sp_atk']
    df['defense_score'] = df['defense'] + df['sp_def']
    df['bulk_score']    = df['hp'] + df['defense'] + df['sp_def']
    df['speed_tier']    = pd.qcut(df['speed'], q=4, labels=False, duplicates='drop')
    df['is_dual_type']  = (df['type2'].str.lower() != 'none').astype(int)

    return df
