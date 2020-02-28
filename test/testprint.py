import sys
import os
import pytest

def printa():
  a="hello,world"
  return a

def test_printa():
  c="hello,world"
  b=printa()
  assert b==c
