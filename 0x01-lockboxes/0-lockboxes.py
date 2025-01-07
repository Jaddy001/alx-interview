#!/usr/bin/python3

def canUnlockAll(boxes):
    # Set to keep track of unlocked boxes
    unlocked = set()
    unlocked.add(0)  # The first box is unlocked

    # List to use as a stack for DFS
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    # Check if all boxes can be unlocked
    return len(unlocked) == len(boxes)

