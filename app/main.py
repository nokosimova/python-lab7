from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import entities, models, repository

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Glossary 2025", description="Glossary Term Management Application",version="1.0.0")

def db_session():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.post("/words", response_model = models.GetResponse, status_code = status.HTTP_201_CREATED)
def create(request: models.CreateRequest, db: Session = Depends(db_session)):

    word = repository.get_word_by_name(db, request.name)
    
    if word:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "You have already add this word")
    
    return repository.add_word(db, request)

@app.get("/words/{name}", response_model = models.GetResponse)
def get(name: str, db: Session = Depends(db_session)):
    
    word = repository.get_word_by_name(db, name)
    
    if not word:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Word not found!")
    
    return word

@app.get("/allWords", response_model = list[models.GetResponse])
def get_all(db: Session = Depends(db_session)):
    
    words = repository.get_all_words(db)
    
    return terms

@app.delete("/words/{name}", status_code = status.HTTP_204_NO_CONTENT)
def delete(word_name: str, db: Session = Depends(db_session)):
    
    word = repository.get_word_by_name(db, word_name)
    
    if not word:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Word updated")
    
    repository.delete_word(db, word)
    
    return None

@app.put("/words/{name}", response_model = models.GetResponse)
def update(word_name: str, new_data: models.UpdateRequest, db: Session = Depends(db_session)):
    
    word = repository.get_word_by_name(db, word_name)    
    
    if not word:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Word not found")
    
    return repository.update_term(db, word, new_data)