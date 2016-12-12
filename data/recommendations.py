from pyspark import SparkContext
from itertools import combinations

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)

distinct_lines = data.distinct()

pairs = distinct_lines.map(lambda line: line.split())
views = pairs.groupByKey()
view_pairs = views.flatMap(lambda user_items: [(user_items[0], pair) for pair in combinations(user_items[1], 2)])
inverted_view_pairs = view_pairs.map(lambda kv: (tuple(sorted(kv[1])), 1))
counts = inverted_view_pairs.reduceByKey(lambda a, b: a + b)
filtered_counts = counts.filter(lambda kv: kv[1] >= 3)

output = filtered_counts.collect()
print("=============================================================")
for pair, count in output:
    print("co-view: {}; count: {}".format(pair, count))
print("=============================================================")

sc.stop()
