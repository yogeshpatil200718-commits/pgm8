import sys

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
average = total / len(scores)

print("Scores:", scores) 
print("Sum:", total) 
print("Average:", average)

#--------------------------------------------------
maximum = max(scores)
minimum = min(scores)

print("Maximum Score:",maximum)
print("Minimum Score:",minimum)