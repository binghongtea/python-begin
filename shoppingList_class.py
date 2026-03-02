class ShoppingList :
    def __init__(self, shoppingList):
        self.shoppingList = shoppingList

    def get_item_count(self):
        return len(self.shoppingList)

    def get_item_total(self):
        total = 0
        for price in self.shoppingList.values():
            total += price
        return total