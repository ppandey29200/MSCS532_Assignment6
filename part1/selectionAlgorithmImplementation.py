import random
import time


def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    
    # Step 1: Divide array into groups of 5
    chunks = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks]
    
    # Step 2: Find the median of medians
    pivot = median_of_medians(medians, len(medians)//2)
    
    # Step 3: Partition array around pivot
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    
    # Step 4: Recurse to find k-th smallest
    if k < len(lows):
        return median_of_medians(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return median_of_medians(highs, k - len(lows) - len(pivots))


def randomized_quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    # Step 1: Choose random pivot
    pivot = random.choice(arr)
    
    # Step 2: Partition array around pivot
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    
    # Step 3: Recurse to find k-th smallest
    if k < len(lows):
        return randomized_quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return randomized_quickselect(highs, k - len(lows) - len(pivots))


# Testing and Empirical Analysis
def test_selection_algorithms():
    input_sizes = [100, 1000, 10000, 50000]
    distributions = ["random", "sorted", "reverse-sorted"]
    print(f"{'Size':<10}{'Type':<20}{'MedianOfMedians':<20}{'Quickselect':<20}")

    for size in input_sizes:
        for dist in distributions:
            if dist == "random":
                arr = [random.randint(0, size) for _ in range(size)]
            elif dist == "sorted":
                arr = list(range(size))
            elif dist == "reverse-sorted":
                arr = list(range(size, 0, -1))
            
            k = size // 2  # Find the median
            
            # Test Median of Medians
            start_time = time.time()
            median_of_medians(arr, k)
            mom_time = time.time() - start_time
            
            # Test Randomized Quickselect
            start_time = time.time()
            randomized_quickselect(arr, k)
            quickselect_time = time.time() - start_time            
            print(f"{size:<10}{dist:<20}{mom_time:<20.6f}{quickselect_time:<20.6f}")


if __name__ == "__main__":
    test_selection_algorithms()