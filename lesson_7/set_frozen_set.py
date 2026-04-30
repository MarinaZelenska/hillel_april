"""
===========================================
📘 Lecture: set() and frozenset in Python
===========================================

This file contains:
- theory examples
- demonstrations
- practice tasks
"""

# =========================
# 🔹 BASIC: set()
# =========================

print("=== BASIC SET ===")

# Creating a set
numbers = {1, 2, 3, 4}
print("Set:", numbers)

# Removing duplicates
numbers_with_duplicates = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers_with_duplicates)
print("Unique numbers:", unique_numbers)

# Empty set
empty_set = set()
print("Empty set:", empty_set)

# =========================
# 🔹 ADD / REMOVE
# =========================

print("\n=== ADD / REMOVE ===")

s = {1, 2, 3}

# Add element
s.add(4)
print("After add:", s)

# Remove element (error if not exists)
s.remove(2)
print("After remove:", s)

# Safe remove
s.discard(10)
print("After discard (no error):", s)

# Remove random element
removed = s.pop()
print("Removed random element:", removed)
print("Set now:", s)

# =========================
# 🔹 CHECK MEMBERSHIP
# =========================

print("\n=== CHECK MEMBERSHIP ===")

if 3 in s:
    print("3 is in set")
else:
    print("3 is not in set")

# =========================
# 🔹 SET OPERATIONS
# =========================

print("\n=== SET OPERATIONS ===")

a = {1, 2, 3}
b = {3, 4, 5}

print("A:", a)
print("B:", b)

# Union
print("Union:", a | b)

# Intersection
print("Intersection:", a & b)

# Difference
print("Difference (A - B):", a - b)

# Symmetric difference
print("Symmetric difference:", a ^ b)

# =========================
# 🔹 SUBSET / SUPERSET
# =========================

print("\n=== SUBSET / SUPERSET ===")

small = {1, 2}
big = {1, 2, 3}

print("Is subset:", small.issubset(big))
print("Is superset:", big.issuperset(small))

# =========================
# 🔒 FROZENSET
# =========================

print("\n=== FROZENSET ===")

fs = frozenset([1, 2, 3])
print("FrozenSet:", fs)

# Cannot modify (uncomment to see error)
# fs.add(4)

# But operations still work
fs2 = frozenset([3, 4])
print("Union:", fs | fs2)
print("Intersection:", fs & fs2)

# Using frozenset as dict key
data = {
    frozenset([1, 2]): "group1",
    frozenset([3, 4]): "group2"
}

print("Dict with frozenset keys:", data)

# =========================
# 🧩 PRACTICE TASKS
# =========================

print("\n=== TASKS ===")

# 🧩 Task 1: Remove duplicates
numbers = [1, 2, 2, 3, 4, 4]
result = list(set(numbers))
print("Task 1:", result)

# 🧩 Task 2: Find common elements
a = [1, 2, 3]
b = [2, 3, 4]
common = set(a) & set(b)
print("Task 2:", common)

# 🧩 Task 3: Unique elements
a = [1, 2, 3]
b = [3, 4, 5]
unique = set(a) ^ set(b)
print("Task 3:", unique)

# 🧩 Task 4: Check duplicates
numbers = [1, 2, 3, 4, 4]
has_duplicates = len(numbers) != len(set(numbers))
print("Task 4:", has_duplicates)

# 🧩 Task 5: Unique skills
users = [
    {"name": "Anna", "skills": ["Python", "SQL"]},
    {"name": "Bob", "skills": ["Python", "Java"]},
    {"name": "Kate", "skills": ["SQL", "Java"]}
]

all_skills = set()

for user in users:
    all_skills.update(user["skills"])

print("Task 5:", all_skills)

# 🧩 Task 6: Common skills
common_skills = set(users[0]["skills"])

for user in users[1:]:
    common_skills &= set(user["skills"])

print("Task 6:", common_skills)

# 🧩 Task 7: Group users by skills using frozenset
grouped = {}

for user in users:
    key = frozenset(user["skills"])

    if key not in grouped:
        grouped[key] = []

    grouped[key].append(user["name"])

print("Task 7:", grouped)

print("\n=== END OF FILE ===")