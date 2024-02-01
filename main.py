from fastapi import FastAPI
import mess_feb
import uvicorn

menu = mess_feb.menu

final_menu = []
for i in menu:
    final_menu.append(
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
        "BoysHostelMenu": final_menu
    }



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
