# main.py
from ads_tools import create_campaign
from rich.console import Console
from rich.prompt import Prompt
from dotenv import load_dotenv
import os

load_dotenv()
console = Console()

def run_cli():
    console.print("\n🤖 [bold cyan]Marv – Google Ads CLI Agent[/bold cyan]\n")

    objective = Prompt.ask("📌 Enter campaign objective (e.g. get more leads)")
    budget = Prompt.ask("💰 Budget (e.g. ₦50000 or $100)")
    country = Prompt.ask("🌍 Target country (e.g. Nigeria, Ghana)")

    console.print("\n[bold blue]Submitting your campaign...[/bold blue]")
    result = create_campaign(objective, budget, country)
    console.print(f"\n[bold yellow]{result}[/bold yellow]")

if __name__ == "__main__":
    run_cli()
