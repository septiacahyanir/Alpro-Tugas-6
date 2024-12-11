import pandas as pd

#membaca file students.csv
df = pd.read_csv('students.csv')
print('data :')
print(df)

#menampilkan 5 baris
print('\n5 Baris Pertama')
print(df.head())

#menampilkan informasi
df.info()
print(df.describe())

#membuat kolom baru "status"
df['Status']=['Lulus' if grade >= 80 else 'Tidak Lulus' for grade in df['Grade']]
print(df)

#menyimpan file baru
df.to_csv('students_processed.csv', index=False)

#rata rata
rata_rata_grade = df['Grade'].mean()
print(f"Rata rata nilai alpro mahasiswa : {rata_rata_grade}")

kelompok = df.groupby('Status').size()
print(kelompok)