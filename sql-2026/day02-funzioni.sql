-- funzoni scalari

-- https://learn.microsoft.com/en-us/sql/t-sql/language-reference?view=sql-server-ver17
-- https://it.wikipedia.org/wiki/ISO_8601
-- https://regex101.com/

select
	CONCAT(TRIM([cognome]), ' ', TRIM([nome])),
	CONCAT(TRIM([cognome]), ' ', LEFT(TRIM([nome]), 1) + '.'),
	[nome],
	[cognome],
	[altezza_cm] / 100, -- divisione tra 2 interi => risultato interi
	CAST([altezza_cm] as float) / 100, -- se c'è almeno un float/double/decimal/money => risultato decimal
	DAY([data_nascita]),
	MONTH([data_nascita]),
	YEAR([data_nascita]),
	GETDATE(),
	DATEADD(MONTH, 1, '2026-02-28T00:00:00'),
	DATEADD(DAY, -(DAY('2026-02-28T00:00:00')), DATEADD(MONTH, 2, '2026-02-28T00:00:00')),
	UPPER([nome]),
	LOWER([cognome])
from
	[dbo].[studente]