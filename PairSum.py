import nums as nums
from networkx.algorithms.assortativity import pairs


def pair_sum_div(nums, k):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) % k == 0:
                pairs.append((nums[i], nums[j]))
    return len(pairs), pairs


if __name__ == "__main__":
    n, p = pair_sum_div([2, 2, 1, 7, 5, 3], 4)
    print(f"pairs: {n}\n{p}")
