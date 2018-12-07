# An approach using a set
def countwords_set(s):
    for c in set(s):
        if c == ' ': continue
        print(c, 'in', s.count(c))

# An approach using a standard dict
def countwords_dict(s):
    d = dict()
    for c in s:
        if c == ' ': continue               # Skip spaces
        d[c] = d.get(c,0) + 1               # Use the .get method in case the 
                                            #   key isn't set

    for c,x in d.items():                   # Display results
        print(c, 'in', x)


# An approach using a defaultdict (from the collections module)
def countwords_ddict(s):
    from collections import defaultdict     # Typically, imports go at the top

    d = defaultdict(int)

    for c in s:
        if c == ' ': continue
        d[c] += 1

    for c,x in d.items():
        print(c, 'in', x)


# An approach using a Counter (from the collections module)
def countwords_counter(s):
    from collections import Counter         # Typically, imports go at the top

    counter = Counter(s)

    # Counters can be accessed like dicts
    for c,x in counter.items():
        if c == ' ': continue
        print(c, 'in', x)


# User input and comparison
s = str(input("Enter a paragraph "))
s = s.lower()

countwords_set(s)
print("---")

countwords_dict(s)
print("---")

countwords_ddict(s)
print("---")

countwords_counter(s)
print("---")