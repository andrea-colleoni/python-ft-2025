
CREATE TABLE [dbo].[WorldsLargestSQL](
	[Rank] [tinyint] NOT NULL,
	[City] [nvarchar](50) NOT NULL,
	[Country] [nvarchar](50) NOT NULL,
	[Population_Est] [int] NOT NULL,
	[Area_sq_km] [smallint] NOT NULL
) ON [PRIMARY]

-- https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver17

BULK INSERT WorldsLargestSQL -- nome tabella
FROM 'C:\Work\Corsi\PythonIPSOS\Sql2026\Top 100 Worlds Largest Cities.csv'
WITH(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n'
)