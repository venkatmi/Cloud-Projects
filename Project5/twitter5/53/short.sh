#!/bin/bash

hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file shortmap.py shortreduce.py -mapper shortmap.py -reducer shortreduce.py
