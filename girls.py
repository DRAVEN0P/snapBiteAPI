import copy as cp 
class DailyMeals:
    def __init__(self,id,date, breakfast, lunch, dinner,snacks):
        self.id = id
        self.date = date
        self.breakfast = breakfast
        self.lunch = lunch
        self.snacks = snacks
        self.dinner = dinner

day1= DailyMeals(
    id = 1,
    date = ["2024-02-01"],
    breakfast=["Gobi Paratha", "Curd,"],
    lunch=["Phulka", "Dal Masala"],
    snacks=["Sweet Corn","Tea"],
    dinner=["Poori","White Rice"])

day15 = cp.copy(day1)
day15.id = 15
day15.date = ["2024-02-15"]
day29 = cp.copy(day1)
day29.id = 29
day29.date = ["2024-02-29"]

day2 = DailyMeals(
    id = 2,
    date = ["2024-02-02"],
    breakfast=["Gobi Paratha", "Curd,"],
    lunch=["Phulka", "Dal Masala"],
    snacks=["Sweet Corn","Tea"],
    dinner=["Poori","White Rice"])


day16 = cp.copy(day2)
day16.id = 16
day16.date = ["2024-02-16"]

day3 = DailyMeals (
    id = 3,
    date = ["2024-02-03"],
    breakfast=["Gobi Paratha", "Curd,"],
    lunch=["Phulka", "Dal Masala"],
    snacks=["Sweet Corn","Tea"],
    dinner=["Poori","White Rice"])


day17 = cp.copy(day3)
day17.id = 17
day17.date = ["2024-02-17"]

day4 = DailyMeals (
    id = 4,
    date = ["2024-02-04"],
    breakfast=["Gobi Paratha", "Curd,"],
    lunch=["Phulka", "Dal Masala"],
    snacks=["Sweet Corn","Tea"],
    dinner=["Poori","White Rice"])

day18 = cp.copy(day4)
day18.id = 18
day18.date = ["2024-02-18"]

day5 = DailyMeals (
    id = 5,
    date = ["2024-02-05"],
    breakfast=["Gobi Paratha", "Curd,"],
    lunch=["Phulka", "Dal Masala"],
    snacks=["Sweet Corn","Tea"],
    dinner=["Poori","White Rice"])

day19 = cp.copy(day5)
day19.id = 19
day19.date = ["2024-02-19"]

day6 = DailyMeals (
    id = 6,
    date = ["2024-02-06"],
    breakfast=["Gobi Paratha", "Curd,"],
    lunch=["Phulka", "Dal Masala"],
    snacks=["Sweet Corn","Tea"],
    dinner=["Poori","White Rice"])


day20 = cp.copy(day6)
day20.id = 20
day20.date= ["2024-02-20"]

day7 = DailyMeals (
    id = 7,
    date = ["2024-02-07"],
    breakfast=["Gobi Paratha", "Curd,"],
    lunch=["Phulka", "Dal Masala"],
    snacks=["Sweet Corn","Tea"],
    dinner=["Poori","White Rice"])

day21 = cp.copy(day7)
day21.id = 21
day21.date = ["2024-02-21"] 

day8 = DailyMeals (
    id = 8,
    date = ["2024-02-08"],
    breakfast=["Gobi Paratha", "Curd,"],
    lunch=["Phulka", "Dal Masala"],
    snacks=["Sweet Corn","Tea"],
    dinner=["Poori","White Rice"])

day22 = cp.copy(day8)
day22.id = 22
day22.date = ["2024-02-22"]

day9 = DailyMeals (
    id = 9,
    date = ["2024-02-09"],
    breakfast=["Gobi Paratha", "Curd,"],
    lunch=["Phulka", "Dal Masala"],
    snacks=["Sweet Corn","Tea"],
    dinner=["Poori","White Rice"])

day23 = cp.copy(day9)
day23.id = 23
day23.date = ["2024-02-23"]

day10 = DailyMeals (
    id = 10,
    date = ["2024-02-10"],
    breakfast=["Gobi Paratha", "Curd,"],
    lunch=["Phulka", "Dal Masala"],
    snacks=["Sweet Corn","Tea"],
    dinner=["Poori","White Rice"])

day24 = cp.copy(day10)
day24.id = 24
day24.date = ["2024-02-24"]

day11 = DailyMeals (
    id = 11,
    date = ["2024-02-11"],
    breakfast=["Gobi Paratha", "Curd,"],
    lunch=["Phulka", "Dal Masala"],
    snacks=["Sweet Corn","Tea"],
    dinner=["Poori","White Rice"])

day25 =cp.copy(day11)
day25.id = 25
day25.date = ["2024-02-25"]

day12 = DailyMeals (
    id = 12,
    date = ["2024-02-12"],
    breakfast=["Gobi Paratha", "Curd,"],
    lunch=["Phulka", "Dal Masala"],
    snacks=["Sweet Corn","Tea"],
    dinner=["Poori","White Rice"])

day26 = cp.copy(day12)
day26.id = 26
day26.date = ["2024-02-26"]

day13 = DailyMeals (
    id = 13,
    date = ["2024-02-13"],
    breakfast=["Gobi Paratha", "Curd,"],
    lunch=["Phulka", "Dal Masala"],
    snacks=["Sweet Corn","Tea"],
    dinner=["Poori","White Rice"])

day27 = cp.copy(day13)
day27.id = 27
day27.date = ["2024-02-27"]

day14 = DailyMeals (
    id = 14,
    date = ["2024-02-14"],
    breakfast=["Gobi Paratha", "Curd,"],
    lunch=["Phulka", "Dal Masala"],
    snacks=["Sweet Corn","Tea"],
    dinner=["Poori","White Rice"])

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