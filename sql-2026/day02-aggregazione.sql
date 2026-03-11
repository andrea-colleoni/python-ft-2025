-- funzioni di aggregazione

select
	count(*),
	sum([altezza_cm]),
	avg([altezza_cm]),
	min([altezza_cm]),
	min([data_nascita]),
	min([nome]),
	max([nome]),
	[citta]
from 
	[dbo].[studente]
group by
	[citta]

select
	Count(*),
	[nome]--,[citta]
from
	[dbo].[studente]
group by [nome]--, [citta]