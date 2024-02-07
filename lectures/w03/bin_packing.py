def first_fit(item_list, bin_size):

    # Initialise a list of bins
    bin_list = [0]

    for item in item_list
    # Take our ith item
    if item <= bin_size - bin_list[0]:
        bin_list[0] += item

    else:
        bin_list.append(item)

    # bin_list[0]


    return bin_list





# Data we have:

# size of each item
item_list = [2, 1, 3, 2, 1, 2, 3, 1]


# size of bin
bin_size = 4

# Output:
# some list of bis with what each bin contains
# solution to "how many bins are needed?"
# can be obtained from len(bin_list)

print(first_fit(item_list, bin_size) == [4, 4, 4, 3])


















