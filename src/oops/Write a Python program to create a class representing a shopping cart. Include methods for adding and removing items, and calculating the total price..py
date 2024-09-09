class shoppingCart:
    def __init__(self):
        self.cart = []
    def addItems(self,item_name,qty):
        item = (item_name,qty)
        self.cart.append(item)
        return self.cart
    def removeItems(self,item_name,qty):
        for item in self.cart:
            if item[0] == item_name:
                self.cart.remove(item)
        return self.cart
    def totalitems(self):
        total = 0
        for item in self.cart:
            total +=item[1]
        return total

carts = shoppingCart()
print(carts.addItems("brush",2))
print(carts.addItems("sugar",3))
print(carts.addItems("dal",1))
print(carts.addItems("bottle",10))
print(carts.totalitems())
print(carts.removeItems("bottle",10))

