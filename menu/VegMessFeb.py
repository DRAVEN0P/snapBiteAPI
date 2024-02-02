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


day18 = day4

day5 = DailyMeals(
    breakfast=["Poori", "Aloo Masala", "Semiya", "Chutney", "B,B,J", "Tea, Coffee, Milk"],
    lunch=["Phulka", "Dal Ajawin", "White Rice", "Sambar", "Rasam", "Butter Milk", "Onion rings", "Veg Panneer Hydrabadi", "Sweet:Rava Laddu/Boondhi laddu"],
    snacks=["Veg Cutlet", "Sauce", "Tea, Coffee, Milk"],
    dinner=["Phulka", "Dosa", "Chutney", "Dhal", "White Rice", "Rasam", "Sambar", "Butter Milk", "Green Veg", "Sabzhi", "Seasonal Fruits"]
)
day19 = day5

day6 = DailyMeals(
    breakfast=["Idly", "Sambar", "Chutney", "Kitchadi", "B,B,J", "Tea, Coffee, Milk"],
    lunch=["Phulka", "Dal Gujrati", "White Rice", "Rasam", "Loose Curd", "Papad", "Coconut Rice", "Thuvayal", "Dingri Muttar"],
    snacks=["Veg Samosa", "Sauce", "Tea,Coffee,Milk"],
    dinner=["Chapathi", "Dhal", "White Rice", "Rasam", "Sambar", "Butter Milk", "Dhum Aloo", "Sczewan Fried Rice", "Garlic Sauce", "Fruits : Pineapple"]
)
day17 = day6

day7 = DailyMeals(
    breakfast=["Masala Uthappam", "Sambar", "Chutney", "B,B,J", "Tea, Coffee, Milk"],
    lunch=["Phulka", "Dal Punjabi", "White Rice", "Sambar", "Rasam", "Loose Curd", "Fryums", "Panneer Do Piaza", "Poriyal", "Sweet : Jangri / Jilebi"],
    snacks=["Pani Poori", "Tea,Coffee,Milk"],
    dinner=["Phulka", "Dhal fry", "White Rice", "Rasam", "Sambar", "Curd Rice", "Meal maker peas Masala", "Fruits : Watermelon"],
)
day21 = day7

day8 = DailyMeals(
    breakfast=["Gobi Paratha", "Curd,","Pongal", "Chutney", "Sambar","B,B,J", "Tea, Coffee, Milk,"],
    lunch=["Phulka", "Dal Madka", "White Rice", "Sambar", "Rasam", "Curd", "Papad", "Green Veg Sabzhi", "Avaraikai Poriyal"],
    snacks=["Masala Peanuts", "Tea,Coffee,Milk"],
    dinner=["Poori", "Channa Masala", "White Rice", "Rasam", "Sambar", "Butter Milk", "Green Poriyal", "Fruits : Banana"]
)
day22 = day8

day9 = DailyMeals(
    breakfast=["Masala Dosa", "Sambar", "Chutney", "B,B,J", "Tea, Coffee, Milk"],
    lunch=["Phulka", "Dal Rajasthani", "White Rice", "Sambar", "Rasam", "Curd", "Masala Papad", "Panneer Tikka Masala", "Keerai Kootu", "Sweet :   Gulab Jamun"],
    snacks=["ake", "Tea,Coffee,Milk"],
    dinner=["Phulka", "Idly", "Chutney", "Dhal", "White Rice", "Rasam", "Sambar", "Butter Milk", "Aloo Brinjal", "Drumstic Masala", "Fruits :  Seasonal Fruits"]
)
day23 = day9

day10 = DailyMeals(
    breakfast=["Aloo Paratha", "Curd,","Kitchadi", "Chutney", "Sambar","B,B,J", "Tea, Coffee, Milk,"],
    lunch=["Phulka", "Dal Thadka", "White Rice", "Rasam", "Kadi pakoda / Dahi vada", "Papad", "Vatha Kozhambu", "Capsicum Peas Masala"],
    snacks=["Mysore Bonda", "Sauce", "Tea,Coffee,Milk"],
    dinner=["Phulka", "Dhal Masala", "White Rice", "Rasam", "Sambar", "Butter Milk", "Veg Chow mein", "Gobi Manchurian", "Fruits : Papaya"]
)
day24 = day10

day11 = DailyMeals(
    breakfast=["Idly", "Vada", "Sambar", "Chutney", "B,B,J", "Tea, Coffee, Milk"],
    lunch=["Phulka", "Dal Rajma", "White Rice", "Sambar", "Rasam", "Curd", "Fryums", "Veg Biryani", "Oil Brinjal", "Onion Raitha", "Sweet : Ice Cream"],
    snacks=["Vadapav", "Mint Chutney", "Tea,Coffee,Milk"],
    dinner=["Phulka", "Dhal masoor", "White Rice", "Rasam", "Sambar", "Butter Milk", "Channa Masala", "Plain Dosa", "Chutney", "Fruits : Fruit Salad"]
)
day25 = day11

day12 = DailyMeals(
    breakfast=["Poori", "Aloo Masala", "Poha Nampkin", "B,B,J", "Tea, Coffee, Milk"],
    lunch=["Phulka", "Dal Panchmela", "White Rice", "Sambar", "Rasam", "Curd", "Onion Rings", "Kadai Panneer", "Poriyal"],
    snacks=["Keera Bonda", "Chutney", "TEa, Coffee, Milk"],
    dinner=["Phulka", "Dhal masoor", "White Rice", "Rasam", "Sambar", "Butter Milk", "Channa Masala", "Plain Dosa", "Chutney", "Fruits : Fruit Salad"]
)
day26 = day12

day13 = DailyMeals(
    breakfast=["Aloo Paratha", "Curd,","Kitchadi", "Chutney", "Sambar","B,B,J", "Tea, Coffee, Milk,"],
    lunch=["Phulka", "Dal Thadka", "White Rice", "Sambar", "Rasam", "Curd", "Papad", "Veg Jal Frizhi", "Keerai Kootu", "Sweet : Fruit Kesari / Bread Halwa"],
    snacks=["Raw Banana Bajji", "Chutney", "TEa, Coffee, Milk"],
    dinner=["Phulka", "Dhal fry", "White Rice", "Rasam", "Sambar", "Butter Milk", "Veg Chow Mein", "Gobi Manchurian", "Fruits : Pineapple"],
)
day27 = day13

day14 = DailyMeals(
    breakfast=["Plain Dosa", "Sambar", "Chutney", "B,B,J", "Tea, Coffee, Milk"],
    lunch=["Phulka", "Dal Fry", "White Rice", "Sambar", "Rasam", "Curd", "Fryums", "Panneer Do Piazha"],
    snacks=["Eggless Cake", "Tea, Coffee,Milk"],
    dinner=["Phulka", "Dhal Thadka", "White Rice", "Rasam", "Sambar", "Butter Milk", "Puliyodra", "Aloo Podimas", "Bindi masala", "Fruits : Water Melon"]
)
day28 = day14