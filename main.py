from fastapi import FastAPI, Depends
from models import *
from schemas import *
from database import SessionLocal, engine
from sqlalchemy.orm import Session

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/game/add")
async def addGame(details: CreateGame, db: Session = Depends(get_db)):
    to_create = Game(name=details.name)
    db.add(to_create)
    db.commit()
    return {"id": to_create.id, "name": to_create.name}
    