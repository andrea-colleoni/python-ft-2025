create procedure CalcolaRiordini as

declare @limiteRiordino int

-- set @limiteRiordino = 500

select @limiteRiordino = MIN([ReorderPoint])
FROM [Production].[Product]
WHERE Name LIKE 'P%'

SELECT [ProductID]
      ,[Name]
      ,[ProductNumber]
      ,[SafetyStockLevel]
      ,[ReorderPoint]
      ,[ReorderPoint] 
      , ReorderPoint - @limiteRiordino Differenza
      ,[StandardCost]
      ,[ListPrice]
      ,[DaysToManufacture]
      ,[SellStartDate]
      , @limiteRiordino * 10 / 3 Calcolo
  FROM [Production].[Product] 
  where ReorderPoint <= @limiteRiordino