#  Lexicographical Permutation Problems

Recently I was faced with a problem in which I was asked to do the following:

Given a string of characters, find the next greater permutation of characters.

For example:
    Given: lmno
    Return: lmon

I was only asked to iterate once, not find the whole list of all permutations until I could no longer.

I was able to get it to work in about 90% of test cases... But I failed on one:

Where:
    Given: zyxw
    Return: 'no answer possible'

I did handle the edge case of all the same characters.

Anyway. I was really bummed out. So I went and studied and made this one. This one appears to solve the problem adequately.

The typical algorithm looks like:
    * From left to right, find array[i] where array[i] < array[i+1]
        * If i < 0, break out because your array is already sorted descending order
    * From array[i], find where array[i + x] closest < array[i]
    * Swap those two values
    * Reverse order all from array[i +1:]

Mine deviates from after that first break: 
    * From left to right, find array[i] where array[i] < array[i+1]
    * If i < 0, break out because your array is already sorted descending order
    * From right to left, find array[-1 - j] where array[i] > array[-1 - j]
    * Swap the values of array[i] and array[-1 -j]
    * Reverse order all from array[i + 1:]