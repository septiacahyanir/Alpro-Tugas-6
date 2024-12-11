import pandas as pd

df = pd.read_csv('data.csv')
print('data :')
print(df)

print('\nBaris Pertama')
print(df.head())

df.info()

df['nilai_uas']=df['nilai_alpro']*0.4
print(df)

rata_rata_alpro = df['nilai_alpro'].mean()
print(f"Rata rata nilai alpro mahasiswa : {rata_rata_alpro}")

kelompok = df.groupby('nilai_alpro').size()
print(kelompok)


