import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

st.set_page_config(page_title="🇳🇬 Nigerian Tech Salaries", layout="wide")
st.title("📊 Nigerian Tech Salaries Dashboard")

@st.cache_data
def load_data():
    conn = psycopg2.connect(
        host="localhost",
        database="tech_salaries_db",
        user="postgres",
        password="Samhanzy2002",
        port=5432
    )
    df = pd.read_sql("SELECT * FROM tech_salaries", conn)
    conn.close()
    return df

df = load_data()

df["remote_ratio"] = df["remote_ratio"].astype(str)

avg_salary_remote = df.groupby("remote_ratio", as_index=False)["salary"].mean()
fig1 = px.bar(avg_salary_remote, x="remote_ratio", y="salary", title="💰 Average Salary by Remote Ratio", color="remote_ratio")

remote_count = df["remote_ratio"].value_counts().reset_index()
remote_count.columns = ["remote_ratio", "count"]
fig2 = px.bar(remote_count, x="remote_ratio", y="count", title="📈 Job Count by Remote Ratio", color="remote_ratio")

avg_salary_job = df.groupby("job", as_index=False)["salary"].mean().sort_values(by="salary", ascending=False)
fig3 = px.bar(avg_salary_job.head(15), x="salary", y="job", orientation="h", title="💼 Top 15 Average Salaries by Job Title", color="salary")

fig4 = px.scatter(df, x="years_experience", y="salary", color="remote_ratio", title="📉 Salary vs. Years of Experience")

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.plotly_chart(fig2, use_container_width=True)

st.plotly_chart(fig3, use_container_width=True)
st.plotly_chart(fig4, use_container_width=True)
