# cars = {"Maruti": "Ciaz", "Hyundai": "Verna",
#         "Honda": "City", "Toyota": "Corolla", "Tata": "Nexon"}
# cars2 = {key: value for key, value in cars.items()}
# print(cars2)


# dist1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# dist2 = {key: 2*value for key, value in dist1.items()}
# print(dist2)

# dist3 = {key*2: value for key, value in dist1.items()}
# print(dist3)


# str = "WE LOVE INDIA"
# dist1 = {char: str.count(char) for char in str}
# for key, value in dist1.items():
#     print(f"{key} : {value}")


dist1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
         "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}
dist2 = {key: value for key, value in dist1.items() if value >
         2 if value % 2 == 0}
print(dist2)
