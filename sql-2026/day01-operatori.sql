/*
NULL => SCONOSCIUTO

NULL = NULL => NO!
NULL <> NULL => NO!
*/
SELECT
	*
FROM
	[dbo].[studente]
WHERE
	[citta] IS NULL

-- operatore IN
SELECT
	*
FROM
	[dbo].[studente]
WHERE
	[citta] IN ('Milano', 'Bergamo', 'Brescia', 'Torino')
	-- citta = 'Milano' OR citta = 'Bergamo' OR citta = '....

-- operatore BETWEEN
SELECT
	*
FROM
	[dbo].[studente]
WHERE 
	[data_nascita] BETWEEN '2015-01-01' AND '2020-12-31' -- estremi compresi
	-- [data_nascita] >= '2015-01-01' AND [data_nascita] <= '2020-12-31'

-- operatore LIKE (uso delle wildcards: % e _) => case insensitive
SELECT
	*
FROM
	[dbo].[studente]
WHERE 
	--[cognome] LIKE 'G%a%'
	--[nome] LIKE '%i%'
	--[nome] LIKE 'A_____'
	[nome] LIKE 'Anna'

-- 
SELECT
	*
FROM
	[dbo].[studente]
WHERE 
	DAY([data_nascita]) = 9