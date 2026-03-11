SELECT [BusinessEntityID] A
      ,[LoginID] B
      ,[JobTitle] C
      ,[BirthDate] D
      ,CASE [MaritalStatus]
        WHEN 'S' THEN 'Single'
        WHEN 'M' THEN 'Married'
        ELSE 'Unknown'
       END StatoCivile
      ,CASE [Gender]
        WHEN 'F' THEN 'Female'
        WHEN 'M' THEN 'Male'
        ELSE 'Unknown'
       END
      ,[HireDate]
      ,[SalariedFlag]
      ,[VacationHours]
      ,[SickLeaveHours]
      ,[CurrentFlag]
      ,[rowguid]
      ,[ModifiedDate]
  FROM [HumanResources].[Employee]

GO

