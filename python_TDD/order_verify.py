
pending_orders =[]
delivered_orders =[2]


def check_order_status(order_id):

 if order_id in delivered_orders:
   return True
 else:
   return False