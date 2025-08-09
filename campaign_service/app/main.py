from fastapi import FastAPI

app = FastAPI(title="Campaigns Service")

@app.get("/campaigns")
async def list_campaigns():
    # Temporary stub so we can see the server working
    return []
