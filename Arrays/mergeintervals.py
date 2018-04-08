intervals = [(1,5),(3,7),(4,6),(6,8),(10,12),(11,15)]

def merge_intervals(intervals):
    merged_interval = []
    low, high = intervals[0]
    for start, end in intervals[1:]:
        if start > low and start <= high:
            if end > high:
                high = end
        elif start > high:
            merged_interval.append((low,high))
            low = start
            high = end
    merged_interval.append((low, high))
    return merged_interval

print(merge_intervals(intervals))
