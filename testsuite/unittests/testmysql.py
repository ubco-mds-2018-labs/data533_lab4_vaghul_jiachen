import os
import sys
import unittest
import mysql.connector
import pandas as pd

# to access xuebadb (in the parent repository)
parent_dir = os.path.normpath(os.path.join(os.getcwd(),'../..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from xuebadb.dbgeneric.mysql_interface import MySQLInterface

class TestMySQL(unittest.TestCase):  #creating a test class
    @classmethod
    def setUpClass(cls):
        print("Instantiating TestMySQL object")
        
    def setUp(self):
        self.mysql_intfc = MySQLInterface('cosc304.ok.ubc.ca', 'jwei', '11154549', 'WorksOn')
        #creates a MySQLInterface object
        
    def test_MySQL(self):  # test case
        # Testing if able to connect to the MySQL server
        self.assertTrue( self.mysql_intfc._MySQLInterface__connect()) 
        #call the private method __connect() and it returns TRUE or FALSE
        
        #Testing if SELECT is functioning
        self.assertEqual(int(self.mysql_intfc.select("select 1234").values), 1234)
        #in SQL query, "SELECT anything" returns anything
        
        # Testing if the SELECT query returns a dataframe
        self.assertIsInstance(self.mysql_intfc.select("select * from emp"), pd.DataFrame)
       
        # Testing if select() throws a mysql.connector.errors.ProgrammingError for an invalid SELECT query
        self.assertRaises(mysql.connector.errors.ProgrammingError, self.mysql_intfc.select, "select * from fake_table")
        
        # Testing if the query result is correct
        correct = pd.DataFrame(pd.Series( ['D1', 'Management', 'E8'], index=[0,1,2]),columns=[0])
        correct = correct.T
        res_df = self.mysql_intfc.select("select * from dept where dno='D1'")
        self.assertTrue(correct.equals(res_df))
        
    def tearDown(self):
        print("Finished testing the test case.")
        
    @classmethod
    def tearDownClass(cls):
        print("Destroying TestMySQL object")
        