from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
#burda fastapı çalıştırırken ilk önce py dosyamızın ismi sonra  app = FastAPI()  `FastAPI` sınıfı, FastAPI uygulamasını temsil eden bir sınıftır
# --reload sonuna eklenerek fast api de bir güncelleme yapıoldığında otomatik olarak sunucu tekra çalıştırılır.





app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class hero(BaseModel):
    id: int
    name: str


heroes = [
    {"id": 12, "name": "Dr. Nice"},
    {"id": 13, "name": "Bombasto"},
    {"id": 14, "name": "Celeritas"},
    {"id": 15, "name": "Magneta"},
    {"id": 16, "name": "RubberMan"},
    {"id": 17, "name": "Dynama"},
    {"id": 18, "name": "Dr. IQ"},
    {"id": 19, "name": "Magma"},
    {"id": 20, "name": "Tornado"}
]


@app.get("/heroes")
def get_heroes():
    return heroes

@app.get("/detail/{hero_id}")
def get_hero(hero_id: int):
    for hero in heroes:
        if hero["id"] == hero_id:
            return hero
@app.post("/heroes/")       
async def add_hero(hero: dict):
    new_hero = { 
               "id": max(hero["id"] for hero in heroes) + 1, 
               "name": hero["name"],
                    } 
    heroes.append(new_hero)
    return new_hero


@app.delete("/heroes/{hero_id}")
async def delete_hero(hero_id: int):
     global heroes
     heroes = [hero for hero in heroes if hero["id"] !=  hero_id] 
@app.put("/heroes/{hero_id}")
async def update_hero(hero_id: int, hero_update: hero):
    for hero in heroes:
        if hero["id"] == hero_id:
            hero["name"] = hero_update.name
            return {"message": "Hero updated successfully"}  # Başarılı bir yanıt d

    return JSONResponse(status_code=404, content={"message": "Hero not found"})  # Hero bulunamadı durumu için HTTP 404 yanıtı döndür



@app.get("/detail/")
def search_hero(name: str):  
 found_heroes = [hero for hero in heroes if name.lower() in hero["name"].lower()] 
 return found_heroes


    
    
    