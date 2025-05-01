from Stratergy_Pattern.Strategy.BubbleSort import BubbleSort
from Stratergy_Pattern.Strategy.MergeSort import MergeSort
from Stratergy_Pattern.Strategy.QuickSort import QuickSort


class SortingFactory:
    @staticmethod
    def getSortingObj(algo):
        if algo == "Bubble Sort":
            return BubbleSort()
        if algo == "Quick":
            return QuickSort()
        if algo == "Merge":
            return MergSort()
