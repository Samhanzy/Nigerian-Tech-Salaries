import pandas as pd
import psycopg2

DATABASE_URL = "postgresql://nigerian_tech_salaries_db_user:b1d07OK7m0u1oMDGLL9umEI36cIH2ihh@dpg-d1lo69ili9vc73e7kmf0-a.frankfurt-postgres.render.com/nigerian_tech_salaries_db"

df = pd.read_csv("tech_salaries.csv")

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS tech_salaries (
    id SERIAL PRIMARY KEY,
    job VARCHAR(100),
    salary INTEGER,
    remote_ratio INTEGER,
    years_experience REAL
)
""")

for _, row in df.iterrows():
    cur.execute(
        "INSERT INTO tech_salaries (job, salary, remote_ratio, years_experience) VALUES (%s, %s, %s, %s)",
        (row['job'], int(row['salary']), int(row['remote_ratio']), float(row['years_experience']))
    )

conn.commit()
cur.close()
conn.close()

print("✅ Upload complete.")
