#!/usr/bin/python3
def safe_print_division(a, b):
    r = 0
    try:
        r = a / b
    except Exception:
        return None
    finally:
        return r
