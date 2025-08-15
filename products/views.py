from django.shortcuts import render , redirect 
from .models import Product
from django.http import HttpResponse 
from .forms import Search_form , sell_form


# Create your views here.
def sing(gti):
 h = list(gti)
 
 if str(h[-1])=='s':
      h.pop()
      if str(h[-1])=='e':
         h.pop()
         if str(h[-1])=='i':
            h.pop()
 
 return ''.join(h)




def end(list):
   sep =[]
   i =1
   while i < len(list) :
      a = -i
      sep.append(list[a]) 
      if list[a] == ' ' :
          b =''.join(sep)
          search_end =''.join(reversed(b))
          print(search_end)
          return search_end
          
      i+=1



def begin(list):
   set =[]
   i=0
   while i < len(list):
      set.append(list[i])
      if list[i] == ' ' :
         z = ''.join(set)
         print(z)
         return(z)
      i +=1


def begin_correct(listi):
   a =begin(listi) 
   h= list(a)
   h.pop()
   if str(h[-1])=='s':
      h.pop()
      if str(h[-1])=='e':
         h.pop()
         if str(h[-1])=='i':
            h.pop()
   if str(h[-1])=='r' and str(h[-2])=='o' and str(h[-3])=='f' and len(h)==3 :
      h.pop()
      if str(h[-1])=='o':
         h.pop()
         if str(h[-1])=='f':
            h.pop()
   return ''.join(h)



def end_correct(listo):
   gti =end(listo)
   h = list(gti)

   print(h)
   if str(h[-1])=='s':
      h.pop(-1)
      if str(h[-1])=='e':
         h.pop()
         if str(h[-1])=='i':
            h.pop()
   if str(h[-1])=='r' and str(h[-2])=='o' and str(h[-3])=='f' and len(h)==3 :
      h.pop()
      if str(h[-1])=='o':
         h.pop()
         if str(h[-1])=='f':
            h.pop()
   return ''.join(h)






def space( b ,list):
   
   while b < len(list):
     if list[b] == ' '  :
      return b

     b+=1



i =0

def strin(i , f):
  while i<len(f):
    
    set=[]
    a = space(i ,f)
    if not a == None   :
       b =a+1
       x = space(b , f)
       if not x == None :
         
         for h in range((a+1) , x):
           
             set.append(f[h])
             
             if  h == x-1 and str(f[(x-1)]) =='s' :
               a =set.pop()
               print(f[(x-1)])
              
               if  str(f[x-2]) =='e' and h == x-1 and str(f[(x-1)]) =='s'  :
                 set.pop()
                 if str(f[x-3])=="i":
                   set.pop()
             if  h == x-1 and str(f[(x-2)]) =='i' :
                 set.pop()
             if   h == x-1 and str(f[(x-1)]) =='r'  and str(f[(x-2)]) =='o' and str(f[(x-3)]) =='f' :
               set.pop()
               set.pop()
               set.pop()
               

           
       v = ''.join(set)
       return v




    if not a ==None:
       i =a
    i+=1



def finallist( f):
 set1 =[]
 z=0
 while z < len(f) :
   
   q = strin(z , f)
   if not q ==None :
      set1.append(q)
   h =space(z , f)
   if not h==None:
      z=h
   z+=1
 return set1

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
  #the next line is specifically for the grandtotal in the cart to get rid of the persistent comma in front of the digits
  h =comma_posi.pop(0)

  final_comma =''.join(comma_posi)
  return(final_comma)

          

          

 



def search_view(request , *args , **kwargs):
  product =      Product.objects.all()
  n =      Product.objects.count()
  a = int( n/3 )
  x = Product.objects.filter(title__iendswith='board')
  y = Product.objects.filter(title__istartswith='c')
  form = Search_form(request.POST or None)
    
  if request.method == 'POST'  :
    if  form.is_valid():
      zx = form.cleaned_data
      search_st =zx.get('search')
      der =list(search_st)
      confirm = begin(der)
      if not confirm == None:
        h =form.cleaned_data
        print(h)
        search_string =h.get('search')
        lis=list(search_string)
        u = end_correct(lis)
        g=begin_correct(lis)
        m =g
        print(m  ,u)
        
        if not u ==None:
         ending = Product.objects.filter(title__icontains = u)
         
            
        if not m ==None :
          begin2 = Product.objects.filter(title__istartswith= m)
          print(begin2)
        
        print('this is from' , u , m , list(ending) )
        if not finallist(lis)==None:
           querry_set = []
           finset =finallist(lis) 
           for words in finset :
              if not words == 'for'  and not words =='and' and not words=='':
                 querry_set.append(Product.objects.filter(title__icontains=words))
        print(querry_set)
    
                 
                 
        
          
        contexto = {
           'productEnd' : ending ,
           'productBegin' : begin2 ,
           'querry_set_list' : querry_set
        }
        return render(request , 'all_view.html' , contexto )
      if confirm==None:
           h =form.cleaned_data
           print(h)
           search_string =h.get('search')
           gt =sing(search_string)
           crt = Product.objects.filter(title__icontains=gt)
           print(crt)
           if not crt.exists():
              return HttpResponse('<h>ITEM NOT AVAILABLE </h>')
         
           return render(request , 'all_view.html' , {'ultimate':crt})
      
        



    
    
  context ={
        'products' : product ,
        'one-third' :int( a) ,
        'total' : n ,
        'x' : x ,
        'y' : y ,
        'form' : form

    }

  return render(request , 'all_view.html' , context)

def product_detail_view(request , id):
    product = Product.objects.get(id = id)

    if request.method == "POST" :
       product.quantity_cart +=1
       product.save()
       a = product.purchase_url()
       b = product.get_absolute_url()
       print(a , b)
       return redirect(a)
            
    context ={
        'product' : product
    }
    return render(request , 'product_detail.html' , context)



def cart_view(request , id):
   product =Product.objects.get(id =id)
   price = int(product.quantity_cart) * int(product.price)
   all = Product.objects.all()
   products_incart =[]
   quan =[]
   for item in all:
      if int(item.quantity_cart) >0 :
          quan.append(float(item.quantity_cart))
          products_incart.append(item)
   price =[]
   
   for item in products_incart:
      pa =int(item.quantity_cart) * int(item.price)
      price.append(pa)
   grand_total = sum(price)
   grand_total_comma =comma(grand_total)
   

   print(request.user)
   print(quan)
   tre=int(sum(quan))
   
   



   context={"product" : product ,
            'price' : price ,
            'totalpl' :products_incart ,
            'big' : grand_total_comma ,
            'nrows' : tre

   }
   return render(request , 'cart.html' , context)

def seller_view(request, *args , **kwargs):
      form = sell_form(request.POST or None  )
      if request.method == 'POST' :
         form = sell_form(request.POST ,request.FILES)
         if form.is_valid() :
            form.save()
         
            form = sell_form()
      context ={'form':form

         }
      return render(request , 'sellpage.html' , context )