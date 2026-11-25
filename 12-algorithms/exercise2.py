def build_prefix(nums):

    prefix = [0]

    running_sum = 0

    for num in nums:
        running_sum += num
        prefix.append(running_sum)

    return prefix


def range_sum(prefix, left, right):

    return prefix[right + 1] - prefix[left]


def equilibrium_index(nums):

    total_sum = sum(nums)

    left_sum = 0

    for i in range(len(nums)):

        right_sum = (
            total_sum
            - left_sum
            - nums[i]
        )

        if left_sum == right_sum:
            return i

        left_sum += nums[i]

    return -1


def count_subarrays_with_sum(nums, k):

    prefix_count = {0: 1}

    current_sum = 0

    count = 0

    for num in nums:

        current_sum += num

        count += prefix_count.get(
            current_sum - k,
            0
        )

        prefix_count[current_sum] = (
            prefix_count.get(current_sum, 0) + 1
        )

    return count




sales = [5, 3, 8, 6, 1, 4]

prefix = build_prefix(sales)

print("prefix:", prefix)

print("sum days 1..3:",
      range_sum(prefix, 1, 3))

print("sum days 0..5:",
      range_sum(prefix, 0, 5))

print(
    "equilibrium of [1, 7, 3, 6, 5, 6]:",
    equilibrium_index([1, 7, 3, 6, 5, 6])
)

print(
    "subarrays summing to 3 in [1, 2, 1, 2, 1]:",
    count_subarrays_with_sum(
        [1, 2, 1, 2, 1],
        3
    )
)