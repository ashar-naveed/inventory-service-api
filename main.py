from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas
from auth import hash_password, verify_password, create_access_token
from auth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

Base.metadata.create_all(bind=engine)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Inventory API running"}

@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    db_item = models.Item(name=item.name, quantity=item.quantity)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/", response_model=list[schemas.ItemResponse])
def get_items(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return db.query(models.Item).all()

@app.put("/items/{item_id}")
def update_quantity(item_id: int, quantity: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.quantity = quantity
    db.commit()
    return {"message": "Updated"}

@app.get("/items/low-stock/")
def low_stock(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return db.query(models.Item).filter(models.Item.quantity < 5).all()

from fastapi import HTTPException  # make sure this is imported

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Deleted"}

@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_pw = hash_password(user.password)
    db_user = models.User(username=user.username, password=hashed_pw)
    db.add(db_user)
    db.commit()
    return {"message": "User created"}

@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == form_data.username).first()
    
    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}