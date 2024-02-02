def first_fit(item_list, bin_size, method=None):
    '''
    First-fit algorithm for the bin packing problem.
    Input:
        item_list (list): list of items to pack
        bin_size (float): capacity of each bin
        method (str): 'increasing' or 'decreasing' for variants
            of the algorithm. The default value is None,
            which corresponds to using the basic method with no sorting.
    
    Output:
        bin_list (list): a list of bins with what's inside of each bin.
    '''
    # Initialise a list of bins with one empty bin
    bin_list = [0]

    # Pre-sort the items depending on method
    if method == 'increasing':
        item_list = sorted(item_list)
    elif method == 'decreasing':
        item_list = sorted(item_list, reverse=True)

    # Take the items one by one, using a loop
    for i in range(len(item_list)):
        
        # Inside this loop, we're looking at the ith item.
        # We will need to keep track of whether this item will be
        # successfully placed in a bin. We can use a Boolean for this.
        placed = False      # we start with the item not placed in any bins.

        # Look at the open bins one by one
        for b in range(len(bin_list)):

            # Inside this loop, we're looking at the bth bin.
            # Does it fit?
            if item_list[i] <= bin_size - bin_list[b]:
                # It fits: place item i in bin b
                bin_list[b] += item_list[i]

                # Use our tracker to indicate that the item has now been placed
                # (so we know we won't need to open a new bin for now)
                placed = True

                # We don't need to look at the rest of the bins now,
                # as we've successfully placed our item in bin b. Stop the loop
                break
            
            # We don't need an "else:" as we don't do anything else with our item
            # if it doesn't fit in the current bin -- we just move on to the next bin.
        
        # Now we've finished looking over the bins. If we placed our item, there's nothing
        # else to do; we can continue with the item loop and go to the next item directly.
        # But if we have not placed our item, we now need to open an extra bin, and place
        # the item inside it.
        if not placed:
            bin_list.append(item_list[i])


    # Output the resulting list of bins with what they contain
    return bin_list


# Another way to do it, without the placed flag, but with a while loop...
# def first_fit(item_list, bin_size):
#     # Initialise a list of bins with one empty bin
#     bin_list = [0]

#     # Take the items one by one, using a for loop
#     for i in range(len(item_list)):
        
#         # Look at the open bins one by one, using a while loop.
#         # Start with bin 0.
#         b = 0
#         while b < len(bin_list):

#             # Inside this loop, we're looking at the bth bin.
#             # Does it fit?
#             if item_list[i] <= bin_size - bin_list[b]:
#                 # It fits: place item i in bin b
#                 bin_list[b] += item_list[i]

#                 # We don't need to look at the rest of the bins now,
#                 # as we've successfully placed our item in bin b. Stop the loop
#                 break

#             # If the item doesn't fit, move to the next available bin.
#             else:
#                 b += 1
        
#         # If we placed our item, there's nothing else to do; we can continue with
#         # the item loop and go to the next item directly.
#         # But if we have not placed our item, meaning we have exhausted our list
#         # of bins and we are now at b = len(bin_list),
#         # then we need to open a new bin.
#         if b == len(bin_list):
#             bin_list.append(item_list[i])


#     # Output the resulting list of bins with what they contain
#     return bin_list


# Data we have:

# size of each item
item_list = [2, 1, 3, 2, 1, 2, 3, 1]

# size of bin
bin_size = 4

# Output:
# some list of bins with what each bin contains.
# Solution to the question "how many bins are needed"
# can be obtained from len(bin_list).

print(first_fit(item_list, bin_size) == [4, 4, 4, 3])

# Another way to write the same test: using "assert".
# assert X will do nothing at all if X is True,
# and will give an AssertionError if X is False.
assert first_fit(item_list, bin_size) == [4, 4, 4, 3]

# Some more tests...

# All items have size 1
number_of_items = 50
item_list = [1] * number_of_items
bin_size = 15
expected_result = [bin_size]*(number_of_items // bin_size) + [number_of_items % bin_size]    # [15, 15, 15, 5]
assert first_fit(item_list, bin_size) == expected_result

# Single item
assert first_fit([5], 10) == [5]

# All items have size bin_size-1
number_of_items = 40
bin_size = 12
item_list = [bin_size-1] * number_of_items
expected_result = item_list.copy()    # just one item in each bin
assert first_fit(item_list, bin_size) == expected_result

# If we don't have an assertion error at this point, it means all our tests are correct:
print('All tests passed.')

# Testing the increasing/decreasing methods
item_list = [2, 1, 3, 2, 1, 2, 3, 1]
bin_size = 4
print(first_fit(item_list, bin_size, method='increasing'))
print(first_fit(item_list, bin_size, method='decreasing'))


def first_fit(item_list, bin_size, method=None):
    '''
    First-fit algorithm for the bin packing problem.
    Input:
        item_list (list): list of items to pack
        bin_size (float): capacity of each bin
        method (str): 'increasing' or 'decreasing' for variants
            of the algorithm. The default value is None,
            which corresponds to using the basic method with no sorting.
    
    Output:
        bin_list (list): a list of bins with the individual items inside of each bin.
    '''
    # Initialise a list of bins with one empty bin
    bin_list = [[]]

    # Pre-sort the items depending on method
    if method == 'increasing':
        item_list = sorted(item_list)
    elif method == 'decreasing':
        item_list = sorted(item_list, reverse=True)

    # Take the items one by one, using a loop
    for i in range(len(item_list)):
        
        placed = False      # we start with the item not placed in any bins.

        # Look at the open bins one by one
        for b in range(len(bin_list)):

            # Inside this loop, we're looking at the bth bin.
            # Does it fit?
            if item_list[i] <= bin_size - sum(bin_list[b]):
                # It fits: place item i in bin b
                bin_list[b].append(item_list[i])
                placed = True
                break
            
        # Open a new bin if current item has not been placed
        if not placed:
            bin_list.append([item_list[i]])

    # Output the resulting list of bins with individual items they contain
    return bin_list

# Testing...
item_list = [2, 1, 3, 2, 1, 2, 3, 1]
bin_size = 4
assert first_fit(item_list, bin_size) == [[2, 1, 1], [3, 1], [2, 2], [3]]
assert first_fit(item_list, bin_size, method='increasing') == [[1, 1, 1], [2, 2], [2], [3], [3]]
assert first_fit(item_list, bin_size, method='decreasing') == [[2, 1, 1], [3, 1], [2, 2], [3]]
print('Test passed.')