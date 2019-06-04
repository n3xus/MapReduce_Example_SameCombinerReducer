#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: ./tag_driver.sh [input_location] [output_location]"
    exit  1
fi

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-D mapreduce.job.reduces=3 \
-D mapreduce.job.name='Tag owner inverted list' \
-file category_mapper.py \
-mapper category_mapper.py \
-file category_reducer.py \
-reducer category_reducer.py \
-combiner category_reducer.py \
-input $1 \
-output $2
