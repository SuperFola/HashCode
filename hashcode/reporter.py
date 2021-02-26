#!/usr/bin/env python3
# coding: utf-8

import time
import os
import psutil


DEBUG = True


def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss


def reporter(name: str):
    """reporter decorator
    Args:
        name (str): [description]
    """
    def inner(func):
        def wrapper(*args, **kwargs):
            mem_before = get_process_memory()
            start = time.perf_counter()
            out = func(*args, **kwargs)
            end = time.perf_counter()
            mem_after = get_process_memory()

            if DEBUG:
                print(f"|____{name} took {(end - start) * 1000:0.3f} ms")
                print(f"     |____ memory consumed: {mem_after - mem_before}")
            return out
        return wrapper
    return inner
