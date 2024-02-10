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
    id = 1,
    date = ["2024-02-01"],
    breakfast = ["Idly","Sambar","Chutney","Vadai"],
    lunch = ["Phulka","Dhal Makhani","Vangibath","White Rice","Poondu kulambu","Rasam","Cup Curd","Keerai Kuttu","Fryums"],
    snacks = ["Mysore Bonda Chutney","Ginger Tea"],
    dinner=["Roti","Channa Butter Masala","Yam fry","Garlic Sauce","White Rice","Sambar","Rasam","Loose Curd","Veg: Veg Chow Mein Seasoanal Fruit"],
)

day15 = cp.copy(day1)
day15.id = 15
day15.date = ["2024-02-15"]
day29 = cp.copy(day1)
day29.id = 29
day29.date = ["2024-02-29"]

day2 = DailyMeals (
    id = 2,
    date = ["2024-02-02"],
    breakfast=["Paav Bhaji","Fry Chilly Rava kitchadi","Chutney"],
    lunch=["Plain Kulcha","Dhal","Malai Kofta Gravy","White Rice","Radish Sambar","Rasam","Cup Curd","Green Gram Pumpkin Sabji","Papad  Sweet : Rava laddu"],
    snacks=["Dahi Papdi Chat"],
    dinner=["Chapathi","Dhal","Urapadai","Avial","White rice","Sambar","Rasam","Butter Milk","Veg : Crispy Baby Corn","Banana"],
)

day16 = cp.copy(day2)
day16.id = 16
day16.date = ["2024-02-16"]

day3 = DailyMeals (
    id = 3,
    date = ["2024-02-03"],
    breakfast=["Masala Dosai","Sambar","Onion Chutney"],
    lunch=["Phulka","Masoor Dhal","Tamarind Rice","White Rice","Brinjal Sambar","Rasam","Cup Curd","Avaraikai Poriyal","Appalam"],
    snacks=["Veg.Sandwich"],
    dinner=["Wheat Parata","Veg Kurma","White Rice","Sambar","Rasam","Loose Curd","Beans Carrot Poriyal","Seasonal Fruit"],
)

day17 = cp.copy(day3)
day17.id = 17
day17.date = ["2024-02-17"]

day4 = DailyMeals (
    id = 4,
    date = ["2024-02-04"],
    breakfast = ["Methi poori","Aloo sabji","Brown Bread"],
    lunch=["Roti","Mixed Dhal Fry","White Rice","Brinjal Gravy","Rasam","Fryums","Onion Raitha","Veg : Vegetable Dum Biriyani","Gobi 65","Sweet : Kheer"],
    snacks=["Pani Poori (5 Nos)"],
    dinner=["Chapathi","Dhal","Mini Idli","Sambar","White Rice","Rasam","Loose Curd","Pudalangai Poriyal","Banana"],
)

day18 = cp.copy(day4)
day18.id = 18
day18.date = ["2024-02-18"]

day5 = DailyMeals (
    id = 5,
    date= ["2024-02-05"],
    breakfast=["Aloo Paratha","Curd","Varmicilli upma","Coconut Chutney"],
    lunch=["Phulka","Urad Dhal","White Rice","Bottle Guard Sambar","Rasam","Cup Curd","Papad","Veg : Paneer Butter Masala"],
    snacks=["Onion Samosa","Hot Badam Milk"],
    dinner=["Roti","Rajma masala","Ghee Rice","Dhal","White Rice","Rasam","Loose Curd","Kovaikai Poriyal","Water Melon"],
)

day19 = cp.copy(day5)
day19.id = 19
day19.date = ["2024-02-19"]

day6 = DailyMeals (
    id = 6,
    date=["2024-02-06"],
    breakfast=["Vada Pav","Mint Chutney","Fried Idly","Sambar","Chutney"],
    lunch=["Chapathi","Veg Dahi Vala","Bisibela Bath","White Rice","Rasam","Cup Curd","Potato Chips","Carrot Poriyal","Sweet : Gulab Jamun" ],
    snacks=["Coconut bun"],
    dinner=["Phulka","Mix veg curry","Plain Dosai","Kara Chutney","White Rice","Sambar","Rasam","Loose Curd","Fruit salad"],
)

day20 = cp.copy(day6)
day20.id = 20
day20.date = ["2024-02-20"]

day7 = DailyMeals (
    id = 7,
    date=["2024-02-07"],
    breakfast=["Pongal","Sambar","Chutney","Vadai","Pasta"],
    lunch=["Roti","Dhal Makani","White Rice","Moore kulambu","Rasam","Cup Curd","Cabbage Poriyal","Papad"],
    snacks=["Aloo Bonda","Chutney"],
    dinner=["Phulka","Dhal","Fried Rice","White Rice","Sambar","Rasam","Loose Curd","Veg : Mushroom Peas curry","Seasonal Fruit"],
)

day21 = cp.copy(day7)
day21.id= 21
day21.date =["2024-02-21"]

day8 = DailyMeals (
    id = 8,
    date=["2024-02-08"],
    breakfast=["Onion Tomato Uthappam","Sambar","Peanut Chutney"],
    lunch=["Phulka","Kadi pakoda","Beet Root Poriyal","White Rice","Avarakkai sambar","Rasam","Cup Curd","Green Gram Sprouts","Fryums"],
    snacks=["Veg Cutlet (2 Nos)"],
    dinner=["Diamond Chapathi","Capsicum Paneer Masala","White Rice","Sambar","Rasam","Loose Curd","Beans Poriyal","Musk melon"],
)

day22 = cp.copy(day8)
day22.id= 22
day22.date = ["2024-02-22"]

day9 = DailyMeals (
    id = 9,
    date=["2024-02-09"],
    breakfast = ["Gobi Paratha","Curd","Pickle","Kitchadi","Coconut Chutney"],
    lunch = ["Phulka","Mixed Dhal","Coconut Rice","White Rice","Raw Mango Sambar","Rasam","Cup Curd","Aloo Capcicum Sabji","AppalamSweet : Milk peda"],
    snacks = ["Navadhanya Sundal"],
    dinner=["Chapathi","Yellow Dhal","White Rice","Sambar","Rasam","Loose Curd","Veg : Veg Kofta Curry","Banana"],
)

day23 = cp.copy(day9)
day23.id = 23
day23.date = ["2024-02-23"]

day10 = DailyMeals (
    id = 10,
    date=["2024-02-10"],
    breakfast=["Podi Dosai","Sambar","Chutney"],
    lunch=["Chapathi","Green gram Dhal","White Rice","Karamani Kara Kulambu","Rasam","Peerkankai Poriyal","Fryums","Cup Curd"],
    snacks=["French Fries"],
    dinner=["Methi Chapathi","Soya Chunks Gravy","White Rice","Sambar","Rasam","Loose Curd","Cabbage Peas poriyal","Schezwan fried rice","Fruit salad","Ice cream"],
)

day24 = cp.copy(day10)
day24.id = 24
day24.date = ["2024-02-24"]

day11 = DailyMeals(
    id = 11,
    date=["2024-02-11"],
    breakfast=["Poori","Channa Masala","Brown Bread"],
    lunch=["Phulka","Dhal","White Rice","Rasam","SalnaAppalam","Cucumber Raitha","Veg : Chettinad Veg Biriyani","Gobi 65","Sweet : Payasam"],
    snacks=["Aloo Samosa"],
    dinner=["Chapathi","Dhal Punjabi","White Rice","Sambar","Rasam","Loose Curd","Kashmiri Pulav","Vegetable kurma","Papaya"],
)

day25 = cp.copy(day11)
day25.id = 25
day25.date = ["2024-02-25"]

day12 = DailyMeals (
    id = 12,
    date = ["2024-02-12"],
    breakfast=["Set Dosai","Vadacury","Chutney","Pasta"],
    lunch=["Chapathi","Toor  Dhal","Tomato Rice","White Rice","Lady's finger Sambar","Rasam","Cup Curd","Cluster beans sabji","Appalam"],
    snacks=["Sweet corn chat"],
    dinner=["Chole Bhatura","White Rice","Sambar","Rasam","Loose Curd","Bottle Guard Sabji","Curd rice","Seasonal Fruit"],
)

day26 = cp.copy(day12)
day26.id = 26
day26.date = ["2024-02-26"]

day13 = DailyMeals (
    id = 13,
    date = ["2024-02-13"],
    breakfast=["Mixed Veg Paratha","Curd","Kitchadi","Chutney"],
    lunch=["Chapati","Palak green gram dal","Lemon Rice","White Rice","Sundakai Vatha kuzlambu","Rasam","Potato fry","Appalam","Cup Curd","Sweet : Jangari"],
    snacks=["Bhel Poori"],
    dinner=["Wheat Roti","Gobi Mattar masala","White Rice","Sambar","Rasam","Butter Milk","Veg : Manchurian Dry","Water Melon"],
)

day27 = cp.copy(day13)
day27.id =27
day27.date = ["2024-02-27"]

day14 = DailyMeals (
    id = 14,
    date = ["2024-02-14"],
    breakfast=["Poha Namkeen","Curd","Pongal","Sambar","Chutney"],
    lunch=["Chapathi","Channa dhal","Sepan Kizhangu fry","Papad","White Rice","Drumstick Sambar","Rasam","Cup Curd","Veg : Kadai Paneer" ],
    snacks=["Veg Puff"],
    dinner=["Phulka","Dhal","Onion Uthappam","Mixed vegetable curry","White Rice","Sambar","Rasam","Nool Khol Poriyal","Loose Curd","Tomato Soup","Banana"],
)

day28 = cp.copy(day14)
day28.id = 28
day28.date = ["2024-02-28"]


menu = [
    day1, day15, day29,
    day2, day16,
    day3, day17,
    day4, day18,
    day5, day19,
    day6, day20,
    day7, day21,
    day8, day22,
    day9, day23,
    day10, day24,
    day11, day25,
    day12, day26,
    day13, day27,
    day14, day28
]