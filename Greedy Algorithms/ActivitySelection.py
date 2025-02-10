def activity_selector(intervals):
    if not intervals:
        return []
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    optimal_solution = [sorted_intervals[0]]
    current_end_time = sorted_intervals[0][1]
    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i][0] >= current_end_time:
            optimal_solution.append(sorted_intervals[i])
            current_end_time = sorted_intervals[i][1]
    return optimal_solution


# Example usage
intervals_ = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
print(activity_selector(intervals_))
