import os
import sys
import unittest
import pandas as pd
import matplotlib

# to access xuebadb (in the parent repository)
parent_dir = os.path.normpath(os.path.join(os.getcwd(),'../..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
    
import xuebadb.dfanalysis.cleanup as cu

class TestCleanup(unittest.TestCase):  #creating a test class
    @classmethod
    def setUpClass(cls):
        print("Instantiating TestCleanup object")

    def setUp(self):
        # a test dataframe containing None values
        self.testdf=pd.DataFrame([ {1:'a',2:'b', 3:None}, {1:'d',2:None,3:'f'}])
        
    def test_Cleanup(self):  
        # test case
        # test if show_nulls() can handle an integer input
        self.assertEqual(cu.show_nulls(123), None)
        
        #test if show_nulls() can handle a string input
        self.assertEqual(cu.show_nulls('abc'),None)
        
        #test if show_nulls() can handle a list input
        self.assertEqual(cu.show_nulls([123,'abc']),None)
        
        #test if the None values are changed to NaN
        cu.show_nulls(self.testdf)
        for item in self.testdf:
            self.assertIsNot(item,None)
        
        #test if show_nulls() returns a matplotlib.axes.Axes object
        obj = cu.show_nulls(self.testdf)
        self.assertIsInstance(obj, matplotlib.axes.Axes)
        
    def tearDown(self):
        print("Finished testing the test case")
        
    @classmethod
    def tearDownClass(cls):
        print("Destroying TestCleanup object")
        