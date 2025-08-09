from fastapi import FastAPI

app = FastAPI(title="Profile Matcher Service")

@app.get("/get_client_config/{player_id}")
async def get_client_config(player_id: str):
    # Temporary stub so we can see the server working
    return {"player_id": player_id, "active_campaigns": []}
