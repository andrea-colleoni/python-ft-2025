-- nested query
SELECT [ProductID]
      ,[Name]
      ,[ProductNumber]
      ,[SafetyStockLevel]
      ,[ReorderPoint]
      ,[ReorderPoint] - (
          SELECT AVG([ReorderPoint])
          FROM [Production].[Product]
        ) Differenza
      ,[StandardCost]
      ,[ListPrice]
      ,[DaysToManufacture]
      ,[SellStartDate]
  FROM 
    ( SELECT *  FROM [Production].[Product] WHERE Name LIKE 'A%') ProdottiConLaA
  WHERE [ReorderPoint] > (
      SELECT AVG([ReorderPoint])
      FROM [Production].[Product]
  )