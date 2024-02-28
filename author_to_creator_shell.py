import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('Post-2024-02-19.csv')


# Her bir satır için işlemi gerçekleştir
for index, row in df.iterrows():
    creator_name = row['creator']
    
    # Eğer 'author' alanı boşsa, 'creator' değeriyle doldur
    if pd.isna(row['author']):
        df.at[index, 'author'] = creator_name

# CSV dosyasını güncelle
df.to_csv('Post-2024-02-19.csv', index=False)
