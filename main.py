from fastapi import FastAPI
import menu.finalVegMess as mess_feb
import menu.nonveg as nonveg
import menu.specialMHostel as special
import girls.Lhveg as lhveg
import girls.Lhsp as lhsp


vegMenu = mess_feb.menu
nonvegMenu = nonveg.menu
specialMenu = special.menu


girlsMenu_veg = lhveg.menu
girlsSp = lhsp.menu


final_veg_menu = []
final_nonveg_menu = []
final_special_menu = []


final_girlsMenu_veg = []
final_girlsMenu_Sp = []

for i in range(len(vegMenu)):

#   boys menu
    final_veg_menu.append(
        {
            "id":vegMenu[i].id,
            "date":vegMenu[i].date[0],
            "BreakFast":vegMenu[i].breakfast,
            "Lunch":vegMenu[i].lunch,
            "Snacks":vegMenu[i].snacks,
            "Dinner":vegMenu[i].dinner
        }
    )

    final_nonveg_menu.append(
        {
            "id":nonvegMenu[i].id,
            "date":nonvegMenu[i].date[0],
            "BreakFast":nonvegMenu[i].breakfast,
            "Lunch":nonvegMenu[i].lunch,
            "Snacks":nonvegMenu[i].snacks,
            "Dinner":nonvegMenu[i].dinner
        }
    )

    final_special_menu.append(
        {
            "id":specialMenu[i].id,
            "date":specialMenu[i].date[0],
            "BreakFast":specialMenu[i].breakfast,
            "Lunch":specialMenu[i].lunch,
            "Snacks":specialMenu[i].snacks,
            "Dinner":specialMenu[i].dinner
        }
    )

# girls menu
    
    final_girlsMenu_veg.append(
        {
            "id":girlsMenu_veg[i].id,
            "date":girlsMenu_veg[i].date[0],
            "BreakFast":girlsMenu_veg[i].breakfast,
            "Lunch":girlsMenu_veg[i].lunch,
            "Snacks":girlsMenu_veg[i].snacks,
            "Dinner":girlsMenu_veg[i].dinner
        }
    )


    final_girlsMenu_Sp.append(
        {
            "id":girlsSp[i].id,
            "date":girlsSp[i].date[0],
            "BreakFast":girlsSp[i].breakfast,
            "Lunch":girlsSp[i].lunch,
            "Snacks":girlsSp[i].snacks,
            "Dinner":girlsSp[i].dinner
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
        "BoysHostelMenu": [final_girlsMenu_veg,final_nonveg_menu,final_girlsMenu_Sp]
    }


