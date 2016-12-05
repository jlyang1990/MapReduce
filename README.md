# Command Lines for Hadoop and MapReduce
## List directory contents in \<HDFS directory\>
`hadoop fs -ls <HDFS directory>`
## Create new directory named \<HDFS directory\>
`hadoop fs -mkdir <HDFS directory>`
## Delete directory named \<HDFS directory\>
`hadoop fs -rm -r <HDFS directory>`
## Input data into HDFS
`hadoop fs -input <local directory of input> <HDFS directory>`
## Run MapReduce job
`hs <local directory of mapper.py> <local directory of reducer.py> <HDFS directory of input> <HDFS directory>`

`hsc <local directory of mapper.py> <local directory of reducer.py> <HDFS directory of input> <HDFS directory>`

`hs` and `hsc` are aliases defined in [*bashrc*](https://github.com/jlyang1990/MapReduce/blob/master/bashrc), where "combiner" is added in `hsc`.
## Retrieve output from HDFS
`hadoop fs -get <HDFS directory of output> <local directory of output>`
## Example
`hadoop fs -mkdir input`

`hadoop fs -input data/purchases.txt input`

`hadoop fs -ls input`

`hadoop fs -mkdir output`

`hs code/mapper.py code/reducer.py input/purchases.txt output`

`hadoop fs -ls output`

`hadoop fs -get output/part-00000 result/summary.txt`
# Quick check MapReduce code on a small dataset on local machine
`cat small_dataset.csv | python mapper.py | sort | python reducer.py`
