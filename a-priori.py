def get_frequent_itemsets(transactions, min_support):
    # Count individual items
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1
    
    # Filter by support
    frequent_items = {k: v for k, v in item_counts.items() if v >= min_support}
    
    # Find frequent pairs
    pairs = {}
    items_list = list(frequent_items.keys())
    for i in range(len(items_list)):
        for j in range(i + 1, len(items_list)):
            pair = tuple(sorted((items_list[i], items_list[j])))
            for transaction in transactions:
                if items_list[i] in transaction and items_list[j] in transaction:
                    pairs[pair] = pairs.get(pair, 0) + 1
                    
    frequent_pairs = {k: v for k, v in pairs.items() if v >= min_support}
    return frequent_items, frequent_pairs

# --- EXAMPLE 1: Online Pharmacy Orders ---
orders = [
    ["Vitamin-C", "Zinc", "Mask"],
    ["Vitamin-C", "Mask"],
    ["Zinc", "Mask", "Sanitizer"],
    ["Vitamin-C", "Zinc", "Mask"],
    ["Sanitizer", "Mask"]
]
print("Pharmacy Analysis:", get_frequent_itemsets(orders, 3))

# --- EXAMPLE 2: Playlist Genre Coupling ---
playlists = [
    ["Rock", "Metal", "Blues"],
    ["Pop", "Jazz"],
    ["Rock", "Metal"],
    ["Rock", "Blues", "Pop"],
    ["Rock", "Metal", "Jazz"]
]
print("Playlist Analysis:", get_frequent_itemsets(playlists, 3))