-- 1. Total number of records
SELECT COUNT(*) FROM tech_salaries;

-- 2. Average salary
SELECT ROUND(AVG(salary), 2) AS avg_salary FROM tech_salaries;

-- 3. Top 5 highest paying jobs
SELECT job, AVG(salary) AS avg_salary
FROM tech_salaries
GROUP BY job
ORDER BY avg_salary DESC
LIMIT 5;

-- 4. Salary distribution by employment type
SELECT employment_type, ROUND(AVG(salary)) AS avg_salary, COUNT(*) AS num_roles
FROM tech_salaries
GROUP BY employment_type
ORDER BY avg_salary DESC;

-- 5. Remote ratio and salary relationship
SELECT remote_ratio, ROUND(AVG(salary)) AS avg_salary
FROM tech_salaries
GROUP BY remote_ratio
ORDER BY remote_ratio DESC;

-- 6. Top locations with highest salaries
SELECT location, ROUND(AVG(salary)) AS avg_salary
FROM tech_salaries
GROUP BY location
ORDER BY avg_salary DESC
LIMIT 10;