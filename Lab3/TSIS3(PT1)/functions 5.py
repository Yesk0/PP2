from itertools import permutations

def all_permutations(some_string : str):
    permutations_of_the_string = permutations(some_string)
    permutated_string_collection = list(permutations_of_the_string)
    permutated_string_collection = [''.join(permutation) for permutation in permutated_string_collection]
    for i in permutated_string_collection:
        print(i)

    return None