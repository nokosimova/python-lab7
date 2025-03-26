from sqlalchemy.orm import Session
from . import entities, models

def get_all_words(db_session: Session):

    return db_session.query(entities.Word).all()

def get_word_by_name(db_session: Session, name: str):

    return db_session.query(entities.Word)
                     .filter(entities.Word.name == name).first()

def add_word(db_session: Session, r: models.CreateRequest):

    entity = entities.Word(name = r.name, definition = r.definition)
    
    db_session.add(entity)
    
    db_session.commit()
    
    db_session.refresh(entity)
    
    return entity

def update_word(db_session: Session, word: entities.Word, value: models.UpdateRequest):
    
    word.definition = value.definition
    
    db_session.commit()
    
    db_session.refresh(word)
    
    return word

def delete_word(db_session: Session, word: entities.Word):
    
    db_session.delete(word)
    
    db_session.commit()
    
    return True