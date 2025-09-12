import matplotlib.pyplot as plt

# ---------- 1. Pie Chart ----------
departments = ["IT", "HR", "Finance", "Marketing"]
employees = [40, 25, 20, 15]

plt.figure(figsize=(6, 6))
plt.pie(employees, labels=departments, autopct="%.1f%%", startangle=140,
        colors=["skyblue", "lightgreen", "orange", "pink"],
        explode=[0.05, 0, 0, 0])
plt.title("Employee Distribution by Department")
plt.show()


# ---------- 2. Stack Plot ----------
years = [2018, 2019, 2020, 2021, 2022]
product_A = [10, 20, 30, 40, 50]
product_B = [5, 15, 25, 35, 45]
product_C = [2, 10, 20, 30, 40]

plt.figure(figsize=(8, 5))
plt.stackplot(years, product_A, product_B, product_C,
              labels=["Product A", "Product B", "Product C"],
              colors=["skyblue", "lightcoral", "lightgreen"])
plt.title("Product Sales Over Years (Stack Plot)")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend(loc="upper left")
plt.show()


# ---------- 3. Horizontal Bar Chart ----------
countries = ["Bangladesh", "India", "USA", "UK", "Canada"]
population = [170, 1400, 330, 67, 39]   # in millions

plt.figure(figsize=(8, 5))
plt.barh(countries, population, color="purple")
plt.title("Population Comparison")
plt.xlabel("Population (millions)")
plt.ylabel("Countries")
plt.show()
# ---------- Task ----------
departments = ["IT", "HR", "Finance", "Marketing", "R&D"]
employees = [50, 30, 40, 20, 10]
plt.figure(figsize=(6, 8))
plt.pie(employees, labels=departments, autopct="%.1f%%", startangle=140,
        colors=["skyblue", "lightgreen", "orange", "pink", "lightgray"],
        explode=[0, 0, 0, 0.1, 0])  
plt.title("Employee Distribution by Department")
plt.show()

years = [2019, 2020, 2021, 2022, 2023]
product_X = [15, 25, 35, 45, 55]
product_Y = [10, 20, 30, 40, 50]
product_Z = [5, 15, 25, 30, 35]
plt.figure(figsize=(8, 5))
plt.stackplot(years, product_X, product_Y, product_Z,
              labels=["Product X", "Product Y", "Product Z"],
              colors=["skyblue", "lightcoral", "lightgreen"])
plt.title("Product Sales Over Years (Stack Plot)")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend(loc="upper left")
plt.show()
countries = ["Bangladesh", "India", "China", "USA", "UK"]
population = [170, 1400, 1440, 330, 68]
plt.figure(figsize=(8, 5))
plt.barh(countries, population, color="teal")
plt.title("Population Comparison")
plt.xlabel("Population (millions)")
plt.ylabel("Countries")
plt.show()
# ---------- End of Task ----------
