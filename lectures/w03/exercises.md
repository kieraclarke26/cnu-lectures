# The first-fit algorithm for bin packing

In the lecture we started writing the function to implement the first-fit algorithm for the bin-packing problem.

Try to finish the function! You can pick your level of challenge depending on how comfortable you feel with the code.

- You can finish the function yourself from scratch. In the lecture, we started by looking at just one item and one bin, then we later changed the code to look at all items; you will need to continue making similar changes to complete the algorithm. Don't be afraid to change the code we have so far -- don't necessarily treat it as your starting point.
- If you'd prefer some hints:
    - I've added a `bin_packing_skeleton.py` script, with some code comments indicating the structure of the function, and some `...` in place of commands. You can complete the code there by replacing the `...` with appropriate commands.
    - You can also [click here to get a Parson's puzzle of the finished function](https://parsons.problemsolving.io/puzzle/6da27ce27f3f4aa8a80671e907ce5eaa). A Parson's puzzle is a programming exercise/question, where you are given all the code, but the lines are given to you in a random order -- you need to put them back in the correct order, and with the correct indentation.

And an extra few practice questions, once you have the correct function:

- In the lecture, we've talked about different things our function could return. Change it so that instead of returning a list of bins with the total occupied volume for each bin, your function returns a list of bins, where each bin is itself a list of the different objects inside it, in the order in which they've been added. With our example, the result should be `[[2, 1, 1], [3, 1], [2, 2], [3]]`.
- Two adaptations of this algorithm are the "first fit increasing" and the "first fit decreasing" methods. The difference is that, before placing the items in bins, you sort them in increasing/decreasing order of size. Add one more input argument to your `first_fit()` function called `method`, which can be `'increasing'` or `'decreasing'`, so that depending on the chosen `method`, the function implements the increasing or the decreasing algorithm. Which one performs better on the test example?
- Create other test values for you to check that your function works as expected. Think about things that are easy to check: what should the total volume of items in your bins be equal to? What should the result be if all items have size 1? size `bin_size - 1`? size `bin_size`? What if `bin_size` is 1? What should the result be if there is only one item? etc...
- Expand your function so that it also deals with cases where some of the items are bigger than the bin size, and therefore cannot be placed in any bins. You can choose how you want to deal with this -- stop the function and give an error message, set them aside in a special "big items" bin, etc...