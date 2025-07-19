# fake_mcp_api.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class CampaignRequest(BaseModel):
    objective: str
    budget: str
    country: str

@app.post("/google-ads/create")
async def create_campaign(data: CampaignRequest):
    print(f"🎯 Campaign received: {data}")
    
    return JSONResponse(content={
        "status": "success",
        "campaign_id": "ADK-2025-XYZ987",
        "summary": f"📈 Campaign to '{data.objective}' in {data.country} with budget {data.budget} has been created."
    })
