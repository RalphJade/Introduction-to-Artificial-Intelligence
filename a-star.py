import heapq

def a_star(graph, start, goal, h, grid_mode=False):
    open_list = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    while open_list:
        current = heapq.heappop(open_list)[1]
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        for neighbor, weight in graph[current].items():
            tentative_g = g_score[current] + weight
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h.get(neighbor, 0)
                heapq.heappush(open_list, (f_score, neighbor))
    return "No Path"

# --- EXAMPLE 1: Warehouse Robot (Grid) ---
# A 5x5 grid converted to a graph. Obstacle at (1,1) and (1,2)
warehouse_graph = {(r, c): {} for r in range(3) for c in range(3)}
# Add edges (simplified movement)
for r, c in warehouse_graph:
    for dr, dc in [(0,1), (1,0)]:
        if (r+dr, c+dc) in warehouse_graph and (r+dr, c+dc) != (1,1):
            warehouse_graph[(r,c)][(r+dr, c+dc)] = 1

h_warehouse = {(r, c): abs(r-2) + abs(c-2) for r, c in warehouse_graph}
print("Ex 1 (Warehouse Path):", a_star(warehouse_graph, (0,0), (2,2), h_warehouse))

# --- EXAMPLE 2: City Courier (Weighted Graph) ---
city_map = {
    'Hub': {'Zone_A': 5, 'Zone_B': 10},
    'Zone_A': {'Target': 15},
    'Zone_B': {'Target': 2}, # Zone B is further but has less traffic
    'Target': {}
}
h_city = {'Hub': 12, 'Zone_A': 10, 'Zone_B': 2, 'Target': 0}
print("Ex 2 (City Courier Path):", a_star(city_map, 'Hub', 'Target', h_city))