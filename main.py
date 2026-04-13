import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# 1. SECURITY 
load_dotenv()
db_pass = os.getenv('DB_PASSWORD')
db_url = f'postgresql://postgres:{db_pass}@localhost:5432/vault_production'

# 2. EXTRACT (raw data)
df = pd.read_csv('vault.csv')

# 3. TRANSFORM (categorize items)
def categorize_item(item):
    if 'Gold' in item or 'Diamond' in item: return 'Fine Jewelry'
    if 'Watch' in item or 'Rolex' in item: return 'Luxury Timepieces'
    return 'General'

df['category'] = df['item_type'].apply(categorize_item)


# 4. LOAD (ending to postgresql)
engine = create_engine(db_url)

# This sends the data to a table name in my DBeaver
df.to_sql('vault_sales', engine, if_exists='replace', index=False)

print("Pure Element raw data record is now in PostgreSQL")

