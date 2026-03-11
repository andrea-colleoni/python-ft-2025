-- JOIN

select
	s.*,
	c.*
from
	[dbo].[studente] s INNER JOIN [dbo].[corso] c
	--[dbo].[studente] s LEFT OUTER JOIN	[dbo].[corso] c
	--[dbo].[studente] s RIGHT OUTER JOIN	[dbo].[corso] c
	--[dbo].[studente] s FULL OUTER JOIN	[dbo].[corso] c
	ON s.codice_corso = c.codice AND s.lingua_corso = c.lingua
	--INNER JOIN ....
--where
--	s.id is null
