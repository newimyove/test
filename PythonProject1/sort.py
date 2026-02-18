import random
import time


class Sort:

    def __init__(self, n):
        self.arr = [0] * n
        self.len = n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0, 99)

    def partition(self, left, right):
        k = i = left
        while k < right:
            if self.arr[k] < self.arr[right]:
                self.arr[k], self.arr[i] = self.arr[i], self.arr[k]
                i += 1
            k += 1
        self.arr[i], self.arr[right] = self.arr[right], self.arr[i]
        return i

    def quick_sort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def adjust_max_heap(self, pos, arr_len):
        parent = pos
        child = 2 * parent + 1
        while child < arr_len:
            if child + 1 < arr_len and self.arr[child] < self.arr[child + 1]:
                child += 1
            if self.arr[child] > self.arr[parent]:
                self.arr[child], self.arr[parent] = self.arr[parent], self.arr[child]
                parent = child
                child = child * 2 + 1
            else:
                break

    def heap_sort(self):
        for i in range(self.len // 2 - 1, -1, -1):
            self.adjust_max_heap(i, self.len)
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        for arr_len in range(self.len - 1, 1, -1):
            self.adjust_max_heap(0, arr_len)
            self.arr[0], self.arr[arr_len - 1] = self.arr[arr_len - 1], self.arr[0]

    def use_time(self, sort_function,*args):
        start = time.time()
        sort_function(*args)
        end=time.time()
        print(f'the total time of this function is {end-start}s')

if __name__ == '__main__':
    # my_sort = Sort(10000)
    # # print(my_sort.arr)
    # # my_sort.quick_sort(0,9)
    # start = time.time()
    # my_sort.heap_sort()
    # end = time.time()
    # # print(my_sort.arr)
    # print(end - start)
    # my_sort.use_time(my_sort.quick_sort,0,10000-1)
    # list1=[22,11,2,67,90,13]
    # list2=[22,11,2,67,90,13]

    # Python自带排序

    # print(sorted(list1))
    # print(list1)
    # print(list2.sort())
    # print(list2)

