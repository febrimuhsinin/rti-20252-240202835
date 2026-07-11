import pandas as pd
import numpy as np

df = pd.read_csv('data form.csv/data form.csv')

def calc_sus_reguler(row):
    score = 0
    for i in range(10):
        q_num = i + 1
        val = row.iloc[6 + i]
        if q_num % 2 != 0:
            score += (val - 1)
        else:
            score += (5 - val)
    return score * 2.5

def calc_sus_food(row):
    score = 0
    # Q1 (Odd)
    score += (row.iloc[16] - 1)
    # Q2 is MISSING, impute as 3 (neutral -> 5-3 = 2)
    score += 2
    # Q3 (Odd)
    score += (row.iloc[17] - 1)
    # Q4 (Even)
    score += (5 - row.iloc[18])
    # Q5 (Odd)
    score += (row.iloc[19] - 1)
    # Q6 (Even)
    score += (5 - row.iloc[20])
    # Q7 (Odd)
    score += (row.iloc[21] - 1)
    # Q8 (Even)
    score += (5 - row.iloc[22])
    # Q9 (Odd)
    score += (row.iloc[23] - 1)
    # Q10 (Even)
    score += (5 - row.iloc[24])
    return score * 2.5

df['Skor_Reguler'] = df.apply(calc_sus_reguler, axis=1)
df['Skor_Food'] = df.apply(calc_sus_food, axis=1)

print(f"Reguler: {df['Skor_Reguler'].mean():.2f} ± {df['Skor_Reguler'].std():.2f}")
print(f"Food: {df['Skor_Food'].mean():.2f} ± {df['Skor_Food'].std():.2f}")
