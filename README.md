# Big_Data_Project

Project Description

In the phase 1 of our project, we have downloaded tweets from twitter and extracted urls and hashtags on the same. We have ran a python code to extracted the tweets from the out.json file and the extract hastags and urls. The extracted file is also uploaded in the repository as "input.txt"

Hadoop:

We ran wordcount program on hadoop on the extracted file "input.txt" and ran the command " bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.1.jar wordcount /Project_Phase_1/input_data.txt /Project_Phase_1/output_phase_1". The output file for the same has been stored in the repository " part-r-00000 "

The logs files that are generated are also uploaded to the repo with the name "hadoop_log_files "

Spark:


We ran wordcount program on spark on the extracted file and ran the command "$SPARK_HOME/bin/spark-submit run-example JavaWordCount /Project_Phase_1/input_data.txt >output_spark"and the ouput file for the same has been stored in the repository "output_spark"

The logs files that are generated are also uploaded to the repo with the name "spark_log_files"


Note: out.json which we have mentioned in the project description, we were unable to upload it.


