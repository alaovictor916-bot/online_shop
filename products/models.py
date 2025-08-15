from django.db import models
from django.shortcuts import redirect
from django.urls import reverse

# Create your models here.
def comma(b):
  m= str(b)
  a =list(m)
  c =len(a)
  comma_posi=[]
  i =1
  while i <= c :
          n =-i
          comma_posi.append(a[n])
          if  i%3==0 :
                  comma_posi.append(',')
          i+= 1
  comma2 = comma_posi.reverse() 
  

  final_comma =''.join(comma_posi)
  return(final_comma)


class Product(models.Model):
    title = models.TextField()
    description = models.TextField(default='this is cool')
    image = models.ImageField(upload_to='product/images')
    price = models.DecimalField(max_digits=1000 , decimal_places=2)
    quantity_avail = models.DecimalField(max_digits=1000000000 , decimal_places=0 , default =1) 
    quantity_cart = models.DecimalField(max_digits=1000000000 , decimal_places=0 ,default=0) 

 
    def get_absolute_url(self):
        return reverse('detail_view' , kwargs={'id' : self.id})
    def purchase_url(self):
        return reverse('cart' , kwargs={'id' : self.id})
    def comma_price(self):
         nw = self.price
         c =int(nw)

         if len(str(c))>3:
           now =comma(c)
           return now
         else :
              
              return nw
    def cart_decrease(self) :
         self.quantity_cart -=1
         self.save()

    def cart_increase(self):
         self.quantity_cart +=1
         self.save()
         
      

        

