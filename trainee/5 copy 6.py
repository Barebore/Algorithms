def combine_rows_cols(arr):
    row_sums = [sum(row) for row in arr]
    col_sums = [sum(col) for col in zip(*arr)]
    all_sums = row_sums + col_sums
    return set([sum(comb) for i in range(1, len(all_sums) + 1) for comb in combinations(all_sums, i)])

def()