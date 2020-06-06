# convert temperature to and from Celsius (C) or Fahrenheit (F)
# 2 Equations; C = (5(F-32))/9 and F = (9C + (32*5))/5
# User would input say 55C, 131F or even 55c
# Express your result to the nearest one unit (No decimal value) using round()

temp = input("Enter the temperature to convert? (eg. 55C, 131F, etc) : ")
degree = int(temp[:-1]) #get digits
method = str(temp[-1])  #get last alphabet


