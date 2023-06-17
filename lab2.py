import math
import random


def dist(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def connect(cluster1, cluster2):
    min_dist = float('inf')
    for point1 in cluster1:
        for point2 in cluster2:
            d = dist(point1, point2)
            if d < min_dist:
                min_dist = d
    return min_dist

def ierrarh(x):
    distances = [[dist(x[i], x[j]) for j in range(len(x))] for i in range(len(x))]
    clusters = [[i] for i in range(len(x))]
    print(clusters)
    history = [list(clusters)]
    
    while len(clusters) > 1:
        min_dist = float('inf')
        union = None
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                d = connect([x[k] for k in clusters[i]], [x[k] for k in clusters[j]])
                if d < min_dist:
                    min_dist = d
                    union = (i, j)
        
        new_cluster = clusters[union[0]] + clusters[union[1]]
        clusters.pop(union[1])
        clusters[union[0]] = new_cluster
        history.append(list(clusters))
    
    return clusters, history

#def print_dendrogram(clusters, level=0):
    

x = []
for i in range(15):
    fillx = [random.randint(-10, 10) for j in range(2)]
    x.append(fillx)
print(x)

clusters, history = ierrarh(x)

for i in range(len(history)):
    print(f"Итерация {i+1}:")
    j = 1
    for cluster in history[i]:
        print(f"Кластер {j}: {[x[k] for k in cluster]}")
        j += 1
    print("\n")

for i in range(len(clusters)):
    cluster = clusters[i]
    print(f"Кластер {i+1}: {[x[k] for k in cluster]}")