-- Total cases by country
SELECT 
    country,
    MAX(total_cases) AS highest_cases
FROM covid_cleaned
GROUP BY country
ORDER BY highest_cases DESC;

-- Total deaths by country
SELECT 
    country,
    MAX(total_deaths) AS highest_deaths
FROM covid_cleaned
GROUP BY country
ORDER BY highest_deaths DESC;

-- Death rate
SELECT 
    country,
    MAX(total_deaths) * 100.0 / MAX(total_cases) AS death_rate
FROM covid_cleaned
GROUP BY country
ORDER BY death_rate DESC;

-- Global daily cases
SELECT 
    date,
    SUM(total_cases) AS global_cases
FROM covid_cleaned
GROUP BY date
ORDER BY date;