import argparse
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

from modules.scanner import run_nmap_scan
from modules.ai_engine import generate_report
from modules.utils import save_report

console = Console()


def print_banner():
    """Prints a beautiful terminal banner."""
    banner = """[bold cyan]Local SecOps Reporter[/bold cyan]
[white]AI-Powered Nmap Analyzer & Report Generator[/white]"""
    console.print(Panel(banner, expand=False, border_style="cyan"))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Local SecOps Reporter - Live Nmap AI Analyzer"
    )

    parser.add_argument(
        "-t", "--target", type=str, required=True, help="Target IP or Domain to scan"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("output/client_report.md"),
        help="Path to save the generated report",
    )
    parser.add_argument(
        "--nmap-flags",
        type=str,
        default="-sV -F",
        help="Custom Nmap flags (default: '-sV -F')",
    )

    # Fitur Baru: Personalisasi Bisnis
    parser.add_argument(
        "--client",
        type=str,
        default="Confidential Client",
        help="Name of the client receiving the report",
    )
    parser.add_argument(
        "--agency",
        type=str,
        default="Independent Security Consultant",
        help="Name of your agency",
    )

    args = parser.parse_args()

    # Cetak Banner Aplikasi
    print_banner()

    # 1. Pipeline Start: Lakukan Scan Live
    live_scan_content = run_nmap_scan(args.target, args.nmap_flags)

    # 2. Process with AI
    report_content = generate_report(live_scan_content, args.client, args.agency)

    # 3. Save output & Export to PDF
    if report_content:
        save_report(report_content, args.output)
    else:
        console.print(
            "[bold yellow][-] Warning: The AI generated an empty response.[/bold yellow]"
        )


if __name__ == "__main__":
    main()
