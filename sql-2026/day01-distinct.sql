SELECT DISTINCT
	[nome],
	[cognome]
FROM
	[dbo].[studente]

SELECT
	[cognome],
	COUNT(*)
FROM
	[dbo].[studente]
GROUP BY
	[cognome]