"""Timetable scheduling as a Constraint Satisfaction Problem (CSP)
Search technique: Backtracking
"""

# ---------- 1. Variables ----------
variables = ["Maths", "Python", "DBMS", "AI"]

# ---------- 2. Domains ----------
time_slots = ["9:00 AM", "11:00 AM", "2:00 PM"]
domains = {var: list(time_slots) for var in variables}

# ---------- 3. Constraints ----------
# Each pair must NOT share the same time slot.
not_equal_pairs = [
    ("Maths", "Python"),
    ("DBMS", "AI"),
]


def is_consistent(var, value, assignment):
    """Check that giving `var` the slot `value` breaks no constraint."""
    for a, b in not_equal_pairs:
        if var == a and assignment.get(b) == value:
            return False
        if var == b and assignment.get(a) == value:
            return False
    return True


# ---------- 4. Backtracking search ----------
def backtrack(assignment):
    # Every subject has exactly one slot -> solution found
    if len(assignment) == len(variables):
        return assignment

    # Pick the next unassigned subject
    var = next(v for v in variables if v not in assignment)

    for value in domains[var]:
        if is_consistent(var, value, assignment):
            assignment[var] = value          # try this slot
            result = backtrack(assignment)   # recurse
            if result is not None:
                return result
            del assignment[var]              # dead end -> undo (backtrack)
    return None


# ---------- 5. Solve and display ----------
solution = backtrack({})

if solution:
    print("Final Timetable")
    print("-" * 28)
    print(f"{'Subject':<10}| Time Slot")
    print("-" * 28)
    for subject in variables:
        print(f"{subject:<10}| {solution[subject]}")

    print("\nConstraint check:")
    for a, b in not_equal_pairs:
        ok = solution[a] != solution[b]
        print(f"  {a} != {b}: {solution[a]} vs {solution[b]} -> {'OK' if ok else 'VIOLATED'}")
else:
    print("No valid timetable exists.")
