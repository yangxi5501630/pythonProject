from ctypes import *
import sys, os

handle = CDLL("./libadd.so")

if __name__ == "__main__":
    print(handle.add(100, 200))
    print(handle.sub(100,200))
