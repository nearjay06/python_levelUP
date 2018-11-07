import unittest
from order_verify import check_order_status,add_new_order,order_marked_delivered,check_order_status
from order_verify import order_id_not_in_both_lists,orders_added_to_the_list,pending_orders

class TestOrder(unittest.TestCase):
    def test_order_status(self):
      self.assertEqual(check_order_status(2),True)

    def test_id_is_integer(self):
      self.assertTrue(check_order_status(2),int )

    def test_order_id_does_not_exist_in_both_lists(self):
       self.assertEqual(order_id_not_in_both_lists(2),False)
       
    def test_if_orders_added_to_the_list(self):
       self.assertEqual(orders_added_to_the_list(65),True)
       self.assertIn(65,pending_orders)

    def test_add_new_order(self):
      self.assertTrue(add_new_order(3))
      
    def test_mark_order_delivered(self):
       self.assertTrue(order_marked_delivered(2))

    def check_order_id_status(self):
      self.assertEqual(check_order_status(2), True)
      

      
      
      unittest.main()