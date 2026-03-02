import unittest
from shoppingList_class import ShoppingList

class TestShoppintList(unittest.TestCase):
    def test_get_item_count(self):
        shoppingList = ShoppingList({'苹果': 5, '香蕉': 3, 'orage': 2})
        self.assertEqual(shoppingList.get_item_count(), 3)
    
    def test_get_item_total(self):
        shoppingList = ShoppingList({'苹果': 5, '香蕉': 3, 'orage': 2})
        self.assertEqual(shoppingList.get_item_total(), 10)