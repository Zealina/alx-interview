#!/usr/bin/python3
"""Trchnical Interview: Lockboxes"""


from collections import deque


def canUnlockAll(boxes):
    """Check to see if you can open all boxes
    Return: True if all boxes can open, false otherwise"""
    if not boxes:
        return False
    keys = deque(boxes[0])
    visited = {0}
    while keys:
        key = keys.popleft()
        if key in visited:
            continue
        keys.extend(boxes[key])
        visited.add(key)
    if len(visited) == len(boxes):
        return True
    return False
