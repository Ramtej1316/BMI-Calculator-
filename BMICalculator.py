print("BODY MASS INDEX CALCULATOR")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
BMI = weight / (height **2)
if  BMI < 18.5:
    print( "You are categorized as ->Underweight by :",BMI)
    
elif 18.5 <= BMI < 24.9:
    print( "You are categorized as -> Normal Weight by :",BMI)
elif 25 <= BMI < 29.9:
    print ("You are categorized as -> Overweight by :",BMI)
else:
    print("You are categorized as ->Obese by :",BMI)
    
