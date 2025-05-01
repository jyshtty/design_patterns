from .sorting import Sorting

class QuickSort(Sorting):
    def sort(self, data):
        data.sort()
        print("Quick sort")
        print(f"Sorted Data using quick sort {data}")

