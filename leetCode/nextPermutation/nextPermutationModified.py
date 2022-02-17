# Objective:
# Lexicographical Permutation Succession
#
# Return next highest permutation.
# If no higher permutation exists, return 'no answer exists'
#
# I recently had to deal with this problem, but was unable to satisfy all of the 
#   conditions during testing.
# I was able to handle strings like the following:
#   abcd
#   aaaa
# But I was unable to handle a few cases where the letters were already in the highest
#   reverse alphabetical order. I gave up. Now I'm trying again.
#   example: zyxw

def rearrangeArray(array):

    numOfElements = len(array)
    selection = numOfElements - 2
    #  we are first looking for the first instance from left to right that:
    #    array[i] < array [i + 1]
    #    -1 is end of the array, so array[-2] is the element principally concerned
    while selection >= 0:
        if array[selection] < array[selection + 1]:
            break
            #  this is the first instance in which array[i] < array[i + 1]
        selection = selection - 1
            #  desired behavior not identified so: this moves our selection one to 
            #    the left, getting closer to index 0
    if selection < 0:
        array = array[::-1]
        #  print("Array was inverted.")
        return 'no answer exists'
        #  the array is already fully permutated, return no answer.
        #  reverse the array and begin searching the other direction
        #  this is the exception handle I failed to handle in the question
    else:
        for number in range(numOfElements -1, selection, -1):
            if array[number] > array[selection]:
                break
                #  you have found the first number array[ -1 - x] that is greater than
                #    array[selection]
        array[number], array[selection] = array[selection], array[number]
            #  swap the two numbers to get the next permutation
        array[selection + 1:] = reversed(array[selection + 1:])
            #  reverse the list of elements to the right of the replaced selected
            #    element
    return array

# supply word
testCases = ["zyxw", "zzzz", "abcd"]
for word in testCases:
    # convert word to list of numbers
    wordAsNum = []
    permutation = []
    for letter in word:
        wordAsNum.append(ord(letter) - 96)

    # generate permutation
    permAsNum = rearrangeArray(wordAsNum)
    if permAsNum == 'no answer exists':
        joinedPermutation = permAsNum
        pass
    else:
        for letter in permAsNum:
            permutation.append(chr(ord('`') + letter))
        joinedPermutation = ''.join(permutation)

    print("Test Case:", word)
    print("Permutation:", joinedPermutation)


#  Output:

#  Test Case: zyxw
#  Permutation: no answer exists
#  Test Case: zzzz
#  Permutation: no answer exists
#  Test Case: abcd
#  Permutation: abdc