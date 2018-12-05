import xuebadb.dbgeneric.db_interface as dbintfc
import xuebadb.dfanalysis.cleanup as cleanup
import xuebadb.dfanalysis.stats as stats
from testsuite import testsuite

# Testing out connectivity to a MySQL DB server using the package
res_con = dbintfc.DBInterface('mysql', 'cosc304.ok.ubc.ca', 'vbalaji', '10796456', 'WorksOn')
res_df = res_con.querySelect("select * from dept")
cleanup.show_nulls(res_df)
print(res_df)
print(stats.dfSummary(res_df))

# Testing out connectivity to a SQL server DB using the package
res_con = dbintfc.DBInterface('sql_server', 'sql04.ok.ubc.ca', 'rlawrenc', 'test', 'workson')
res_df = res_con.querySelect("select * from emp")
cleanup.show_nulls(res_df)
print(res_df)
stats.colBoxPlot(res_df)

# Running the xuebadb package test-suite
testsuite.testSuite()
