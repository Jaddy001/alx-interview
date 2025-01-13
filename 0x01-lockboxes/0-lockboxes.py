#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    The function performs a graph traversal (DFS) starting from box 0, using the keys
    in each unlocked box to open other boxes. The traversal continues until no more boxes
    can be unlocked. If all boxes are unlocked, the function returns True; otherwise, False.

    Args:
        boxes (list): A list of lists where each sublist represents a box, and contains
                      the keys (box numbers) that can be used to unlock other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    # Create a set to keep track of unlocked boxes, starting with box 0 unlocked
    unlocked = set([0])
    
    # Initialize a stack to perform DFS. We start from box 0.
    stack = [0]
    
    # Perform DFS to explore all reachable boxes
    while stack:
        box = stack.pop()  # Take the last box from the stack
        
        # Check all the keys in the current box
        for key in boxes[box]:
            # If the key opens a box that has not been unlocked yet
            if key < len(boxes) and key not in unlocked:
                # Unlock the box and add it to the stack for further exploration
                unlocked.add(key)
                stack.append(key)
    
    # If the number of unlocked boxes equals the total number of boxes,
    # it means all boxes can be unlocked.
    return len(unlocked) == len(boxes)

