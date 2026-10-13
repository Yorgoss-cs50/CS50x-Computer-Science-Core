import sys

names = ["David", "Ryan", "Tobey", "Andrew", "Anna"]

if "Anna" in names:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)
