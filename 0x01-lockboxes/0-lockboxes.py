#!/usr/bin/python3

def canUnlockAll(boxes):
    # Set to keep track of unlocked boxes
    unlocked = set()
    unlocked.add(0)  # The first box is unlocked by default
    
    # Stack to perform DFS, starting from box 0
    stack = [0]
    
    # Perform DFS
    while stack:
        current_box = stack.pop()  # Get the current box
        
        # For every key in the current box
        for key in boxes[current_box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)  # Unlock the box
                stack.append(key)  # Add to stack to visit later
    
    # Check if all boxes have been unlocked
    return len(unlocked) == len(boxes)

