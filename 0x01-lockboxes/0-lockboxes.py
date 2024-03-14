#!/usr/bin/python3
"""Trchnical Interview: Lockboxes"""


from collections import deque


def canUnlockAll(boxes):
    """Check to see if you can open all boxes
    Return: True if all boxes can open, false otherwise"""
    if not boxes or not boxes[0]:
        return False
    keys = deque(boxes[0])
    visited = {0}
    boxes_length = len(boxes)
    length = 0
    while keys:
        length += 1
        key = keys.popleft()
        if key in visited or key >= boxes_length:
            continue
        keys.extend(boxes[key])
        visited.add(key)
    total_len = 0
    for i in boxes:
        total_len += len(i)

    if total_len == length:
        return True
    return False
