from Stratergy_Pattern.Factory.SortingFactory import SortingFactory

class Sorter:

    def sort_data(self, data, algo):
        print("Test")
        strategy = SortingFactory.getSortingObj(algo)
        strategy.sort(data)
