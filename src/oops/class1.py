class DNS:
    def __init__(self,domain):
        self.domain = domain

    def validate(self):
        if self.domain != "google.com":
            return "wrong domain name"
        else:
            return None

class Amazon(DNS):
    def __init__(self,domain):
        super().__init__(domain)

    def getamazonurl(self):
        validationerror = self.validate()
        if validationerror:
            return validationerror
        else:
            return f"{self.domain}/amazon"



class Flipkart(DNS):
    def __init__(self,domain):
        super().__init__(domain)

    def getflipkarturl(self):
        validationerror = self.validate()
        if validationerror:
            return validationerror
        else:
            return f"{self.domain}/flipkart"


amaozn1 = Amazon("google.com")
print("amazon url is ",amaozn1.getamazonurl())
flipkart1 = Flipkart("july.com")
print("flipkart url is ",flipkart1.getflipkarturl())
