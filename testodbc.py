import unittest
import pandas as pd

from xuebadb.dbgeneric.odbc_interface import ODBCInterface
    
class TestODBC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Instantiating TestODBC object")
        
    def setUp(self):
        self.odbc_intfc = ODBCInterface('sql04.ok.ubc.ca', 'rlawrenc', 'test', 'workson')
        self.bad_odbc_intfc = ODBCInterface('sql04.ok.ubc.ca', 'bad', 'password', 'workson')
        print("Instantiating test ODBC-interface object")
        
    def testODBC(self):
        # Testing if successfully able to connect to the ODBC DB server
        self.assertTrue(self.odbc_intfc._ODBCInterface__connect())
        
        # Testing if the SELECT query returns the correct result
        self.assertEqual(int(self.odbc_intfc.select("select 1234").values), 1234)
        
        # Testing if the SELECT query returns a dataframe
        self.assertIsInstance(self.odbc_intfc.select("select * from emp"), pd.DataFrame)
        
        # Testing if the select method throws a pyodbc.ProgrammingError for an incorrect SELECT query
        self.assertFalse(self.odbc_intfc.select("select * from dummy_table"))
        
        # Testing if the select method throws a pyodbc.Error for an empty query
        self.assertFalse(self.odbc_intfc.select( ""))
        
        # Testing if the connection is fine
        self.assertEqual(self.bad_odbc_intfc.select("select * from emp"), None)
    
    def tearDown(self):
        del(self.odbc_intfc)
        print("Destroyed test ODBC-interface object")
        
    @classmethod
    def tearDownClass(cls):
        print("Destroying TestODBC object")
        
unittest.main()        
