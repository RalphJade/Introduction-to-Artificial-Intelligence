import random

def evolve(target, charset, length):
    pop = [''.join(random.choice(charset) for _ in range(20)) for _ in range(50)]
    for gen in range(100):
        pop = sorted(pop, key=lambda x: sum(1 for a, b in zip(x, target) if a == b), reverse=True)
        if pop[0] == target: break
        
        new_gen = pop[:5] # Top 5 survive
        for _ in range(45):
            p1, p2 = random.sample(pop[:10], 2)
            child = p1[:length//2] + p2[length//2:]
            if random.random() < 0.1: # Mutation
                idx = random.randint(0, length-1)
                child = child[:idx] + random.choice(charset) + child[idx+1:]
            new_gen.append(child)
        pop = new_gen
    return pop[0], gen

# --- EXAMPLE 1: 4-Digit PIN ---
print(f"Ex 1 (PIN Cracked): {evolve('4921', '0123456789', 4)}")

# --- EXAMPLE 2: 5-Letter Code ---
print(f"Ex 2 (Code Evolved): {evolve('AIZEN', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 5)}")