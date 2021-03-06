# data533_lab3_vaghul_jiachen
Submission repository for DATA-533 Lab 3

## Travis CI Status:

[![Build Status](https://travis-ci.org/vaghulb1992/data533_lab4_vaghul_jiachen.svg?branch=master)](https://travis-ci.org/vaghulb1992/data533_lab4_vaghul_jiachen)  

*Please note that becasue we are connecting to UBC's DB servers, Travis CI will not be able to connect to them as it runs from another server at a different location. Because of this, we had to comment out some of the assert statements in the unittests that try to create a connection object in MySQL and ODBC so that Travis CI would be able to run successfully. Otherwise, it will fail everytime.*

---

Group Members:
* Vaghul Aditya Balaji
* Jiachen Wei

***xuebadb*** is a python package that allows users to conveniently connect to and query from various database systems using a unified API. Currently, it supports connecting to *MySQL* and *SQL Server* database systems. The queries return Pandas dataframes which can then be cleaned up and analysed using one of the modules in the package.

---

**Requirements:**  
In order to be able to use the package, you would have to install the following:

Python packages:
* pyodbc
* mysql-connector
* pandas
* numpy
* missingno
* matplotlib

[ Microsoft ODBC Driver 17 ](https://docs.microsoft.com/en-us/sql/connect/python/python-driver-for-sql-server?view=sql-server-2017)

---

**Package structure:**

xuebadb --> package  
&nbsp;&nbsp;-- dbgeneric --> sub-package  
&nbsp;&nbsp;&nbsp;&nbsp;-- db_interface --> module   
&nbsp;&nbsp;&nbsp;&nbsp;-- mysql_interface -->module  
&nbsp;&nbsp;&nbsp;&nbsp;-- odbc_interface --> module  
&nbsp;&nbsp;-- dfanalysis --> sub-package  
&nbsp;&nbsp;&nbsp;&nbsp;-- cleanup --> module  
&nbsp;&nbsp;&nbsp;&nbsp;-- stats --> module  
     
Please use *DATA533_Lab2_Vaghul_Jiachen.py* to test out the package and to execute the test suite.

***NOTE:*** Since we are using UBC's databases for testing purposes, you would have to use the UBCO VPN if you are trying to run this code outside campus.
