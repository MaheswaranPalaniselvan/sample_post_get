# pip install fastapi uvicorn sqlalchemy databases requests
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
from typing import Dict, List, Union

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = MetaData()

app = FastAPI()
items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("data", String), 
)

metadata.create_all(bind=engine)

def get_existing_data(db) -> List[Union[Dict, List]]:
    existing_item = db.query(items).first()
    if existing_item:
        return json.loads(existing_item.data)
    else:
        return []
    
@app.post("/save_data/")
async def create_or_update_item(item_data: Dict):
    db = SessionLocal()

    existing_data = get_existing_data(db)
    existing_data.append(item_data)
    json_data = json.dumps(existing_data)
    stmt = items.update().values(data=json_data)
    db.execute(stmt)
    db.commit()
    db.close()
    return {"message": "Data appended successfully."}

@app.get("/get_data/", response_model=List[Dict])
async def read_items():
    db = SessionLocal()
    existing_data = get_existing_data(db)
    db.close()
    return existing_data
# uvicorn app:app --reload