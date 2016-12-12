from pyspark import SparkContext
from itertools import combinations

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)

pairs = data.map(lambda line: line.split())
views = pairs.groupByKey()
view_pairs = views.map(lambda user_items: (user_items[0], list(combinations(user_items[1], 2))))
inverted_view_pairs = view_pairs.map(lambda kv: (tuple(kv[1]), kv[0]))
view_pair_users = inverted_view_pairs.groupByKey()
view_pair_counts = view_pair_users.map(lambda users: len(users))
filtered_view_pair_counts = view_pair_counts.filter(lambda count: count >= 3)

output = filtered_view_pair_counts.collect()
print("=============================================================")
for item_id, count in output:
    print ("item_id %s count %d" % (item_id, count))
print("=============================================================")

sc.stop()
