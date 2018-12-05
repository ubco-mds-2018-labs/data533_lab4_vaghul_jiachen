import os
import sys
import unittest
import pandas as pd

parent_dir = os.path.normpath(os.path.join(os.getcwd(), '../..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
    
import xuebadb.dfanalysis.stats as stats
    
class TestStats(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Instantiating TestStats object")
        
    def setUp(self):
        self.df = pd.DataFrame([[10, 20], [30, 40]], index = ['row1', 'row2'])
        print("Instantiating test dataframe object")
        
    def testStats(self):
        # Testing if the dfSummary method returns a dataframe
        self.assertIsInstance(stats.dfSummary(self.df), pd.DataFrame)
        
        # Testing if the dataframe returned by dfSummary conains 8 rows
        self.assertEqual(len(stats.dfSummary(self.df)), 8)
        
        # Testing if the 'max' row in '0' column has value 30
        self.assertEqual(stats.dfSummary(self.df).loc['max', 0], 30)
        
        # Testing if the colBoxPlot method fails to plot from non-numeric data
        self.assertFalse(stats.colBoxPlot(pd.DataFrame(['a', 'b'])))
        
        # Testing if the colBoxPlot method successfully plots from numeric data
        self.assertTrue(stats.colBoxPlot(self.df))      
    
    def tearDown(self):
        del(self.df)
        print("Destroyed test dataframe object")
        
    @classmethod
    def tearDownClass(cls):
        print("Destroying TestStats object")
