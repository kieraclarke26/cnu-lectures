def first_fit(item_list, bin_size):
    # Initialise a list of bins with one empty bin
    bin_list = [0]

    # Take the items one by one, using a loop
    for i in range(len(item_list)):
        
        # Inside this loop, we're looking at the ith item.
        # We will need to keep track of whether this item will be
        # successfully placed in a bin. We can use a Boolean for this.
        placed = False      # we start with the item not placed in any bins.

        # Look at the open bins one by one
        for b in ...

            # Inside this loop, we're looking at the bth bin.
            # Does it fit?
            if ...
                # It fits: place item i in bin b
                ...

                # Use our tracker to indicate that the item has now been placed
                # (so we know we won't need to open a new bin for now)
                ...

                # We don't need to look at the rest of the bins now,
                # as we've successfully placed our item in bin b. Stop the loop
                ...
            
            # We don't need an "else:" as we don't do anything else with our item
            # if it doesn't fit in the current bin -- we just move on to the next bin.
        
        # Now we've finished looking over the bins. If we placed our item, there's nothing
        # else to do; we can continue with the item loop and go to the next item directly.
        # But if we have not placed our item, we now need to open an extra bin, and place
        # the item inside it.
        if ...
            ...


    # Output the resulting list of bins with what they contain
    return bin_list



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