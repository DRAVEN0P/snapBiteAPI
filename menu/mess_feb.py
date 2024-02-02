import copy as cp

class DailyMeals:
    def __init__(self,id,date, breakfast, lunch, dinner,snacks):
        self.id = id
        self.date = date
        self.breakfast = breakfast
        self.lunch = lunch
        self.snacks = snacks
        self.dinner = dinner

day1 = DailyMeals(
    id=1,
    date= ["2024-02-01"],
    breakfast=["Gobi Paratha, Curd,","Pongal, Chutney, Sambar","B,B,J", "Tea, Coffee, Milk,"],
    lunch=["Phulka", "Dal Masala", "White Rice", "Sambar", "Rasam" , "Curd", "Onion Rings", "Green Veg Sabzhi", "Sweet:Badushai / CoconutLaddu "],
    snacks=["Sweet Corn","Tea,Coffee,Milk"],
    dinner=["Poori", "White Rice", "Rasam", "Sambar", "Loose Curd", "Jeera Rice", "Poriyal", "Fruits : Banana"]
)
day15 = cp.copy(day1)
day15.date = "2024-02-15",
day15.id = 15
day29 = cp.copy(day1)
day29.date ="2024-02-29",
day29.id = 29

day2 = DailyMeals(
    id=2,
    date=["2024-02-02"],
    breakfast=["Kal Dosa", "Sambar/Vadacurry", "Chutney", "B,B,J", "Tea, Coffee, Milk"],
    lunch=["Phulka", "Dal Maharani", "White Rice", "Rasam", "Kara/More Kozhambhu", "Poriyal", "Dahi Vada", "Fryums", "Sweet :  Gulab Jamun"],
    snacks=["Masala Peanuts", "Tea, Coffee, Milk"],
    dinner=["Phulka", "Dhal Makhani", "White Rice", "Rasam", "Sambar", "Butter Milk", "Chutney", "Idly", "Sambar", "Beetroot Poriyal", "Fruits :  Seasonal Fruits"]
)
day16 = cp.copy(day2) 
day16.date ="2024-02-16",
day16.id = 16


day3 = DailyMeals(
    id=3,
    date=["2024-02-03"],
    breakfast=["Aloo Paratha" , "Curd", "Kitchadi", "Chutney", "Sambar", "B,B,J", "Tea, Coffee, Milk"],
    lunch=["Phulka", "Dal Maharani", "White Rice", "Rasam", "Kara/More Kozhambhu", "Poriyal" , "Dahi Vada", "Fryums", "Sweet :  Gulab Jamun"],
    snacks=["Aloo Bonda, Sauce", "Tea,Coffee,Milk"],
    dinner=["Phulka", "Dhal Rajma", "White Rice", "Rasam", "Sambar", "Curd", "Garlic Sauce", "Veg Fried rice", "Thurai Tomato Sabzhi", "Fruits :   Water melon"]
)
day17 = cp.copy(day3)
day17.date ="2024-02-17",
day17.id = 17

day4 = DailyMeals(
    id=4,
    date=["2024-02-04"],
    breakfast=["Vada Paav/Paav Bhaji,", "Pongal", "chutney" , "Sambar"],
    lunch=["Phulka", "Dal Rajma", "White Rice", "Rasam", "Papad", "Veg Biryani", "Panneer Burji", "Onion Raitha", "Sweet : Ice Cream"],
    snacks=["Veg Puff", "Tea, Coffee, Milk"],
    dinner=["Phulka", "Dhal Rajma", "White Rice", "Rasam", "Sambar", "Curd", "Garlic Sauce", "Veg Fried rice", "Thurai Tomato Sabzhi", "Fruits :   Water melon"]
)

menu = [day1,day15,day29,day2,day16,day3,day17,day4]
