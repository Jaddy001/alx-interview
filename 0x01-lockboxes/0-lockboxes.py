#!/usr/bin/python3

def canUnlockAll(boxes):
    # Initialize a set to keep track of unlocked boxes
    unlocked = {0}  # We can always unlock the first box (index 0)
    to_check = [0]  # A list to simulate a queue for BFS
    
    # Traverse through the boxes using BFS
    while to_check:
        current_box = to_check.pop()  # Get the next box to check
        
        # For each key in the current box, if it's a valid and not yet unlocked box, unlock it
        for key in boxes[current_box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                to_check.append(key)
    
    # If the number of unlocked boxes equals the total number of boxes, all can be unlocked
    return len(unlocked) == len(boxes)

