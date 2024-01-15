import heapq

class Node:
    def _init_(self, position, parent=None, cost=0, heuristic=0):
        self.position = position
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def _lt_(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def calculate_heuristic(current, target):
    return abs(target[0] - current[0]) + abs(target[1] - current[1])

def get_neighbors(node):
    x, y = node.position
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < 4 and 0 <= ny < 4]

def astar(start, target, obstacles):
    open_set = [Node(start, None, 0, calculate_heuristic(start, target))]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.position == target:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.position)

        for neighbor_pos in get_neighbors(current_node):
            if neighbor_pos in obstacles or neighbor_pos in closed_set:
                continue

            neighbor = Node(neighbor_pos, current_node,
                            current_node.cost + 1, calculate_heuristic(neighbor_pos, target))

            if neighbor not in open_set:
                heapq.heappush(open_set, neighbor)

    return None  # No path found

def generate_coordinate_list(target1, target2, target3):
    coordinate_list = []
    
    obstacle1 = [target2,target3]
    
    path1 = astar((0, 0), target1, obstacle1)
    
    coordinate_list.extend(path1[1:])
    coordinate_list.append(path1[-2])
    
    obstacle2 = [target1, target3]
    path2 = astar((path1[-2]), target2, obstacle2)

    coordinate_list.extend(path2[1:])
    coordinate_list.append(path2[-2])
    
    obstacle3 = [target1, target2]
    path3 = astar((path2[-2]), target3, obstacle3)

    coordinate_list.extend(path3[1:])
    coordinate_list.append(path3[-2])
    
    obstacle4 = [target1, target2, target3]
    path4 = astar((path3[-2]), (0,0), obstacle4)
    
    coordinate_list.extend(path4[1:])
    
    return coordinate_list
    
if _name_ == "_main_":
    
    print(generate_coordinate_list((1,1),(2,1),(3,3)))