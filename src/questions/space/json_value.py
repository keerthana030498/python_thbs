class DNS:
    def __init__(self,domain):
        self.domain = domain

class Amazon(DNS):
    def __init__(self,domain):
        super().__init__(domain)
    def get_amazon_url(self):
        return f"{self.domain}/amazon"

class Flipkart(DNS):
    def __init__(self,domain):
        super().__init__(domain)
    def get_Flipkart_url(self):
        return f"{self.domain}/Flipkart"

amazon1 = Amazon("google.com")
print(amazon1.get_amazon_url())

# it is defined as the first parameter of the instance methods in a class
#used to access atributes and methods of the class
#refer to the instance of the class from which method is being called
