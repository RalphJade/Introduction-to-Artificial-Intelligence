# Introduction to Artificial Intelligence - Algorithm Showcase

## 📂 Featured Algorithms

1. **A* (A-Star) Search** - Pathfinding and Graph Traversal
2. **A-Priori** - Association Rule Mining (Frequent Itemset Research)
3. **Genetic Algorithm** - Evolutionary Optimization

---

## 1. A* (A-Star) Search Algorithm
A* is an informed search algorithm that finds the shortest path between a starting node and a goal. It uses the formula:
$$f(n) = g(n) + h(n)$$
Where:
* $g(n)$ is the cost from the start to the current node.
* $h(n)$ is the heuristic (estimated cost) to the goal.

### Examples in Code:
* **Industrial Warehouse:** Navigates a coordinate grid for a robot, treating shelving units as obstacles that must be bypassed.
* **Fiber Optic Network:** Finds the path with the lowest signal loss (latency) between server nodes in a weighted graph.



[Image of A* search algorithm flowchart]


---

## 2. A-Priori Algorithm 
The A-Priori algorithm is used for transactional data mining. It identifies frequent individual items in a database and extends them to larger itemsets as long as those sets appear sufficiently often (Minimum Support). 

### Examples in Code:
* **Online Pharmacy:** Analyzes customer orders to find which health supplements (e.g., Vitamin C and Zinc) are frequently purchased together.
* **Streaming Playlists:** Identifies "Genre Coupling" (e.g., Rock and Metal) in user-curated music playlists to suggest new artists.



---

## 3. Genetic Algorithm
This algorithm mimics the process of natural selection to find optimal solutions. It uses a population of strings that undergo:
1.  **Selection:** Keeping the "fittest" individuals.
2.  **Crossover:** Merging "DNA" from two parents.
3.  **Mutation:** Introducing random changes to maintain diversity.

### Examples in Code:
* **Smart Safe Cracker:** Evolves a random 4-digit sequence until it matches a hidden numeric vault combination.
* **DNA Matcher:** Evolves a bio-sequence string (using G, A, T, C) to match a target genetic pattern.



---

## 🚀 How to Run
Ensure you have Python installed. No external dependencies are required for the standard versions.

```bash
# To run A* Search
python a_star.py

# To run A-Priori Analysis
python a_priori.py

# To run Genetic Algorithm
python genetic_algo.py
