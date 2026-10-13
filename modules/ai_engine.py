import sys
import ollama
from rich.console import Console
from modules.config import MODEL_NAME, get_system_prompt

console = Console()


def generate_report(scan_data: str, client_name: str, agency_name: str) -> str:
    """Sends the scan data to the local Gemma model and returns the generated report."""
    system_prompt = get_system_prompt(client_name, agency_name)

    try:
        # Gunakan rich status untuk loading spinner
        with console.status(
            f"[bold green]AI ({MODEL_NAME}) is analyzing data and writing the report. Please wait...",
            spinner="bouncingBar",
        ):
            response = ollama.chat(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {
                        "role": "user",
                        "content": f"Here is the live Nmap scan result:\n\n{scan_data}",
                    },
                ],
            )

        console.print("[bold green][+] AI Generation complete.[/bold green]")
        return response.get("message", {}).get("content", "")
    except Exception as e:
        console.print(
            f"[bold red][Error] AI Generation failed. Is Ollama running? Details: {e}[/bold red]"
        )
        sys.exit(1)
