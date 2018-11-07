import unittest
from order_verify import check_order_status

class TestOrder(unittest.TestCase):
    def test_order_status(self):
      self.assertEqual(check_order_status(2),True)

    # def test_id_is_integer(self):
    #   self.assertTrue(id_is_integer(2) )




    # def check_order_status(order_id):
     # C:\Users\joan\Desktop\Python_OOP\python_oop\order_verify.py