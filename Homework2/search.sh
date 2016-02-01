#!/bin/bash
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file smap.py sreduce.py -mapper smap.py -reducer sreduce.py
