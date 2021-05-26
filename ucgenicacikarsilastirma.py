# -*- coding: utf-8 -*-

"""

Üçgen iç açılarının karşılaştırılması

X,Y,Z


"""

X=int(input("1. Dereceyi giriniz: "))
Y=int(input("2. Dereceyi giriniz: "))
Z=int(input("3. Dereceyi giriniz: "))

if X+Y+Z!=180 :
    print("SONUÇ= Lütfen Üçgenin iç açılarını doğru giriniz.")
elif X>Y>Z:
  print("SONUÇ=",X,"'", ">", Y,"'", ">",  Z,"'" )
elif X>Z>Y:
  print("SONUÇ=",X, "°", ">", Z,"°", ">", Y,"°" ) 
elif Y>X>Z:
  print("SONUÇ=",Y, "°", ">", X,"°", ">", Z,"°" )
elif Y>Z>X:
  print("SONUÇ=",Y, "°", ">", Z, "°", ">", X, "°" )
elif Z>X>Y:
  print("SONUÇ=",Z, "°", ">", X, "°", ">", Y, "°" )  
elif Z>Y>X:
  print("SONUÇ=",Z, "°", ">", Y, "°", ">", X, "°" )  
elif X==Y==Z:
  print("SONUÇ=",X,"°", "=", Y,"°", "=",  Z,"°" )
elif X>Y==Z:
  print("SONUÇ=",X,"°", ">", Y,"°", "=",  Z,"°" )
elif Y>X==Z:
  print("SONUÇ=",Y, "°", ">", X,"°", "=", Z,"°" )  
elif Z>X==Y:
  print("SONUÇ=",Z, "°", ">", X, "°", "=", Y, "°" )    
else:
  print("Beklenmedik bir hata oluştu.Tekrar deneyiniz.")
  
input()
  
  

