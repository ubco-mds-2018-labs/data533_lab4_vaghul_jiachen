Package: *xuebadb*  
Sub-packages: *dbgeneric* and *dfanalysis*  

**Sub-package: `dbgeneric`**  
* Module: `odbc_interface` This module is responsible for connecting to and querying from a Microsoft SQL Server DB using the ODBC driver and pyodbc module. This module has a class ODBCInterface which contains the following methods:
  * `__init__` takes the server name, username, password and database name and stores it in class instance attributes
  * `__connect` is a private method that creates the connection using the class attributes which we stored in the constructor. It makes use of pyodbc module.
  * `select` takes the query that the user wants to run as a string and returns a [Pandas dataframe](https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.html) as the output.

* Module: `mysql_interface` This module is responsible for connecting to and querying from a MySQL DB. The module has a class MySQLInterface that contains the following methods:
  * `__init__` takes the server name, username, password and database name and stores it in class instance attributes.
  * `__connect` makes use of the mysql.connector module to create a connection object using the class attributes.
  * `select` takes the query and return the query result as a [Pandas dataframe](https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.html).
  
* Module: `db_interface` This module acts as an interface to various database system specific modules. This is module which the user should import for connecting to and running queries as it provides a layer of abstraction from the type of DB system. Currently, it imports `odbc_interface` and `mysql_interface` and contains the following methods:
  * `__init__` takes the db type, server name, username, password and database name and initializes the appropriate parent class based on the db type.  
  * `querySelect` takes the SQL `SELECT` query as input calls the appropriate parent class' `select` method to execute the query. It then returns a data frame with the rows.  
  
**Sub-package: `dfanalysis`**  
* Module: `cleanup` This module contains the following method to display the missing values:
  * `show_nulls` displays the data sparsity matrix to see missing values. It replaces "None" in the data frame with numpy NaN values, and displays the sparsity matrix using the missingno module.
  
* Module: `stats` This module contains the following methods to perform statistical analysis on the data frame:
  * `dfSummary` takes the data frame as input and returns a statistical summary (mean, min, max, etc.).
  * `colBoxPlot` takes the data frame as input and iterates through every column, identifies the columns with numerical data and displays box plots for them.  
