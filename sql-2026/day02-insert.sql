-- DML manipolazione dati
-- INSERT, UPDATE, DELETE

-- INSERT => VALUES
INSERT INTO [dbo].[studente]
           (
           [nome]
           ,[cognome]
           ,[data_nascita]
           ,[citta]
           ,[altezza_cm]
           --,[campo_json]
           --,[codice_corso]
           --,[lingua_corso]
           )
     VALUES
           (
           'Greta'
           ,'Rossi'
           ,'2002-05-28'
           ,'Firenze'
           ,165
           --,NULL
           --,NULL
           --,NULL
           )
           
           
-- SELECT INTO (crea tabella nuova)

select
	s.*,
	c.*
INTO NuovaTabella  -- Questa è la tabella NUOVA dove salvare i dati della query
from
	[dbo].[studente] s INNER JOIN [dbo].[corso] c
	--[dbo].[studente] s LEFT OUTER JOIN	[dbo].[corso] c
	--[dbo].[studente] s RIGHT OUTER JOIN	[dbo].[corso] c
	--[dbo].[studente] s FULL OUTER JOIN	[dbo].[corso] c
	ON s.codice_corso = c.codice AND s.lingua_corso = c.lingua
	--INNER JOIN ....
--where
--	s.id is null


-- INSERT => SELECT

INSERT INTO [dbo].[StudentiPuliti]
        (
        [nome]
        ,[cognome]
        ,[data_nascita]
        ,[citta]
        ,[altezza_cm]
        --,[campo_json]
        --,[codice_corso]
        --,[lingua_corso]
        )
    SELECT 
        'Nome',
        'Cognome',
        GETDATE(),
        'Non lo so',
        100
    FROM
        studente

-- 

