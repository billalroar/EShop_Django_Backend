from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=15,null=True)
    email= models.EmailField()
    password = models.CharField(max_length=500,null=True)
    address=models.CharField(max_length=500,null=True)
    city=models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    zip = models.CharField(max_length=100,null=True)

    def register(self):
        self.save()
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except :
            return False

            

    def isExists(self):
        if Customer.objects.filter(email= self.email):
            return True
        else:
            return False


