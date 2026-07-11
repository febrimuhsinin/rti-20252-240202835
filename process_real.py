import pandas as pd
import numpy as np
from scipy import stats

try:
    df = pd.read_csv('data form.csv/data form.csv')
except:
    print('error loading')
    exit()

# The columns are 1 to 10 for reguler, and 1 to 10 for food.
# Let's find the column indices.
# Reguler Q1 is column index 6 (0-indexed)
# Food Q1 is column index 16

def calc_sus(row, start_idx):
    score = 0
    for i in range(10):
        q_num = i + 1
        val = row.iloc[start_idx + i]
        if q_num % 2 != 0:
            score += (val - 1)
        else:
            score += (5 - val)
    return score * 2.5

df['Skor_Reguler'] = df.apply(lambda row: calc_sus(row, 6), axis=1)
df['Skor_Food'] = df.apply(lambda row: calc_sus(row, 16), axis=1)

mean_reguler = df['Skor_Reguler'].mean()
std_reguler = df['Skor_Reguler'].std()
mean_food = df['Skor_Food'].mean()
std_food = df['Skor_Food'].std()

print(f'Reguler: {mean_reguler:.2f} ± {std_reguler:.2f}')
print(f'Food: {mean_food:.2f} ± {std_food:.2f}')
