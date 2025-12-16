#!/usr/bin/env python3
"""
LeetCode 75 Problem Generator
Usage:
    python lc75.py generate    - Get a random unsolved problem
    python lc75.py solve <id>  - Mark a problem as solved
    python lc75.py status      - Show progress
    python lc75.py list        - List all problems with status
    python lc75.py reset       - Reset all progress
"""

import json
import random
import sys
from pathlib import Path

# LeetCode 75 Study Plan
LEETCODE_75 = [
    # Array / String
    {"id": 1768, "name": "Merge Strings Alternately", "difficulty": "Easy", "category": "Array / String"},
    {"id": 1071, "name": "Greatest Common Divisor of Strings", "difficulty": "Easy", "category": "Array / String"},
    {"id": 1431, "name": "Kids With the Greatest Number of Candies", "difficulty": "Easy", "category": "Array / String"},
    {"id": 605, "name": "Can Place Flowers", "difficulty": "Easy", "category": "Array / String"},
    {"id": 345, "name": "Reverse Vowels of a String", "difficulty": "Easy", "category": "Array / String"},
    {"id": 151, "name": "Reverse Words in a String", "difficulty": "Medium", "category": "Array / String"},
    {"id": 238, "name": "Product of Array Except Self", "difficulty": "Medium", "category": "Array / String"},
    {"id": 334, "name": "Increasing Triplet Subsequence", "difficulty": "Medium", "category": "Array / String"},
    {"id": 443, "name": "String Compression", "difficulty": "Medium", "category": "Array / String"},
    # Two Pointers
    {"id": 283, "name": "Move Zeroes", "difficulty": "Easy", "category": "Two Pointers"},
    {"id": 392, "name": "Is Subsequence", "difficulty": "Easy", "category": "Two Pointers"},
    {"id": 11, "name": "Container With Most Water", "difficulty": "Medium", "category": "Two Pointers"},
    {"id": 1679, "name": "Max Number of K-Sum Pairs", "difficulty": "Medium", "category": "Two Pointers"},
    # Sliding Window
    {"id": 643, "name": "Maximum Average Subarray I", "difficulty": "Easy", "category": "Sliding Window"},
    {"id": 1456, "name": "Maximum Number of Vowels in a Substring of Given Length", "difficulty": "Medium", "category": "Sliding Window"},
    {"id": 1004, "name": "Max Consecutive Ones III", "difficulty": "Medium", "category": "Sliding Window"},
    {"id": 1493, "name": "Longest Subarray of 1's After Deleting One Element", "difficulty": "Medium", "category": "Sliding Window"},
    # Prefix Sum
    {"id": 1732, "name": "Find the Highest Altitude", "difficulty": "Easy", "category": "Prefix Sum"},
    {"id": 724, "name": "Find Pivot Index", "difficulty": "Easy", "category": "Prefix Sum"},
    # Hash Map / Set
    {"id": 2215, "name": "Find the Difference of Two Arrays", "difficulty": "Easy", "category": "Hash Map / Set"},
    {"id": 1207, "name": "Unique Number of Occurrences", "difficulty": "Easy", "category": "Hash Map / Set"},
    {"id": 1657, "name": "Determine if Two Strings Are Close", "difficulty": "Medium", "category": "Hash Map / Set"},
    {"id": 2352, "name": "Equal Row and Column Pairs", "difficulty": "Medium", "category": "Hash Map / Set"},
    # Stack
    {"id": 2390, "name": "Removing Stars From a String", "difficulty": "Medium", "category": "Stack"},
    {"id": 735, "name": "Asteroid Collision", "difficulty": "Medium", "category": "Stack"},
    {"id": 394, "name": "Decode String", "difficulty": "Medium", "category": "Stack"},
    # Queue
    {"id": 933, "name": "Number of Recent Calls", "difficulty": "Easy", "category": "Queue"},
    {"id": 649, "name": "Dota2 Senate", "difficulty": "Medium", "category": "Queue"},
    # Linked List
    {"id": 2095, "name": "Delete the Middle Node of a Linked List", "difficulty": "Medium", "category": "Linked List"},
    {"id": 328, "name": "Odd Even Linked List", "difficulty": "Medium", "category": "Linked List"},
    {"id": 206, "name": "Reverse Linked List", "difficulty": "Easy", "category": "Linked List"},
    {"id": 2130, "name": "Maximum Twin Sum of a Linked List", "difficulty": "Medium", "category": "Linked List"},
    # Binary Tree - DFS
    {"id": 104, "name": "Maximum Depth of Binary Tree", "difficulty": "Easy", "category": "Binary Tree - DFS"},
    {"id": 872, "name": "Leaf-Similar Trees", "difficulty": "Easy", "category": "Binary Tree - DFS"},
    {"id": 1448, "name": "Count Good Nodes in Binary Tree", "difficulty": "Medium", "category": "Binary Tree - DFS"},
    {"id": 437, "name": "Path Sum III", "difficulty": "Medium", "category": "Binary Tree - DFS"},
    {"id": 1372, "name": "Longest ZigZag Path in a Binary Tree", "difficulty": "Medium", "category": "Binary Tree - DFS"},
    {"id": 236, "name": "Lowest Common Ancestor of a Binary Tree", "difficulty": "Medium", "category": "Binary Tree - DFS"},
    # Binary Tree - BFS
    {"id": 199, "name": "Binary Tree Right Side View", "difficulty": "Medium", "category": "Binary Tree - BFS"},
    {"id": 1161, "name": "Maximum Level Sum of a Binary Tree", "difficulty": "Medium", "category": "Binary Tree - BFS"},
    # Binary Search Tree
    {"id": 700, "name": "Search in a Binary Search Tree", "difficulty": "Easy", "category": "Binary Search Tree"},
    {"id": 450, "name": "Delete Node in a BST", "difficulty": "Medium", "category": "Binary Search Tree"},
    # Graphs - DFS
    {"id": 841, "name": "Keys and Rooms", "difficulty": "Medium", "category": "Graphs - DFS"},
    {"id": 547, "name": "Number of Provinces", "difficulty": "Medium", "category": "Graphs - DFS"},
    {"id": 1466, "name": "Reorder Routes to Make All Paths Lead to the City Zero", "difficulty": "Medium", "category": "Graphs - DFS"},
    {"id": 399, "name": "Evaluate Division", "difficulty": "Medium", "category": "Graphs - DFS"},
    # Graphs - BFS
    {"id": 1926, "name": "Nearest Exit from Entrance in Maze", "difficulty": "Medium", "category": "Graphs - BFS"},
    {"id": 994, "name": "Rotting Oranges", "difficulty": "Medium", "category": "Graphs - BFS"},
    # Heap / Priority Queue
    {"id": 215, "name": "Kth Largest Element in an Array", "difficulty": "Medium", "category": "Heap / Priority Queue"},
    {"id": 2336, "name": "Smallest Number in Infinite Set", "difficulty": "Medium", "category": "Heap / Priority Queue"},
    {"id": 2542, "name": "Maximum Subsequence Score", "difficulty": "Medium", "category": "Heap / Priority Queue"},
    {"id": 2462, "name": "Total Cost to Hire K Workers", "difficulty": "Medium", "category": "Heap / Priority Queue"},
    # Binary Search
    {"id": 374, "name": "Guess Number Higher or Lower", "difficulty": "Easy", "category": "Binary Search"},
    {"id": 2300, "name": "Successful Pairs of Spells and Potions", "difficulty": "Medium", "category": "Binary Search"},
    {"id": 162, "name": "Find Peak Element", "difficulty": "Medium", "category": "Binary Search"},
    {"id": 875, "name": "Koko Eating Bananas", "difficulty": "Medium", "category": "Binary Search"},
    # Backtracking
    {"id": 17, "name": "Letter Combinations of a Phone Number", "difficulty": "Medium", "category": "Backtracking"},
    {"id": 216, "name": "Combination Sum III", "difficulty": "Medium", "category": "Backtracking"},
    # DP - 1D
    {"id": 1137, "name": "N-th Tribonacci Number", "difficulty": "Easy", "category": "DP - 1D"},
    {"id": 746, "name": "Min Cost Climbing Stairs", "difficulty": "Easy", "category": "DP - 1D"},
    {"id": 198, "name": "House Robber", "difficulty": "Medium", "category": "DP - 1D"},
    {"id": 790, "name": "Domino and Tromino Tiling", "difficulty": "Medium", "category": "DP - 1D"},
    # DP - Multidimensional
    {"id": 62, "name": "Unique Paths", "difficulty": "Medium", "category": "DP - Multidimensional"},
    {"id": 1143, "name": "Longest Common Subsequence", "difficulty": "Medium", "category": "DP - Multidimensional"},
    {"id": 714, "name": "Best Time to Buy and Sell Stock with Transaction Fee", "difficulty": "Medium", "category": "DP - Multidimensional"},
    {"id": 72, "name": "Edit Distance", "difficulty": "Medium", "category": "DP - Multidimensional"},
    # Bit Manipulation
    {"id": 338, "name": "Counting Bits", "difficulty": "Easy", "category": "Bit Manipulation"},
    {"id": 136, "name": "Single Number", "difficulty": "Easy", "category": "Bit Manipulation"},
    {"id": 1318, "name": "Minimum Flips to Make a OR b Equal to c", "difficulty": "Medium", "category": "Bit Manipulation"},
    # Trie
    {"id": 208, "name": "Implement Trie (Prefix Tree)", "difficulty": "Medium", "category": "Trie"},
    {"id": 1268, "name": "Search Suggestions System", "difficulty": "Medium", "category": "Trie"},
    # Intervals
    {"id": 435, "name": "Non-overlapping Intervals", "difficulty": "Medium", "category": "Intervals"},
    {"id": 452, "name": "Minimum Number of Arrows to Burst Balloons", "difficulty": "Medium", "category": "Intervals"},
    # Monotonic Stack
    {"id": 739, "name": "Daily Temperatures", "difficulty": "Medium", "category": "Monotonic Stack"},
    {"id": 901, "name": "Online Stock Span", "difficulty": "Medium", "category": "Monotonic Stack"},
]

SCRIPT_DIR = Path(__file__).parent
DATA_FILE = SCRIPT_DIR / "lc75_progress.json"


def load_progress() -> dict:
    """Load progress from JSON file."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"solved": []}


def save_progress(progress: dict) -> None:
    """Save progress to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def generate_problem() -> None:
    """Generate a random unsolved problem."""
    progress = load_progress()
    solved_ids = set(progress["solved"])
    unsolved = [p for p in LEETCODE_75 if p["id"] not in solved_ids]
    
    if not unsolved:
        print("🎉 Congratulations! You've solved all LeetCode 75 problems!")
        return
    
    problem = random.choice(unsolved)
    remaining = len(unsolved)
    
    print(f"\n{'='*60}")
    print(f"📝 Problem #{problem['id']}: {problem['name']}")
    print(f"{'='*60}")
    print(f"   Category:   {problem['category']}")
    print(f"   Difficulty: {problem['difficulty']}")
    print(f"   URL:        https://leetcode.com/problems/{problem['name'].lower().replace(' ', '-').replace('(', '').replace(')', '')}/")
    print(f"{'='*60}")
    print(f"   Remaining:  {remaining}/{len(LEETCODE_75)} problems")
    print(f"\n   After solving, run: python lc75.py solve {problem['id']}")
    print()


def solve_problem(problem_id: int) -> None:
    """Mark a problem as solved."""
    problem = next((p for p in LEETCODE_75 if p["id"] == problem_id), None)
    
    if not problem:
        print(f"❌ Problem #{problem_id} is not in LeetCode 75 list.")
        return
    
    progress = load_progress()
    if problem_id in progress["solved"]:
        print(f"ℹ️  Problem #{problem_id} ({problem['name']}) is already marked as solved.")
        return
    
    progress["solved"].append(problem_id)
    save_progress(progress)
    
    remaining = len(LEETCODE_75) - len(progress["solved"])
    print(f"✅ Marked #{problem_id} ({problem['name']}) as solved!")
    print(f"   Remaining: {remaining}/{len(LEETCODE_75)} problems")


def show_status() -> None:
    """Show current progress."""
    progress = load_progress()
    solved_count = len(progress["solved"])
    total = len(LEETCODE_75)
    percentage = (solved_count / total) * 100
    
    print(f"\n📊 LeetCode 75 Progress")
    print(f"{'='*40}")
    print(f"   Solved:    {solved_count}/{total} ({percentage:.1f}%)")
    print(f"   Remaining: {total - solved_count}")
    
    # Progress bar
    bar_width = 30
    filled = int(bar_width * solved_count / total)
    bar = "█" * filled + "░" * (bar_width - filled)
    print(f"   [{bar}]")
    print()


def list_problems() -> None:
    """List all problems with their status."""
    progress = load_progress()
    solved_ids = set(progress["solved"])
    
    current_category = None
    for problem in LEETCODE_75:
        if problem["category"] != current_category:
            current_category = problem["category"]
            print(f"\n📁 {current_category}")
            print("-" * 50)
        
        status = "✅" if problem["id"] in solved_ids else "⬜"
        diff_emoji = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}[problem["difficulty"]]
        print(f"   {status} {problem['id']:4d}. {problem['name']} {diff_emoji}")
    
    print()


def reset_progress() -> None:
    """Reset all progress."""
    save_progress({"solved": []})
    print("🔄 Progress has been reset.")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    command = sys.argv[1].lower()
    
    if command == "generate" or command == "g":
        generate_problem()
    elif command == "solve" or command == "s":
        if len(sys.argv) < 3:
            print("❌ Please provide a problem ID: python lc75.py solve <id>")
            return
        try:
            problem_id = int(sys.argv[2])
            solve_problem(problem_id)
        except ValueError:
            print("❌ Invalid problem ID. Please provide a number.")
    elif command == "status":
        show_status()
    elif command == "list" or command == "l":
        list_problems()
    elif command == "reset":
        confirm = input("Are you sure you want to reset all progress? (y/N): ")
        if confirm.lower() == "y":
            reset_progress()
        else:
            print("Reset cancelled.")
    else:
        print(f"❌ Unknown command: {command}")
        print(__doc__)


if __name__ == "__main__":
    main()
