class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # return true if every customer satisy and if not then return 0
        money = {}
        # bills.sort()
        i = 0

        def checkMoney(money,pending):
            if pending == 15:
                if money.get(10,0)>0 and money.get(5,0)>0:
                    money[10] = money.get(10,0) - 1
                    # money[10] -= 1
                    money[5] = money.get(5,0) - 1
                    return True
                if money.get(10,0) == 0 and money.get(5,0)>=3:
                    money[5] = money.get(5,0) - 3
                    return True
            if pending == 5:
                if money.get(5,0)>0:
                    money[5] = money.get(5,0) - 1
                    return True
            return False


        while i < len(bills):
            get_money = bills[i]
            pending_money = bills[i] - 5
            money[get_money] = money.get(get_money,0) + 1
            if pending_money != 0:
                temp = checkMoney(money,pending_money)
                if not temp:
                    return False
            i += 1

        return True
          
