import itertools

#part 1
freqs = open("day1input.txt").read().strip()
#print(freqs)
freqs = [int(line) for line in freqs.split("\n")]
frequency = sum(freqs)
print(frequency)

#part 2
freq_set = {0}
frequency = 0
for freq in itertools.cycle(freqs):
    frequency += freq
    if frequency in freq_set:
        print(frequency)
        break
    freq_set.add(frequency)