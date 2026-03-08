# Introduction to Artificial Intelligence - Core Algorithms

## 📂 Algorithms & Examples

### 1. A* (A-Star) Search Algorithm
A* is an informed search algorithm that finds the shortest path between a starting node and a goal. It uses the formula:
$$f(n) = g(n) + h(n)$$
Where **g(n)** is the actual cost from the start, and **h(n)** is the heuristic (estimated cost) to the goal.



* **Example 1: Warehouse Robot (Grid Mode)**
    Simulates a robot navigating a $3 \times 3$ grid. It treats coordinate `(1,1)` as a physical obstacle (wall) that the robot must intelligently bypass to reach its destination.
* **Example 2: City Courier (Weighted Graph)**
    Finds the most efficient route through city zones. It demonstrates that A* can choose a physically longer path ('Zone B') if it has lower "traffic" costs compared to a shorter but congested path ('Zone A').

---

### 2. A-Priori Algorithm (Pure Python)
The A-Priori algorithm is used for association rule mining. It identifies frequent itemsets in transactions, following the principle that if an itemset is frequent, all of its subsets must also be frequent.



* **Example 1: Online Pharmacy Orders**
    Analyzes customer baskets to discover that items like "Vitamin-C" and "Zinc" are frequently bought together, allowing for automated product bundling.
* **Example 2: Playlist Genre Coupling**
    Processes music playlists to identify which genres (e.g., Rock and Metal) are frequently paired together by listeners to improve recommendation engines.

---

### 3. Genetic Algorithm (Evolution-Inspired)
This algorithm mimics the process of natural selection. It maintains a population of potential solutions and "evolves" them through generations using fitness-based selection, crossover, and mutation.



* **Example 1: 4-Digit PIN Cracker**
    Starts with a population of random numbers and evolves them until they match the target vault combination `4921`.
* **Example 2: 5-Letter Code Evolution**
    Demonstrates string evolution by transforming a random population into the specific target keyword `AIZEN`.

---

## 🚀 Technical Implementation

| Algorithm | Method | Key Feature |
| :--- | :--- | :--- |
| **A\*** | `heapq` (Priority Queue) | Heuristic-driven efficiency |
| **A-Priori** | Dictionary-based Counting | Zero-dependency implementation |
| **Genetic** | Stochastic Evolution | Selection, Crossover, and Mutation |

