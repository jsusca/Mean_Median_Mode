import decimal
import math


def calculate_mean(numlist, decimals):
    decimal.getcontext().prec = decimals
    mean = decimal.Decimal(sum(numlist)) / decimal.Decimal(len(numlist))
    return decimal.Decimal(mean)


def calculate_median(numlist):
    numlist = sorted(numlist)
    if len(numlist) % 2 == 1:
        median = int(math.floor((len(numlist) / 2)))
        return numlist[median]
    else:
        median = int(math.floor((len(numlist) / 2)))
        return numlist[median], numlist[median - 1]


def calculate_mode(numlist):
    count_dict = {}

    # Fills dictionary with number:occurrences
    for i in numlist:
        count = numlist.count(i)
        if i not in count_dict.keys():
            count_dict[i] = count

    # Determines which number occurs most often
    max_count = 0
    for key in count_dict:
        if count_dict[key] >= max_count:
            max_count = count_dict[key]

    # Appends mode/s and number of occurrences to a list
    modes = []
    for num_key, value in count_dict.items():
        if value == max_count:
            modes.append(num_key)

    # Checks if there is no mode
    if max_count == 1:
        print("There is no mode. All numbers appear only once.")
    return modes, max_count


# Test case
nums = [2, 5, 8, 5, 8, 6, 8, 34, 18, 12, 8, 9, 9, 9, 9, 9]
print("Mode:", calculate_mode(nums), "\nMean:", calculate_mean(nums, 2), "\nMedian:", calculate_median(nums))
