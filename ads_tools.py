# ads_tools.py
from database import SessionLocal, AdCampaign
from dotenv import load_dotenv
from rich.console import Console
import requests, os

load_dotenv()
console = Console()

MCP_URL = os.getenv("MCP_ADS_API_URL", "http://localhost:8001/google-ads/create")  # fallback for fake MCP
MCP_API_KEY = os.getenv("MCP_API_KEY", "mock-key")

def create_campaign(objective: str, budget: str, country: str) -> str:
    """Logs campaign to DB and hits Google ADK MCP endpoint (or mock)."""
    try:
        # Save to database
        session = SessionLocal()
        campaign = AdCampaign(
            objective=objective,
            budget=budget,
            country=country,
            status="pending"
        )
        session.add(campaign)
        session.commit()

        console.print("📡 [bold green]Saved to DB. Sending to Google ADK MCP...[/bold green]")

        # Build payload and headers
        payload = {
            "objective": objective,
            "budget": budget,
            "country": country
        }
        headers = {
            "Authorization": f"Bearer {MCP_API_KEY}",
            "Content-Type": "application/json"
        }

        # Send request to MCP endpoint
        response = requests.post(MCP_URL, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            campaign.status = "created"
            session.commit()
            return data.get("summary", "✅ Campaign successfully deployed via MCP!")
        else:
            campaign.status = "error"
            session.commit()
            return f"❌ MCP failed: {response.status_code} - {response.text}"

    except Exception as e:
        console.print(f"[red]🚨 Error:[/red] {e}")
        return "Final Answer: ❌ Could not complete campaign creation."
