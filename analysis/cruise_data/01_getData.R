rm(list=ls())
library(ROracle)
# define sql file
sqlfile <- 'extractBioChemData.sql'
# read in sql file
sql <- scan(file = sqlfile, what = ls(), sep = '\n')
sql <- paste(sql, collapse = " ")
# define information to connect to database
username <- "GORDONC"
password <- "klSm9#ee"
host <- "VSNSBIOXP74.ENT.DFO-MPO.CA"
port <- 1521
sid <- "ptran"
## create an Oracle Database instance and create connection
drv <- dbDriver("Oracle")
## connect string specifications
connect.string <- paste(
  "(DESCRIPTION=",
  "(ADDRESS=(PROTOCOL=tcp)(HOST=", host, ")(PORT=", port, "))",
  "(CONNECT_DATA=(SID=", sid, ")))", sep = "")
## use username/password authentication
conn <- ROracle::dbConnect(drv, username=username, password=password, dbname = connect.string)
## run SQL statement by creating first a resultSet object
rs <- dbSendQuery(conn, sql)
# fetch records from the resultSet into a dataframe
data <- fetch(rs)
conn <- dbDisconnect(conn)
write.csv(data, paste0('data/', sub('\\.sql$', '', sqlfile), '.csv'))
