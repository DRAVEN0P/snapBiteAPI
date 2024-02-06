from fastapi import FastAPI
import menu.finalVegMess as mess_feb
import menu.nonveg as nonveg
import menu.specialMHostel as special


vegMenu = mess_feb.menu
nonvegMenu = nonveg.menu
specialMenu = special.menu

final_veg_menu = []
final_nonveg_menu = []
final_special_menu = []

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
app = FastAPI()


@app.get("/veg-menu")
def read_root():
    return {
        "BoysHostelMenu": final_veg_menu
    }

@app.get("/nonveg-menu")
def read_root():
    return {
        "BoysHostelMenu": final_nonveg_menu
    }

@app.get("/special-menu")
def read_root():
    return {
        "BoysHostelMenu": final_special_menu
    }

@app.get("/boys")
def read_root():
    return {
        "BoysHostelMenu": [final_veg_menu,final_nonveg_menu,final_special_menu]
    }


