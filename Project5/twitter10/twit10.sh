#!/bin/bash
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file map_ten.py reduce_ten.py -mapper map_ten.py -reducer reduce_ten.py
