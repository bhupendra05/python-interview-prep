#!/usr/bin/env python3
"""
python-interview-prep CLI
Run and test individual problems from the command line.

Usage:
    python cli.py list
    python cli.py run arrays two_sum
    python cli.py test arrays
    python cli.py test all
"""
import importlib
import inspect
import sys
import time
from pathlib import Path

CATEGORIES = ["arrays", "strings", "trees", "graphs", "dynamic_programming", "sorting_searching"]

SAMPLE_INPUTS = {
    "two_sum": (([2, 7, 11, 15], 9), [0, 1]),
    "max_profit": (([7, 1, 5, 3, 6, 4],), 5),
    "contains_duplicate": (([1, 2, 3, 1],), True),
    "max_subarray": (([-2, 1, -3, 4, -1, 2, 1, -5, 4],), 6),
    "is_anagram": (("anagram", "nagaram"), True),
    "is_palindrome": (("A man, a plan, a canal: Panama",), True),
    "climb_stairs": ((10,), 89),
    "coin_change": (([1, 5, 11], 15), 3),
    "rob": (([2, 7, 9, 3, 1],), 12),
}


def list_problems():
    print("\nAvailable problem categories:\n")
    for cat in CATEGORIES:
        try:
            mod = importlib.import_module(f"solutions.{cat}.problems")
            funcs = [name for name, obj in inspect.getmembers(mod, inspect.isfunction)
                     if not name.startswith("_")]
            print(f"  📂 {cat}/")
            for f in funcs:
                print(f"     • {f}")
        except ImportError:
            print(f"  📂 {cat}/ (no problems yet)")
    print()


def run_problem(category: str, problem: str):
    try:
        mod = importlib.import_module(f"solutions.{category}.problems")
    except ImportError:
        print(f"Category '{category}' not found.")
        sys.exit(1)

    func = getattr(mod, problem, None)
    if not func:
        print(f"Problem '{problem}' not found in '{category}'.")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"Problem: {problem}")
    print(f"Category: {category}")
    print(f"{'='*60}")
    if func.__doc__:
        print(func.__doc__)

    if problem in SAMPLE_INPUTS:
        args, expected = SAMPLE_INPUTS[problem]
        print(f"\nSample Input: {args}")
        start = time.perf_counter()
        result = func(*args)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"Output:       {result}")
        print(f"Expected:     {expected}")
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Status:       {status}  ({elapsed:.3f}ms)")
    else:
        print("\n(No sample input defined — add to SAMPLE_INPUTS in cli.py)")


def test_category(category: str):
    passed = failed = 0
    tests = {k: v for k, v in SAMPLE_INPUTS.items()}

    if category == "all":
        cats = CATEGORIES
    else:
        cats = [category]

    for cat in cats:
        try:
            mod = importlib.import_module(f"solutions.{cat}.problems")
        except ImportError:
            continue

        for func_name, (args, expected) in tests.items():
            func = getattr(mod, func_name, None)
            if not func:
                continue
            try:
                result = func(*args)
                if result == expected:
                    print(f"  ✅ {cat}.{func_name}")
                    passed += 1
                else:
                    print(f"  ❌ {cat}.{func_name}  (got {result}, expected {expected})")
                    failed += 1
            except Exception as e:
                print(f"  💥 {cat}.{func_name}  ERROR: {e}")
                failed += 1

    print(f"\n{passed} passed, {failed} failed")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "list":
        list_problems()
    elif args[0] == "run" and len(args) >= 3:
        run_problem(args[1], args[2])
    elif args[0] == "test":
        cat = args[1] if len(args) > 1 else "all"
        test_category(cat)
    else:
        print(__doc__)
