print("BMI Calculator 2.0")

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height2 = height ** 2
bmi = weight / height2
rounded_bmi = round(bmi)
string_bmi = str(rounded_bmi)
bmi_is = "Your BMI is "

class color:
  BOLD = '\033[1m'
  END = '\033[0m'

if bmi < 18.5:
  print(bmi_is + string_bmi + "," + " you are " + color.BOLD  + "underweight" + color.END)
elif bmi < 25:
  print(bmi_is + string_bmi + "," + " you have a " + color.BOLD + "normal weight." + color.END)
elif bmi < 30:
  print(bmi_is + string_bmi + "," + " you are " + color.BOLD + "slightly overweight." + color.END)
elif bmi < 35:
  print(bmi_is + string_bmi + "," + " you are " + color.BOLD + "obese." + color.END)
else:
  print(bmi_is + string_bmi + "," + " you are " + color.BOLD + "clinically obese." + color.END) 

