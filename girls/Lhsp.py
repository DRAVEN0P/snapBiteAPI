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
    breakfast = ["Idly", "Sambar"," Chutney"," Vadai","Veg : Veg Salad","Non Veg : Masala Omlette","Water Melon Juice","Chocos"],
    lunch = ["Phulka"," Dhal Makhani"," Vangibath White Rice"," Poondu  kulambu Rasam", "Cup Curd"," Keerai Kuttu"," Fryums","Sweet:  Rasmalai"],
    snacks = ["Mysore Bonda Chutney","Ginger Tea"],
    dinner=["Roti", "Channa Butter Masala", "Yam fry", "Garlic Sauce","White Rice"," Sambar"," Rasam"," Loose Curd","Veg: Veg Chow Mein","Non Veg : Egg Chow Mein","Palak Soup"," Seasoanl Fruit"]
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
    breakfast=["Water Melon Juice"," Chocos","Paav Bhaji"," Fry Chilly","Rava kitchadi", "Chutney","Veg : Peanut Sundal","Non Veg : French toast","Sapota Juice"],
    lunch=["Plain Kulcha"," Dhal, Malai Kofta Gravy","White Rice"," Radish Sambar"," Rasam"," Cup Curd","Green Gram Pumpkin Sabji"," Papad", "Sweet :  Rava laddu"],
    snacks=["Dahi Papdi Chat","Tea","Coffee","Milk"],
    dinner=["Chapathi"," Dhal"," Urapadai", "Avial White rice"," Sambar"," Rasam", "Butter Milk","Veg : Crispy Baby Corn ","Non Veg : Tandoori Chicken","Cream of Veg Soup"," Banana"],)

day16 = cp.copy(day2)
day16.id = 16
day16.date = ["2024-02-16"]

day3 = DailyMeals (
    id = 3,
    date = ["2024-02-03"],
    breakfast=["Masala Dosai"," Sambar"," Onion Chutney","Veg : Moochai Payaru Sundal","Non Veg : Boiled Egg Masala","Mixed Fruit Juice"],
    lunch=["Phulka"," Masoor Dhal"," Tamarind Rice","White Rice"," Brinjal Sambar"," Rasam", "Cup Curd","Avaraikai Poriyal"," Appalam","Sweet : Shahi Tukra",],
    snacks=["Veg. Sandwich","Ice Lemon Tea","Coffee"],
    dinner=["Wheat Parata"," Veg Kurma","White Rice"," Sambar"," Rasam", "Loose Curd", "Beans Carrot Poriyal","Veg Manchow Soup"," Seasonal Fruit"]
    )

day17 = cp.copy(day3)
day17.id = 17
day17.date = ["2024-02-17"]

day4 = DailyMeals (
    id = 4,
    date = ["2024-02-04"],
    breakfast = ["Methi poori"," Aloo sabji ","Brown Bread","Veg : Green Gram Sprouts","Non Veg : Omlette","Apple Juice, Chocos"],
    lunch=["Roti"," Mixed Dhal Fry", "White Rice", "Brinjal Gravy"," Rasam Fryums "," Onion Raitha","Veg : Vegetable Dum Biriyani ", "Gobi 65","Non Veg : Chicken Dum Biriyani","Sweet :  Kheer"],
    snacks=["Pani Poori (5 Nos)","Tea","Coffee","Milk"],
    dinner=["Chapathi"," Dhal"," Mini Idli"," Sambar","White Rice"," Rasam"," Loose Curd","Pudalangai Poriyal","Carrot Ginger Soup"," Banana"]
    )

day18 = cp.copy(day4)
day18.id = 18
day18.date = ["2024-02-18"]

day5 = DailyMeals (
    id = 5,
    date= ["2024-02-05"],
    breakfast= ["Aloo Paratha", "Curd","Varmicilli upma", "Coconut Chutney","Veg : Boiled Sweet Corn ","Non Veg : Boiled Egg","Musk Melon Juice"],
    lunch=["Phulka","Urad Dhal"," Papad","White Rice"," Bottle Guard Sambar"," Rasam", "Cup Curd","Veg : Paneer Butter Masala","Non Veg : Butter Chicken Masala","Sweet : Jilebi"],
    snacks=["Spring Roll","Hot Badam Milk","Tea","Coffee","Milk"],
    dinner=["Roti"," Rajma masala", "Ghee Rice", "Dhal ","White Rice"," Rasam"," Loose Curd","Kovaikai Poriyal","Sweet Corn Soup", "Water Melon"]
    )

day19 = cp.copy(day5)
day19.id = 19
day19.date = ["2024-02-19"]

day6 = DailyMeals (
    id = 6,
    date=["2024-02-06"],
    breakfast=["Vada Pav"," Mint Chutney","Fried Idly"," Sambar"," Chutney","Veg : Vegetable Salad","Non Veg : Scrambled Egg","Mint Lemon"," Chocos"],
    lunch=["Chapathi"," Veg Dahi Vala","Bisibela Bhat", "White Rice", " Rasam"," Cup Curd","Potato Chips"," Carrot Poriyal" ,"Sweet :  Gulab Jamun "],
    snacks=["coconut bun","Tea","Coffee","Milk"],
    dinner=["Phulka"," Mix veg curry"," Plain Dosai"," Kara Chutney","White Rice"," Sambar"," Rasam"," Loose Curd","Spring onion Soup"," Fruit salad"],)

day20 = cp.copy(day6)
day20.id = 20
day20.date = ["2024-02-20"]


day7 = DailyMeals (
    id = 7,
    date=["2024-02-07"],
    breakfast=["Pongal", "Sambar"," Chutney"," Vadai Pasta","Veg : Mixed Sprouts Sundal ","Non Veg : Boiled Egg","Mixed Fruit Juice "],
    lunch=["Roti"," Dhal Makani","White Rice"," Moore kulambu"," Rasam"," Cup Curd","Cabbage Poriyal"," Papad","Sweet : Kova Mysorepaku"],
    snacks=["Aloo Bonda","Chutney","Tea","Coffee","Milk"],
    dinner=["Phulka"," Dhal"," Fried Rice","White Rice"," Sambar"," Rasam"," Loose Curd","Veg : Mushroom Peas curry","Non Veg :  Aloo Chicken curry","Veg Chettinadu Soup, Seasonal Fruit"]
    )

day21 = cp.copy(day7)
day21 = 21
day21 =["2024-02-21"]

day8 = DailyMeals (
    id = 8,
    date=["2024-02-08"],
    breakfast=["Onion Tomato Uthappam","Sambar"," Peanut Chutney","Veg : Masala Black Chenna","Non Veg : Scrambled Egg ","Amla mint juice"," Chocos"],
    lunch=["Phulka"," Kadi pakoda"," Beet Root Poriyal","White Rice"," Avarakkai sambar"," Rasam"," Cup Curd" ,"Green Gram Sprouts"," Fryums","Sweet : Rasgulla"],
    snacks=["Burger","Tea","Coffee","Milk"],
    dinner=["Diamond Chapathi"," Capsicum Paneer Masala","White Rice"," Sambar", "Rasam", "Loose Curd","Beans Poriyal","Chow Mein Soup"," Musk melon"]
    )

day22 = cp.copy(day8)
day22 = 22
day22 = ["2024-02-22"]

day9 = DailyMeals (
    id = 9,
    date=["2024-02-09"],
    breakfast=["Paneer Paratha"," Curd"," Pickle","Kitchadi"," Coconut Chutney","Veg : Vegetable Salad","Non Veg : Boiled Egg Masala","Grape Juice"],
    lunch=["Phulka"," Mixed Dhal"," Coconut Rice","White Rice"," Raw Mango Sambar", "Rasam", "Cup Curd","Aloo Capcicum Sabji"," Appalam","Sweet : Milk peda"],
    snacks=["Navadhanya Sundal","Tea","Coffee","Milk"],
    dinner=["Chapathi","Yellow Dhal","White Rice","Sambar"," Rasam"," Loose Curd","Veg : Veg Kofta Curry","Non Veg : Chettinadu Chicken" ,"Mixed Veg Soup","Banana"]
    )

day23 = cp.copy(day9)
day23 = 23
day23 = ["2024-02-23"]

day10 = DailyMeals (
    id = 10,
    date=["2024-02-10"],
    breakfast=["Podi Dosai"," Sambar"," Chutney","Veg : Cowpea (Karamani) Sundal","Non Veg : Boiled Egg","Papaya Juice"," Chocos"],
    lunch=["Chapathi"," Green gram Dhal","White Rice", "Karamani Kara Kulambu", "Rasam"," Cup Curd","Peerkankai Poriyal"," Fryums","Sweet : Dry Jamoon"],
    snacks=["French Fries"," Sauce","Tea","Coffee","Milk"],
    dinner=["Methi Chapathi", "Soya Chunks Gravy"," Schezwan fried rice","White Rice", "Sambar"," Rasam"," Loose Curd","Cabbage Peas poriyal","Mushroom Soup"," Fruit salad"," Ice cream"])

day24 = cp.copy(day10)
day24 = 24
day24 = ["2024-02-24"]

day11 = DailyMeals(
    id = 11,
    date=["2024-02-11"],
    breakfast=["Poori"," Channa Masala","Brown Bread","Veg : Vegetable Salad","Non Veg : Masala Omelette ","Water Melon Juice"],
    lunch=["Phulka"," Dhal","White Rice", "Rasam", "Salna Appalam"," Cucumber Raitha","Veg : Chettinad Veg Biriyani , Gobi 65","Non Veg : Chicken Biriyani","Sweet : Payasam "],
    snacks=["Aloo Samosa","Tea","Coffee","Milk"],
    dinner=["Chapathi"," Dhal Punjabi","White Rice", "Sambar"," Rasam"," Loose Curd","Kashmiri Pulav"," Vegetable kurma","Veg Clear Soup","  Papaya"]
    )

day25 = cp.copy(day11)
day25 = 25
day25 = ["2024-02-25"]

day12 = DailyMeals (
    id = 12,
    date = ["2024-02-12"],
    breakfast=["Set Dosai"," Vadacury"," Chutney Pasta","Veg : Multi Grain Sundal ","Non Veg: Boiled Egg","Pineapple Juice, Chocos",],
    lunch=["Chapathi"," Toor Dhal"," Tomato Rice","White Rice"," Lady's finger","  Sambar"," Rasam"," Cup Curd","Cluster beans sabji"," Appalam","Sweet :  Laddu"],
    snacks=["Sweet corn chat","Tea","Coffee","Milk"],
    dinner=["Chole Bhatura","White Rice"," Sambar"," Rasam","Bottle Guard Sabji"," Curd rice","Veg Noodle Soup"," Seasonal Fruit"],)

day26 = cp.copy(day12)
day26 = 26
day26 = ["2024-02-26"]

day13 = DailyMeals (
    id = 13,
    date = ["2024-02-13"],
    breakfast=["Mixed Veg Paratha"," Curd","Kitchadi"," Chutney","Veg : Sauthe Black Chenna Sundal","Non Veg : Scrambled Egg","Dates Milkshake"],
    lunch=["Chapati"," Palak green gram dal"," Lemon Rice","White Rice"," Sundakai Vatha kuzlambu"," Rasam","Potato fry"," Appalam"," Cup Curd","Sweet :  Jangari"],
    snacks=["Bhel poori","Tea","Coffee","Milk"],
    dinner=["Wheat Roti"," Gobi Mattar masala","White Rice", "Sambar, Rasam"," Butter Milk","Veg : Manchurian Dry","Non Veg : Chicken 65 ","Hot and Sour Soup"," Water Melon"],)

day27 = cp.copy(day13)
day27 =27
day27 = ["2024-02-27"]

day14 = DailyMeals (
    id = 14,
    date = ["2024-02-14"],
    breakfast=["Poha Namkeen"," Curd Pongal"," Sambar"," Chutney","Veg : Sprouted Moong Dhal","Non Veg : French Toast","Mango Juice"],
    lunch=["Chapathi"," Channa dhal","Sepan Kizhangu fry"," Papad","White Rice"," Drumstick Sambar"," Rasam", "Cup Curd","Veg : Kadai Paneer ","Non Veg:Fish Curry / Fish ","Sweet : Badusha"],
    snacks=["Veg puff","Tea","Coffee","Milk"],
    dinner=["Phulka"," Dhal"," Onion Uthappam", "Mixed Vegetable Curry","White Rice", "Sambar", "Rasam","Nool Khol Poriyal"," Loose curd","Tomato Soup"," Banana"]
    )

day28 = cp.copy(day14)
day28 = 28
day28 = ["2024-02-28"]


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