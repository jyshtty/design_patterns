from Adapter.Adapters.YesBankAdapter import YesBankAdapter
from Adapter.Payment import Payment

if __name__ == "__main__":
    b = YesBankAdapter()
    p = Payment(b)
    print(type(p.checkBalance()))
