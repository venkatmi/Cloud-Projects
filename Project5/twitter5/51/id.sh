#!/bin/bash
#hadoop fs -rmr /user/zhuxt/output
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file map.py reduce.py -mapper map.py -reducer reduce.py
