from fastapi import FastAPI
import menu.finalVegMess as mess_feb
import menu.nonveg as nonveg
import menu.specialMHostel as special
import girls


vegMenu = mess_feb.menu
nonvegMenu = nonveg.menu
specialMenu = special.menu


girlsMenu = girls.menu

final_veg_menu = []
final_nonveg_menu = []
final_special_menu = []


final_girlsMenu = []

for i in vegMenu:
    final_veg_menu.append(
        {
            "id":i.id,
            "date":i.date[0],
            "BreakFast":i.breakfast,
            "Lunch":i.lunch,
            "Snacks":i.snacks,
            "Dinner":i.dinner
        }
    )
for i in nonvegMenu:
    final_nonveg_menu.append(
        {
            "id":i.id,
            "date":i.date[0],
            "BreakFast":i.breakfast,
            "Lunch":i.lunch,
            "Snacks":i.snacks,
            "Dinner":i.dinner
        }
    )
for i in specialMenu:
    final_special_menu.append(
        {
            "id":i.id,
            "date":i.date[0],
            "BreakFast":i.breakfast,
            "Lunch":i.lunch,
            "Snacks":i.snacks,
            "Dinner":i.dinner
        }
    )
for i in girlsMenu:
    final_girlsMenu.append(
        {
            "id":i.id,
            "date":i.date[0],
            "BreakFast":i.breakfast,
            "Lunch":i.lunch,
            "Snacks":i.snacks,
            "Dinner":i.dinner
        }
    )


app = FastAPI()

@app.get("/boys")
def read_root():
    return {
        "BoysHostelMenu": [final_veg_menu,final_nonveg_menu,final_special_menu]
    }

@app.get("/girls")
def read_root():
    return {
        "BoysHostelMenu": [final_girlsMenu,final_girlsMenu,final_girlsMenu]
    }


