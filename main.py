from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

#instantiate the fastapi
app = FastAPI(
    title="World University Ranking",
    description="Demo APIs for ranking universities and current student counts",
    version="1.0.0",
    openapi_extra={
        "owner": "Sam" 
    }
    
)

# the data in use 
rankings = {
    1: {
        "rank_id": 1,
        "name": "University of Oxford",
        "country": "United Kingdom",
        "rank": 1,
        "students": "20,774"
    },
    2: {
        "rank_id": 2,
        "name": "Stanford University",
        "country": "United States",
        "rank": 2,
        "students": "16,223"
    },
    3: {
        "rank_id": 3,
        "name": "Harvard University",
        "country": "United States",
        "rank": 3,
        "students": "21,261"
    },
    4: {
        "rank_id": 4,
        "name": "California Institute of Technology",
        "country": "United States",
        "rank": 4,
        "students": "2,238"
    },
    5: {
        "rank_id": 5,
        "name": "Massachusetts Institute of Technology",
        "country": "United States",
        "rank": 5,
        "students": "11,276"
    }
}

#create class of ranking
class Ranking(BaseModel):
    rank_id: int
    name: str
    country: str
    students: str


#create class for update
class UpdateRanking(BaseModel):
    rank_id: Optional[int] = None
    name: Optional[str] = None 
    country: Optional[str] = None
    rank: Optional[int] = None
    students: Optional[str] = None



# All REQUESTS Methods

# Request to get all all items
@app.get("/universities", status_code=200)
async def get_all_universities():
    return rankings


# Request to get a  Single  item
@app.get("/single-university/{rank_id}", status_code=200)
async def get_university(rank_id: int = Path(..., description="Get University")):
    return rankings.get(rank_id, {"Data": "Not Found"})


# Request to an item by name
@app.get("/search-university-by-name", status_code=200)
async def search_university_by_name(name: Optional[str] = None):
    for rank_id, university in rankings.items():
        if university["name"] == name:
            return university
    return {"Data": "Not Found"}


#Request to create  a new resource by POST
@app.post("/university", status_code=201)
async def add_university(ranking: Ranking):
    # Check if the university already exists
    for uni_id, uni_data in rankings.items():
        if uni_data["name"] == ranking.name:
            raise HTTPException(status_code=400, detail="University already exists")

    # Assign a new rank_id
    new_rank_id = max(rankings.keys()) + 1 if rankings else 1

    # Add the new university to rankings
    rankings[new_rank_id] = ranking.dict()

    return rankings[new_rank_id]



#Request to Update an already created Item
@app.put("/update-university/{record_id}", status_code=202)
async def update_record(record_id: int, record: UpdateRanking):
    if record_id not in rankings:
        return {"Error": "Record does not exist"}
    for attr, value in record.dict().items():
        if value is not None:
            rankings[record_id][attr] = value
    return rankings[record_id]


#Request Delete an Item
@app.delete("/university/{record_id}", status_code=204)
async def delete_university(record_id: int):
    if record_id not in rankings:
        return {"Error": "university does not exist"}
    del rankings[record_id]
    return {"Message": "University was successfully deleted."}





