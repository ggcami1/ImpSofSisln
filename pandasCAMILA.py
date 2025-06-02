import pandas as pd

df = pd.read_csv('listings.csv', index_col='id')

print(df.head())
print(df.tail(10))

print(df.describe(include='all'))

df.info()

print(df.columns)

if 'name' in df.columns:
    print(df['name'].head())

if {'name', 'neighbourhood_group'}.issubset(df.columns):
    print(df[['name', 'neighbourhood_group']].head())

if 'reviews_per_month' in df.columns and 'last_review' in df.columns:
    df2 = df[['reviews_per_month', 'last_review']].copy()
    df2['last_review'] = pd.to_datetime(df2['last_review'], errors='coerce')
    print(df2.head())