\copy tech_salaries(company, job, salary, years_experience, remote_ratio, employment_type, location)
FROM 'data/tech_salaries.csv'
DELIMITER ','
CSV HEADER;