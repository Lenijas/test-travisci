#!/usr/bin/env python
# coding=UTF-8
import sys
import pytest


# content of test_assert1.py
def f():
    return 3

def test_function():
    assert f() == 3


test_function()
sys.exit(0)
