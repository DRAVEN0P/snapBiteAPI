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
    breakfast = ["Panneer Paratha","Curd","Pongal","Sambar","Fresh Juice","Cold Milk","Cornflakes","Chutney","B,B,J","Tea","Coffee","Milk","Black Channa Sprout","Fried Eggs(2nos)"],
    lunch = ["Phulka","Fried Egg Lababdar /Fish Amritsari Dingri Muttar","White Rice","Sambar","Rasam","Wheel Chips","Dal Rajma","Sweet : Rasmalai/ Rasagula"],
    snacks = ["Donut/Croissant","Tea","Coffee","Milk"],
    dinner=["Poori","Channa Masala","White Rice","Rasam","Veriety Rice"," Poriyal","Curd","Veg Brocoli Soup","Fruit Salad"],
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
    breakfast=["Mysore Masala Dosa","Sambar","Chutney","Fresh Juice","Cold Milk","Cornflakes","B,B,J","Tea","Coffee","Milk","Moong Dal Sprout","Scrambeled Egg(2)"],
    lunch=["Phulka","Dhal","Tandoor Chicken","Panneer Fingers","White rice","Sambar","Gr.Veg SabzhiCurd","Fryums","Pineapple Rasam","Sweet : Gulab Jamun /  Makhan peda"],
    snacks=["Brownie Cake","Tea","Coffee","Milk"],
    dinner=["Phulka","Dal Rajma","Idly","Sambar","Chutney","White Rice","Dhum Aloo / Aloo Jeera Rasam","Loose Curd","Cream of Tomato","Fruits :  Fresh Fruits"],
)

day16 = cp.copy(day2)
day16.id = 16
day16.date = ["2024-02-16"]

day3 = DailyMeals (
    id = 3,
    date = ["2024-02-03"],
    breakfast=["Aloo Paratha","Curd","Kitchadi","Chutney","Fresh Juice","Cold Milk","Chocos","Sambar","Pickle","B,B,J","Tea","Coffee","Milk","Salad","Egg Podimas"],
    lunch=["Phulka","Dal Makhani","Mushroom Muttar Masala","Dhai Vada","Dal Rasam","Fryums","White Rice","Karakozhambu/ Morekozhambu","Sweet :  Kova  Mysore Paak/  Bread Halwa"],
    snacks=["French Fries","Sauce","Ice Lemon Tea","Coffee"],
    dinner=["Phulka","Dal Rajasthani","Veg & Egg Fried Rice","Meal maker peas  Masala","White Rice","Sambar","Rasam","Curd","Spring Onion Soup","Fruits:Musk melon"],
)

day17 = cp.copy(day3)
day17.id = 17
day17.date = ["2024-02-17"]

day4 = DailyMeals (
    id = 4,
    date = ["2024-02-04"],
    breakfast = ["Paav Bhaji/Vada Paav","Pongal","Chutney","Fresh Juice","Cold Milk","Corn Flakes","B,B,J","Tea","Coffee","Milk","Sambar Green Salad","Fried Eggs(2nos)"],
    lunch=["Phulka","Dal Rajma","Chicken Biryani","Veg Biryani","Banaras Baigan","Panneer Burji","Onion Raitha","White Rice","Sambar","Tomato Rasam","Papad","Sweet:Assorted Ice Cream"],
    snacks=["Sweet Puff/Dilkush","Tea","Coffee","Milk"],
    dinner=["Phulka","Dal Masala","Aloo Capsicum Masala","White Rice","Sambar","Poriyal","Butter Milk","Variety Rice","Rasam","Minestroni Soup","Fruits : Papaya"],
)

day18 = cp.copy(day4)
day18.id = 18
day18.date = ["2024-02-18"]

day5 = DailyMeals (
    id = 5,
    date= ["2024-02-05"],
    breakfast= ["Poori","Aloo Masala","Semiya","Chutney","Banana","Milk Shake","Cold Milk","Chocos","B,B,J","Tea","Coffee","Milk","Cow Peas Salad","French toast"],
    lunch=["Phulka","Mangolian Chicken/ Chilly Chicken","Chilly Panneer","Fried Rice","Poriyal","Dhal Fry","White Rice","Sambar","Rasam","Wheel Chips","Sweet : Chandrakala/Milk Sweet","Butter Milk"],
    snacks=["Spring Roll","Tea","Coffee","Milk"],
    dinner=["Plain Dosa","Dal","Sambar","Chutney","Veg Jal Frizhi","Methi Roti / Phulka","White Rice","Rasam","Butter Milk","Hot n Sour Veg Soup","Fruits : Fresh Fruits"],
)

day19 = cp.copy(day5)
day19.id = 19
day19.date = ["2024-02-19"]

day6 = DailyMeals (
    id = 6,
    date=["2024-02-06"],
    breakfast=["Idly","Vada","Sambar","Kitchadi","Chutney","Fresh Juice","Cold Milk","Cornflakes","B,B,J","Tea","Coffee","Milk","Black eye Peas Salad","Fried Eggs"],
    lunch=["Latcha Parotha/Daimond Chapathy","Dal Thadka","Channa Masala","White Rice","Pineapple Rasam","Curd","Bisibilla Bath","Potato Chips","Sweet : Carrot Halwa"],
    snacks=["Veg Samosa","Imly Chutney","Tea","Coffee","Milk"],
    dinner=["Chapathi","Veg / Egg Sczewan Fried Rice","Rajma Masala","Long Beans Sabzhi","garlic sauce","White Rice","Sambar","Rasam","Butter Milk","Veg Manchow Soup","Fruits : Orange"],
)

day20 = cp.copy(day6)
day20.id = 20
day20.date = ["2024-02-20"]

day7 = DailyMeals (
    id = 7,
    date=["2024-02-07"],
    breakfast=["Kal Dosa","Vadacurry","Chutney","Fresh Juice","Cold Milk","Chocos","B,B,J","Tea","Coffee","Milk\Green Salad","Egg Burji (2 nos)"],
    lunch=["Phulka","Malliga Chicken Masala","Panneer Hariyali","Arvi Fry","Dhal Lasoni","Curd","White Rice","Sambar","Tomato Rasam","Fryums","Sweet : Shahi Thukra"],
    snacks=["Raw banana bajji","Chutney","Tea","Coffee","Milk"],
    dinner=["Phulka","Dal Maharani","Bindi JaipuriSnack Guard Kootu","White Rice","Sambar Rasam","Curd Rice / Variety Rice","Butter Milk","Chetinad Soup","Fruits : Papaya"],
)

day21 = cp.copy(day7)
day21.id = 21
day21.date =["2024-02-21"]

day8 = DailyMeals (
    id = 8,
    date=["2024-02-08"],
    breakfast=["Panneer Paratha","Curd","Pongal","Sambar","Dates Milk Shake","Cold Milk","Cornflakes","B,B,J","Tea","Coffee","Milk","Chutney","Sweet Corn Salad","Fried Eggs (2nos)"],
    lunch=["Phulka","Mughlai Egg Masala","Kadai Mushroom","White Rice","Sambar","Rasam","Banaras Baigan","Fryums","Dal Panchamela","CurdSweet : Rasmalai/ Rasagula"],
    snacks=["Sweet Corn/Masala Peanuts","Tea","Coffee","Milk"],
    dinner=["Poori","Channa Masala","White Rice","Rasam","Jeera Rice","Poriyal","Loose Curd","Mixed veg Soup","Fruits : Banana"],
)

day22 = cp.copy(day8)
day22.id = 22
day22.date = ["2024-02-22"]

day9 = DailyMeals (
    id = 9,
    date=["2024-02-09"],
    breakfast=["Masala Ghee Roast Dosa","Sambar","Fresh Juice","Cold Milk","Chocos","Chutney","B,B,J","Tea","Coffee","Milk Moong Dal Sprout","Scrambeled Egg(2)"],
    lunch=["Phulka","Dal Fry","Tandoori Chicken","Panneer Amritsari","White rice","Sambar","Poondu Rasam","Loose Curd","Fryums","Keira Kootu Sweet : Gulab Jamun/ Makhan peda"],
    snacks=["Brownie Cake","Tea","Coffee","Milk"],
    dinner=["Phulka","Dal Rajma","White Rice","Dhum Aloo/Banaras Aloo Rasam","Curd","Idly","Sambar","ChutneyCream of Tomato","Fruits:Papaya"],
)

day23 = cp.copy(day9)
day23.id = 23
day23.date = ["2024-02-23"]

day10 = DailyMeals (
    id = 10,
    date=["2024-02-10"],
    breakfast=["Aloo Paratha","Curd","Kitchadi","Chutney","Fresh Juice","Cold Milk","Chocos","Sambar","B,B,J","Tea","Coffee","Milk Salad","Egg Burji (2)"],
    lunch=["Phulka","Dal Makhani","Dingri Muttar","Dahi Vada","Poriyal","Sambar/Karakolambu","White Rice","Paruppu Rasam","Fryums","Sweet : Ghee Mysore Paak"],
    snacks=["French Fries Sauce","Tea","Coffee","Milk"],
    dinner=["Phulka","Dal Rajasthani","Veg & Egg Fried Rice","Baby corn Manchurian","Poriyal","Loose Curd","White Rice","Sambar","Rasam","Spring Onion Soup","Fruits : Fresh Fruits"],
)

day24 = cp.copy(day10)
day24.id = 24
day24.date = ["2024-02-24"]

day11 = DailyMeals(
    id = 11,
    date=["2024-02-11"],
    breakfast=["Phulka","Dal","Chicken Biryani","Veg Biryani","Banaras Baigan","Panneer 65","Onion Raitha","White Rice","Sambar","Tomato Rasam","Papad","Sweet : Ice Cream / Kulfhi"],
    lunch=["Phulka","Dal","Chicken Biryani","Veg Biryani","Banaras Baigan","Panneer 65","Onion Raitha","White Rice","Sambar","Tomato Rasam","Papad","Sweet : Ice Cream / Kulfhi"],
    snacks=["Vada Paav/Pani Poori","Tea","Coffee","Milk"],
    dinner=["Phulka","Dal Masala","Butter Peas masala","White Rice","Sambar","Rasam","Aloo Jeera","Curd","Variety Rice","Sweet corn Soup","Fruits : Cut Fruits"],
)

day25 = cp.copy(day11)
day25.id = 25
day25.date = ["2024-02-25"]

day12 = DailyMeals (
    id = 12,
    date = ["2024-02-12"],
    breakfast=["Poori","Aloo Masala","Poha Nampkin","Banana Milk Shake","Cold Milk","Chocos","B,B,J","Tea","Coffee","Milk","CowPeasSalad","Chutney","French Toast"],
    lunch=["Phulka","Kashmiri  Chicken  Masala","Dal FryPanneer Butter Masala","Poriyal","Butter Milk","White Rice","Sambar","Pepper Rasam","Wheel Chips","Sweet : Mothichoor Laddu/   Rava Laddu"],
    snacks=["Mysore Bonda/Onion Pakoda","Tea","Coffee","Milk"],
    dinner=["Pudhina Roti / Phulka","Dosa","Sambar","Chutney","Loose Curd","Dhal Maharani","Channa Masala","White Rice","Rasam","Veg  Mushroom Soup","Fruits : Pineapple"],
)

day26 = cp.copy(day12)
day26.id = 26
day26.date = ["2024-02-26"]

day13 = DailyMeals (
    id = 13,
    date = ["2024-02-13"],
    breakfast=["Gobi Paratha","Curd","Kitchadi","Sambar","Date Milk Shake","Cold Milk","Cornflakes","B,B,J","Pickle","Tea","Coffee","Milk","Chutney","Black eye Peas Salad","Fried Eggs"],
    lunch=["Phulka","Dal  Ajwin","Veg Jal Frizhe","White Rice","Pineapple Rasam","Curd","Bisibilla Bath","Potato Chips","Sweet : Carrot Halwa/Beetroot Halwa"],
    snacks=["Onion Samosa","Sauce","Tea","Coffee","Milk"],
    dinner=["Phulka","Dal Fry","Veg & Egg Chow mein","Veg Chat pata/ Garlic Sauce","Poriyal","White Rice","Sambar","Rasam","Curd","Veg Manchow Soup","Fruits : Orange"],
)

day27 = cp.copy(day13)
day27.id = 27
day27.date = ["2024-02-27"]

day14 = DailyMeals (
    id = 14,
    date = ["2024-02-14"],
    breakfast=["Andhra Masala Dosa","Sambar","Chutney","Fresh Juice","Cold Milk","Chocos","B,B,J","Tea","Coffee","Milk","Green Salad","Egg Burji ( 2 nos )"],
    lunch=["Diamond Chapathi","Dal Fry","Pepper Chicken","Panneer Tikka Masala","Curd","Aloo Methi/  AlooSaagwala","White Rice","Sambar","Rasam","FryumsSweet : Coconut Burfi / Pineapple Pudding"],
    snacks=["Veg Burger/Veg Club Sandwich","Tea","Coffee","Milk"],
    dinner=["Phulka","Dal Maharani","Bindi Do Piaza Snack Guard Kootu","White Rice","Sambar","Rasam","Loose Curd","Puliyodra","Chetinad Soup","Fruits : Papaya"],
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