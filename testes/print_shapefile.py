# import tensorflow as tf 
# print('tensorflow version', tf.__version__)
# x = [[3.]]
# y = [[4.]]
# print('Result: {}'.format(tf.matmul(x, y)))

import shapefile

# with shapefile.Reader("entradas/estados_2010.shp") as shp:
#     print(shp)

sf = shapefile.Reader("entradas/estados_2010.shp")
shapes  = sf.shapes()
records = sf.shapeRecords()
list(records)

vizinhos=[]
c=1
for r in shapes:
    bbox = set(r.bbox)
    vizinhos.append((c, bbox))
    c+=1
    
print(vizinhos)

# def box_intersections(set1, set2):
#     set1 = tf.expand_dims(set1, axis=-1)
#     x_min = tf.math.maximum(set1[:, 0], set2[:, 0])
#     y_min = tf.math.maximum(set1[:, 1], set2[:, 1])
#     x_max = tf.math.minimum(set1[:, 2], set2[:, 2])
#     y_max = tf.math.minimum(set1[:, 3], set2[:, 3])
#     dx = tf.math.maximum(x_max - x_min, 0)
#     dy = tf.math.maximum(y_max - y_min, 0)
#     return dx * dy

# import tsp

# points = []
# points.append(tsp.Point('p1', 40, 30))
# points.append(tsp.Point('p2', 140, 80))
# points.append(tsp.Point('p3', 20, 35))
# points.append(tsp.Point('p4', 200, 135))

# distances = tsp.calc_distance_between_points(points)
# print(distances)
# print()

# tsp.calc_shortest_route(len(points), distances)