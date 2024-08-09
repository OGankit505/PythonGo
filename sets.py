# Create an empty set
my_set = set()

# Create a set with initial values
my_set = {1, 2, 3}

# Add an element to a set
my_set.add(4)

# Remove an element from a set
my_set.remove(2)

# Check if an element is in a set
if 3 in my_set:
    print("3 is in the set")

# Get the length of a set
length = len(my_set)

# Iterate over a set
for element in my_set:
    print(element)

# Perform set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets
union_set = set1.union(set2)

# Intersection of two sets
intersection_set = set1.intersection(set2)

# Difference between two sets
difference_set = set1.difference(set2)

# Check if a set is a subset of another set
if set1.issubset(set2):
    print("set1 is a subset of set2")

# Check if a set is a superset of another set
if set1.issuperset(set2):
    print("set1 is a superset of set2")

    # Check if two sets are disjoint (i.e., have no common elements)
    if set1.isdisjoint(set2):
        print("set1 and set2 are disjoint")

    # Remove all elements from a set
    my_set.clear()

    # Create a shallow copy of a set
    copy_set = my_set.copy()

    # Remove and return an arbitrary element from a set
    element = my_set.pop()

    # Remove an element from a set if it is present, otherwise do nothing
    my_set.discard(5)

    # Update a set with the union of itself and another set
    my_set.update({4, 5, 6})

    # Remove elements from a set that are not present in another set
    my_set.intersection_update({1, 2, 3})

    # Remove elements from a set that are present in another set
    my_set.difference_update({3, 4, 5})

    # Remove elements from a set that are present in all other specified sets
    my_set.symmetric_difference_update({2, 3, 4})

    # Create a set with elements that are present in either of the sets, but not both
    symmetric_difference_set = set1.symmetric_difference(set2)