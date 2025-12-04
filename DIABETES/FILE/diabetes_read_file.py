import pandas as pd

# Original 20-row dataset
data = {
    "Name": ["Rahul", "Shyam", "Anjali", "Pooja", "Rohit","Sneha", "Aman", "Riya", "Karan", "Meera",
             "Arjun", "Neha", "Mohit", "Tara", "Kabir","Isha", "Vikram", "Simran", "Aditya", "Diya"],
    "Age": [25,34,42,29,51,37,46,28,33,40,31,38,45,27,50,36,43,30,48,39],
    "Gender": ["Male", "Female", "Male", "Female", "Male","Female", "Male", "Female", "Male", "Female",
               "Male", "Female", "Male", "Female", "Male","Female", "Male", "Female", "Male", "Female"],
    "Glucose": [85, 120, 140, 95, 160, 110, 130, 90, 100, 125, 135, 105, 145, 92, 155, 115, 138, 98, 150, 108],
    "Hba1c": [5.5, 6.1, 7.0, 5.8, 7.5, 6.3, 7.2, 5.7, 6.0, 6.8, 7.1, 6.5, 7.3, 5.9, 7.4, 6.2, 7.0, 5.6, 7.1, 6.4],
    "Diabetes": ["No","No","Yes","No","Yes","No","Yes","No","No","Yes","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No"],
    "Smoking": ["No","Yes","No","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No"],
    "Exercise": ["Low","Medium","High","Low","Medium","High","Low","Medium","High","Low","Medium","High","Low","Medium","High","Low","Medium","High","Low","Medium"],
    "BP": [120, 130, 140, 125, 150, 135, 145, 128, 132, 138, 142, 134, 148, 126, 152, 136, 144, 129, 149, 133],
    "Cholesterol": [180, 200, 220, 190, 240, 210, 230, 185, 195, 215, 225, 205, 235, 188, 245, 212, 232, 192, 238, 208],
    "BMI": [22, 25, 28, 23, 30, 26, 29, 24, 27, 28, 29, 25, 30, 23, 31, 26, 29, 24, 30, 25],
    "Alcohol": ["Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No"],
    "Diet": ["Veg","Non-Veg","Vegan","Veg","Non-Veg","Vegan","Veg","Non-Veg","Vegan","Veg","Non-Veg","Vegan","Veg","Non-Veg","Vegan","Veg","Non-Veg","Vegan","Veg","Non-Veg"],
    "Stress": ["Low","Medium","High","Low","Medium","High","Low","Medium","High","Low","Medium","High","Low","Medium","High","Low","Medium","High","Low","Medium"],
    "Sleep": [7,6,5,8,6,7,5,8,6,7,5,8,6,7,5,8,6,7,5,8],
    "Family_History": ["Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No"],
    "Waist": [80,85,90,82,88,91,87,83,89,86,92,84,90,81,93,85,88,82,91,87],
    "Hip": [95,100,105,97,103,106,101,98,104,102,107,99,105,96,108,101,103,97,106,102],
    "Heart_Rate": [70,75,80,72,78,82,76,73,79,77,81,74,83,71,84,75,80,72,82,76],
    "Vitamin_D": [20,25,30,22,28,32,26,23,29,27,31,24,33,21,34,25,30,22,32,26]
}
# Convert to DataFrame
df = pd.DataFrame(data)
x=pd.read_csv("diabetes.csv")
print(x)