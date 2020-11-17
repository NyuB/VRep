head -50 ../data/purchases.txt | mapper.py | sort | reducer.py

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1- cdh5.5.0.jar –mapper mapper.py –reducer reducer.py –file mapper.py –file reducer.py –input myinput –output joboutput