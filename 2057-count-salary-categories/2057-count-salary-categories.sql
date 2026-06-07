-- CREATE TABLE cat (
--     category VARCHAR(50),
--     accounts_count INT
-- );

-- INSERT INTO cat (category, accounts_count)
-- VALUES
--     ('Low Salary', 0),
--     ('Average Salary', 0),
--     ('High Salary', 0);

-- SELECT * FROM cat;
-- This method won't work as it is creating new table

SELECT
    'Low Salary' AS category,
    COUNT(CASE WHEN income < 20000 THEN 1 END) AS accounts_count
FROM Accounts

UNION ALL

SELECT
    'Average Salary' AS category,
    COUNT(CASE WHEN income BETWEEN 20000 AND 50000 THEN 1 END) AS accounts_count
FROM Accounts

UNION ALL

SELECT
    'High Salary' AS category,
    COUNT(CASE WHEN income > 50000 THEN 1 END) AS accounts_count
FROM Accounts;
/*

SELECT
    'Low Salary' AS category,
    SUM(income < 20000) AS accounts_count
FROM Accounts

UNION ALL

SELECT
    'Average Salary',
    SUM(income BETWEEN 20000 AND 50000)
FROM Accounts

UNION ALL

SELECT
    'High Salary',
    SUM(income > 50000)
FROM Accounts;
*/