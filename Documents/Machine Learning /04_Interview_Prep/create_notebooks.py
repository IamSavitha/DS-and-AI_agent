#!/usr/bin/env python3
"""Create empty notebook templates for interview prep"""
import json
import os

def create_empty_notebook():
    return {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

# Data structures
data_structures = [
    ("01_Data_Structures/Arrays", "arrays_complete.ipynb"),
    ("01_Data_Structures/HashTables", "hash_tables_complete.ipynb"),
    ("01_Data_Structures/LinkedLists", "linked_lists_complete.ipynb"),
    ("01_Data_Structures/Trees", "trees_complete.ipynb"),
    ("01_Data_Structures/Stacks", "stacks_complete.ipynb"),
    ("01_Data_Structures/Queues", "queues_complete.ipynb"),
    ("01_Data_Structures/Graphs", "graphs_complete.ipynb"),
    ("01_Data_Structures/Heaps", "heaps_complete.ipynb"),
]

# Algorithms
algorithms = [
    ("02_Algorithms/Two_Pointers", "two_pointers_complete.ipynb"),
    ("02_Algorithms/Sorting", "sorting_complete.ipynb"),
    ("02_Algorithms/Searching", "searching_complete.ipynb"),
    ("02_Algorithms/Dynamic_Programming", "dynamic_programming_complete.ipynb"),
    ("02_Algorithms/Sliding_Window", "sliding_window_complete.ipynb"),
    ("02_Algorithms/Backtracking", "backtracking_complete.ipynb"),
    ("02_Algorithms/Greedy", "greedy_complete.ipynb"),
    ("02_Algorithms/Graph_Algorithms", "graph_algorithms_complete.ipynb"),
]

for folder, filename in data_structures + algorithms:
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            json.dump(create_empty_notebook(), f, indent=1)
        print(f"Created: {filepath}")

print("\nAll notebook templates created!")

