
Create Table Books(BookId char(5) Primary Key check(BookId Like 'B[0-9][0-9][0-9][0-9]'),
BookName varchar(40) Not Null, AuthorName varchar(40) , Price SmallInt check( Price >0),
Publish_Date DateTime, Publisher_Name varchar(40) Not Null,category varchar(25) , 
BookLanguage varchar(20))
select * from books;