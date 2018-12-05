import unittest

try:
    from unittests.teststats import TestStats
    from unittests.testodbc import TestODBC
    from unittests.testcleanup import TestCleanup
    from unittests.testmysql import TestMySQL
except ImportError:
    from .unittests.teststats import TestStats
    from .unittests.testodbc import TestODBC
    from .unittests.testcleanup import TestCleanup
    from .unittests.testmysql import TestMySQL

def testSuite():
    print("\n\n###################################################")
    print("EXECUTING XUEBADB TEST-SUITE")
    print("###################################################\n")
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestODBC))
    suite.addTest(unittest.makeSuite(TestStats))
    suite.addTest(unittest.makeSuite(TestCleanup))
    suite.addTest(unittest.makeSuite(TestMySQL))
    runner = unittest.TextTestRunner()
    print(f"\nRESULTS: [{runner.run(suite)}]")
    print("\n###################################################")
    print("###################################################")
