#!/usr/bin/env python
# coding=UTF-8
import pytest
import sys


# content of test_assert1.py
def f():
    return 3

def test_function():
    assert f() == 4


test_function()
