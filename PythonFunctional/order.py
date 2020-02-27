class Order:
    # class attribute
    orders = []

    # instance attributes
    orderid = 0
    shipping_address = ''
    expedited = False
    shipped = False
    customer = None

    @staticmethod
    def test_expedited(order):
        return order.expedited

    @staticmethod
    def test_not_expedited(order):
        return not order.expedited

    @staticmethod
    def get_customer_name(order):
        return order.customer.name
    
    




# // OLD CODE 

    # def get_expedited_orders_customer_names(self):
    #     output = []
    #     for order in Order.orders:
    #         if order.expedited:
    #             output.append(order.customer.name)
    #     return output

    
    # def get_expedited_orders_customer_addresses(self):
    #     output = []
    #     for order in Order.orders:
    #         if order.expedited:
    #             output.append(order.customer.address)
    #     return output


    # def get_expedited_orders_shipping_addresses(self):
    #     output = []
    #     for order in Order.orders:
    #         if order.expedited:
    #             output.append(order.shipping_address)
    #     return output
