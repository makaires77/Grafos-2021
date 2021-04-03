import collections
import itertools
import math

Point = collections.namedtuple('Point', ['id', 'x', 'y'])
Distance = collections.namedtuple('Distance', ['id1', 'id2', 'distance'])

def get_distance(p1, p2, distances):
    for d in distances:
        if d.id1 == p1 and d.id2 == p2:
            return d.distance

    return 0

def get_route_length(route_pairs, distances):
    dst = 0
    
    for pair in route_pairs:
        dst += get_distance(pair[0], pair[1], distances)

    return dst

def calc_distance_between_points(points):
    distances = []

    combs = itertools.combinations(range(len(points)), 2)
    for c in combs:
        id1 = points[c[0]].id
        x1 = points[c[0]].x
        y1 = points[c[0]].y

        id2 = points[c[1]].id
        x2 = points[c[1]].x
        y2 = points[c[1]].y

        dst = math.sqrt(pow((y2 - y1), 2) + pow((x2 - x1), 2))
        distance = Distance(id1, id2, dst)

        distances.append(distance)

    return distances

def calc_shortest_route(num_points, distances):

        perms = itertools.permutations(range(num_points))
        distance_ids = []
        
        for val in perms:
            dst_ids = []
            for v in val:
                id = "p" + str(v+1)
                dst_ids.append(id)
                
            dst_ids.append("P" + str(val[0]+1))
            distance_ids.append(dst_ids)

        shortest_route_length = 0
        shortest_route = []

        for route in distance_ids:
            route_pairs = []
            
            for idx in range(len(route)-1):
                sorted_pair = [route[idx], route[idx+1]]
                sorted_pair.sort()
                route_pairs.append(sorted_pair)

            dst = get_route_length(route_pairs, distances)

            if shortest_route_length == 0:
                shortest_route_length = dst
                shortest_route = route

            if dst < shortest_route_length:
                shortest_route_length = dst
                shortest_route = route

        print("shortest_route_length: %.2f" % shortest_route_length)

        res = { 'route': shortest_route[:len(shortest_route) - 1], 'length': "%.2f" % shortest_route_length }

        return res