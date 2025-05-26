##Crypto trading platform

from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

crypto_userid  = {1: "user1", 2: "user2", 3: "user3"}
userid_balance = {1: 1000.0, 2: 2000.0, 3: 3000.0}


@app.get("/")   
def root():
    return {"message": "Welcome to the flower"}

@app.post("/api/crypto/{userid}")
async def add_use(userid: int, request: Request):
    """
    Add a new user with a given userid.
    """
    if userid in crypto_userid:
        return {"message": "User already exists"}
    data = await request.json()    
    crypto_userid[userid] = data.get("username", f"user{userid}")
    userid_balance[userid] = data.get("balance", 1000)
    
    return {"message": "User added successfully", "userid": userid, "username": crypto_userid[userid], "balance": userid_balance[userid]}
@app.get("/api/crypto/{username}")
async def get_user(username: str):
    """
    Get user details by username.
    """
    for userid, name in crypto_userid.items():
        if name == username:
            return {"userid": userid, "username": name, "balance": userid_balance[userid]}
    return {"message": "User not found"}



@app.put("/api/crypto/{username}")
async def update_user(username: str, request: Request):
    """
    Update user details by username.
    """
    for userid, name in crypto_userid.items():
        if name == username:
            data = await request.json()
            crypto_userid[userid] = data.get("username", name)
            userid_balance[userid] = data.get("balance", userid_balance[userid])
            return {"message": "User updated successfully", "userid": userid, "username": crypto_userid[userid], "balance": userid_balance[userid]}
    return {"message": "User not found"}
@app.delete("/api/crypto/{username}")
async def delete_user(username: str):
    """
    Delete user by username.
    """
    for userid, name in list(crypto_userid.items()):
        if name == username:
            del crypto_userid[userid]
            del userid_balance[userid]
            return {"message": "User deleted successfully", "username": username}
    return {"message": "User not found"}