CREATE TABLE tech_salaries (
    id SERIAL PRIMARY KEY,
    company VARCHAR(100),
    job VARCHAR(100),
    salary INTEGER,
    years_experience NUMERIC,
    remote_ratio INTEGER,
    employment_type VARCHAR(20),
    location VARCHAR(100)
);