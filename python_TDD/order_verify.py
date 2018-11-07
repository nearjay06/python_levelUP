
pending_orders =[]
delivered_orders =[2]


def check_order_status(order_id):

 if order_id in delivered_orders:
   return True
 else:
   return False

def add_new_order(order_id):
  if order_id in pending_orders:
    return "order_id exists"
  else:
    pending_orders.append(order_id)
  return "order has been added"

def order_marked_delivered (order_id):
  if order_id in delivered_orders:
    return 'order delivered'
  else:
    return 'order pending'

def order_id_not_in_both_lists(order_id):
  if order_id not in delivered_orders and pending_orders:
    return True
  else:
    return False

def orders_added_to_the_list(order_id):
  for order_id in  pending_orders:
    pending_orders.append(order_id)
    return True
  else:
    return False