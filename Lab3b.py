# Coded by Stephanie Callejas
# Last Edit: 06 Nov 2018
# CS2302 Lab 3 B Project
# Instructors: Diego Aguirre and Saha, Manoj Pravakar
# Goal: Determine if a given anagram is a valid word in the english language

from NodeAVL import Node, AVLTree
from TreePrint import pretty_tree
from RedBlackTree import RedBlackTree

# f is used to populate the tree with the words

f = open("words.txt")
word_list = f.readlines()

for i in range(len(word_list)):
    word_list[i] = word_list[i][:-2]  # -2 to get rid of the enter space
counter = 0


# The method print_anagrams shown below prints all the anagrams of a given word.
# To do this, it generates all permutations of the letters in the word and, for each permutation,
# it checks if it is a valid word in the English language.
# if you call print_anagrams("spot"),the method should print the following words: spot, stop, post, pots, opts, and tops

def print_anagrams(word, prefix=""):
    if len(word) <= 1:
        str = prefix + word

        if str in word_list:
            print(prefix + word)

    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated.
                print_anagrams(before + after, prefix + cur)


# count_anagrams does not produce output, but returns the number of anagrams that a given word has.
# For example, count_anagrams("spot") should return 6.

def count_anagrams(word, prefix=""):
    global counter
    if len(word) <= 1:
        str = prefix + word
        if str in word_list:
            counter += 1
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated.
                count_anagrams(before + after, prefix + cur)
    return counter


# greatest_anagrams reads another file that contains words (feel free to create it yourself)
# and finds the word in the file that has the greatest number of anagrams.

def greatest_anagrams(file, tree):
    print()
    # need to traverse the whole tree


# english_words reads "words.txt" file and populates the binary search tree
# with all the English words contained in the file.

def english_words(tree):
    counter = 0
    for ln in word_list:
        if counter == 10:
            break
        ln = ln.replace('\n', '')
        print(ln)
        ln = Node(ln)
        tree.insert(ln)
        counter += 1
    return tree


# def main():
print_anagrams("stop")
counter = count_anagrams("stop")
print("Number of anagrams", counter)
counter = count_anagrams("stop")
# print("Number of anagrams", counter)

myTree = None
tree_type = raw_input('what type of tree do you want to use?, AVL or RBT \n')
if tree_type == 'AVL':
    myTree = AVLTree()
elif tree_type == 'RBT':
    myTree = RedBlackTree()

if myTree is not None:
    tree = english_words(myTree)


counter = 0
tree = AVLTree()
for ln in word_list:
    if counter == 10000:
        break
    ln = ln.replace('\n', '')
    ln = Node(ln)
    tree.insert(ln)
    counter += 1

    print(pretty_tree(tree))
if tree_type == 'AVL':
    tree_AVL = AVLTree()
    for ln in word_list:
        ln = ln.replace('\n', '')
        words = Node(ln)
        tree_AVL.insert(words)
    print(tree_AVL)

if tree_type == 'RBT':
    tree_RBT = RedBlackTree()
    for ln in word_list:
        tree_RBT.insert(ln)
    print('tree has height ' + str(tree_RBT.get_height()))
