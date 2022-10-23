#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:46:41 2022
 Project: Macro tracker
 By Sheridan Yates
 This program will be able to take in food calculations for your daily 
 intake basked on Carb, Prot, and Fats to comapare to your current macro goal.
@author: Admin
"""
import math as m
import numpy as np

def BMR(W,H,A,S):
    if(S == 2):
        return (665.1 + (9.563 + W) + (1.850  * H) - (4.676 * A))
    elif(S == 1):
        return (66.47 + (13.75 * W) + (5.003  * H) - (6.755 * A))
    else:
        return 'Error'
def Height(a,b):
    return (((a * 12) + b) * 2.54)

def Weight(a):
    return (a / 2.2)
   
bwkg = float(input('Please enter bodyweight in pounds\n'))    
'''bwn = float(bw)'''
''''bwkg = bwn / 2.2'''
W = Weight(bwkg)
   

   
protienl = round(W * 1.2)
protienh = round(W * 2)
carbl = round(W * 5)
carbh = round(W * 8)
fatl = round(W * .4)
fath = round(W * .5)

calories_in_protien = 4
calories_in_fat = 9
calories_in_carbs = 4
      
protien_cal_low = protienl * calories_in_protien
protien_cal_high = protienh * calories_in_protien
      
carb_cal_low = carbl * calories_in_carbs
carb_cal_high = carbh * calories_in_carbs
      
fat_cal_low = fatl * calories_in_fat
fat_cal_high = fath * calories_in_fat
      
      
total_calories_low = (protien_cal_low + carb_cal_low + fat_cal_low)
total_calories_high = (protien_cal_high + carb_cal_high + fat_cal_high)
      
print('For your body weight at ' + str(bwkg) + ' your low to high end macros would be:')
print('Protien: ' + str(protienl) + 'g - ' + str(protienh) +'g')
print('Carbohydrate: ' + str(carbl) + 'g - ' + str(carbh) +'g')
print('Fats: ' + str(fatl) + 'g - ' + str(fath)+'g')
print('Total calories are ' + str(total_calories_low) + ' - ' + str(total_calories_high))

print(' How many grams of Protien, Carbs, and fats have you had so far today?\n ')
cprotien = float(input('Protien:\n'))
ccarb = float(input('Carb:\n'))
cfat = float(input('Fat:\n'))
print('\n')
      
protien_left_low = round(protienl - cprotien)
protien_left_high = round(protienh - cprotien)
      
carb_left_low = round(carbl - ccarb)
carb_left_high = round(carbh - ccarb)

fat_left_low = round(fatl - cfat)
fat_left_high = round(fath - cfat)
      
cp_calories = cprotien * calories_in_protien
cc_calories = ccarb * calories_in_carbs
cf_calories = cfat * calories_in_fat
    
current_calories = (cp_calories + cc_calories + cf_calories)
      
calories_left_low = total_calories_low - current_calories
calories_left_high = total_calories_high - current_calories
      
print('Your total calories left for today: ' + str(calories_left_low) + ' - ' + str(calories_left_high))

print('Your Macros left for today are:')

if (protien_left_low > 0):
    print('Protien: ' + str(protien_left_low) + 'g - ' + str(protien_left_high) +'g')
     
elif(protien_left_high < 0):
    print('You hit your protien goal')
else:
    print('Protien: ' + str(protien_left_high) +'g')

if (carb_left_low > 0):
    print('Carbohydrate: ' + str(carb_left_low) + 'g - ' + str(carb_left_high) +'g')
elif(carb_left_high < 0):
    print('You hit your Caarbohydrate goal')
else:
    print('Carbohydrate: ' + str(carb_left_high) +'g')
         
if (fat_left_low > 0):
    print('Fats: ' + str(fat_left_low) + 'g - ' + str(fat_left_high) +'g')
           
elif(fat_left_high < 0):
    print('You hit your Fat goal')
else:
    print('Fats: ' + str(fat_left_high) +'g')

print(' What is height in feet and inches ')
a = float(input('Feet: '))
b = float(input('Inches:'))
H = Height(a, b)
      
print(' What is your sex? ')
print(' 1 for Male')
S = int(input (' 2 for Famle\n'))

A = float(input('What is your age? '))   

bmr = BMR(W, H, A, S)
print(' Your BMR is: ' + str(bmr))

if (bmr > current_calories):
    minus = current_calories - bmr
    print(' You are eating in a surplus by ' + str(minus))
        
elif(bmr < current_calories):
    plus = current_calories - bmr
    print(' You are eating in a surplus by ' + str(plus))
        
else:
    print(' Your are eatting at maintanence ') + str(current_calories)


    