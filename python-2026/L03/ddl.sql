CREATE TABLE Passeggeri
(
    PassengerId int NOT NULL,
    Survived bit NOT NULL,
    Name varchar(100) NOT NULL
) 

ALTER TABLE Passeggeri ADD CONSTRAINT
PK_Passeggeri PRIMARY KEY CLUSTERED 
(
    PassengerId
)