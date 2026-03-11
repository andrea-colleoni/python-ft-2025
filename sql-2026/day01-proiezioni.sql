USE [corso-sql]

SELECT    
	-- proiezione: impostazione le colonne del set di risultati
	[data_nascita],
	100 as Numero, 
	'Andrea' as NomePersona, 
	[nome] as NomeStudente,
	'bla bla bla..' as Messaggio,
	[nome] as NomeStudente2,
	10 + 20 as Calcolo,
	(10 - 30) / CAST(3 as float) as Espressione,
	UPPER([cognome])
FROM	
	studente
WHERE   
	-- criteri: espressioni che vengono valutate per record => restiuiscono True/False (uso gli oper. di confronto/logici)
	-- confronto: =, <>, >, <, >=, <=
	-- logici: AND, OR, NOT
	--([nome] = 'Andrea' OR [cognome] = 'Rossi')
	--AND [citta] = 'Milano'
	[citta] = '' OR 
	[citta] IS NULL -- NULL significa SCONOSCIUTO
	-- IS NOT => NON nullità
ORDER BY
	[nome], [data_nascita] desc