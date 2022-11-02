from typing import Dict, List


class ATM:

    def __init__(self, list_denominations: List[int] = [1, 2, 5], amt: int = 0) -> None:
        self.list_denominations = list_denominations
        # The sort the list in the desc. order
        self.list_denominations.sort(reverse=True)
        assert amt >= 0, "Amount can not negative number"
        self.amt = amt

        # key is string denomination and value is the number of each denomination notes
        self.denominations = {}

    def depense(self) -> Dict[str, int]:
        amt = self.amt
        for i in self.list_denominations:
            # print(i, self.list_denominations)
            # assert i != 0, ZeroDivisionError  # "Zero Division Error"
            try:
                num = amt // i
                rem = amt - num * i
            except ZeroDivisionError:
                print(f'Denomination {i} is zero')

            if rem == 0:
                self.denominations[str(i)] = num
                break
            else:
                if num != 0:
                    self.denominations[str(i)] = num
                amt = rem
                continue
        return self.denominations

    def get_amt_by_denominations(self, amtDict: Dict[str, int]) -> Dict[str, int]:
        for i in amtDict.keys():
            self.amt += amtDict[i] * int(i)
        return self.depense()

    @staticmethod
    def present(dict: Dict[str, int]):
        for i in dict.keys():
            print(f'{dict[i]} note(s) of GHS {i} ')


# denominations = {}
# list_denominations = [1, 2, 5]
# amt = 111

# atm = ATM(list_denominations=list_denominations, amt=amt)
# print("Class Base: ", atm.depense())
