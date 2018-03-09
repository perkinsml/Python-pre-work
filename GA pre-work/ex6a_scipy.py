from scipy import stats

sample = [3, 75, 98, 2, 10, 3, 14, 99, 44, 25, 31, 100, 356, 4, 23, 55, 327, 64, 6, 20]

mode = stats.mode(sample)
print(type(mode))

print(f"Mode: {mode.mode}. Mode count: {mode.count}")
