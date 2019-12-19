# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 08:01:06 2019

@author: karol
"""

from numba import jit, int64
import numpy as np


@jit(int64(int64[:], int64[:], int64, int64, int64), nopython=True, cache=True)
def merge_2(arr, temp, left, mid, right):
    inv_count = 0
    idL = left
    idR = mid+1
    idO = left

    while idL <= mid and idR <= right:
        if arr[idL] <= arr[idR]:
            temp[idO] = arr[idL]
            idL += 1
        else:
            inv_count += mid + 1 - idL
            temp[idO] = arr[idR]
            idR += 1
        idO += 1

    while idL <= mid:
        temp[idO] = arr[idL]
        idL += 1
        idO += 1

    while idR <= right:
        temp[idO] = arr[idR]
        idR += 1
        idO += 1

    i = left
    while i <= right:
        arr[i] = temp[i]
        i += 1

    return inv_count


@jit(int64(int64[:], int64[:], int64, int64), nopython=True, cache=True)
def cir_2(arr, temp, left, right):
    mid = 0
    inv_count = 0
    if right > left:
        mid = (right+left) // 2
        inv_count += cir_2(arr, temp, left, mid)
        inv_count += cir_2(arr, temp, mid+1, right)
        inv_count += merge_2(arr, temp, left, mid, right)
    return inv_count


def count_inversions_2(arr):
    sl = len(arr)
    temp = [0 for i in range(sl)]
    arr_np = np.array(arr, dtype=np.int64)
    temp_np = np.array(temp, dtype=np.int64)
    return cir_2(arr_np, temp_np, 0, sl-1)
