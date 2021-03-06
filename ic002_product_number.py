def get_products_of_all_ints_except_at_index(nums):
    """
    Get a list of numbers and return a list of those numbers with their products
    except for the number at the index.

    Do not use division.

    For example:

        >>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
        [84, 12, 28, 21]

    Because it's doing this calculation: [7*3*4, 1*3*4, 1*7*4, 1*7*3]
    """

    # brute force, O(n^2) time due to nested loop

    results = []
    multiplier = 1

    for i, num in enumerate(nums):
        for j, n in enumerate(nums):
            if i != j:
                multiplier = multiplier * n
        results.append(multiplier)
        multiplier = 1

    return results


def get_products_of_all_ints_except_at_index_v2(nums):
    """
    Get a list of numbers and return a list of those numbers with their products
    except for the number at the index.

    Do not use division.

    For example:

        >>> get_products_of_all_ints_except_at_index_v2([1, 7, 3, 4])
        [84, 12, 28, 21]

    Because it's doing this calculation: [7*3*4, 1*3*4, 1*7*4, 1*7*3]
    """

    # elegant solution, O(n)

    # make the list
    results = [None] * len(nums)

    # loop through and calculate all numbers before the index
    multiplier = 1
    for i in range(len(nums)):
        results[i] = multiplier
        multiplier *= nums[i]

    multiplier = 1
    for i in reversed(range(len(nums))):
        results[i] *= multiplier
        multiplier *= nums[i]

    return results
