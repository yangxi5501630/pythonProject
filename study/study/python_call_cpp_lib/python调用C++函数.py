from ctypes import *
import sys,os

handle = CDLL("./libadd.so")

if __name__ == "__main__":
    print(handle.add(100, 200))
    print(handle.sub(100, 200))

    handle.mul.restype = c_float
    a = c_float(1.2)
    b = c_float(1.2)
    print(handle.mul(a, b))

