# main.py
from ads_tools import create_campaign, optimize_campaign, generate_report
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from dotenv import load_dotenv
import os

load_dotenv()
console = Console()

def run_cli():
    console.print("\n🤖 [bold cyan]Marv – Google Ads CLI Agent[/bold cyan]\n")
    console.print("1. Create Campaign\n2. Optimize Campaign\n3. Generate Report")
    choice = IntPrompt.ask("\nWhat would you like to do?", choices=["1", "2", "3"])

    if choice == 1:
        objective = Prompt.ask("📌 Enter campaign objective")
        budget = Prompt.ask("💰 Budget")
        country = Prompt.ask("🌍 Target country")
        console.print("[blue]Submitting your campaign...[/blue]")
        result = create_campaign(objective, budget, country)

    elif choice == 2:
        objective = Prompt.ask("🎯 Enter objective to optimize")
        result = optimize_campaign(objective)

    else:
        campaign_id = Prompt.ask("🆔 Enter Campaign ID")
        result = generate_report(campaign_id)

    console.print(f"\n[yellow]{result}[/yellow]")

if __name__ == "__main__":
    run_cli()
