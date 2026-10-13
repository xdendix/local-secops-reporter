import subprocess
import sys
from rich.console import Console

console = Console()


def run_nmap_scan(target: str, nmap_flags: str) -> str:
    """Runs Nmap directly from Python and captures the output in memory."""
    console.print(
        f"[bold cyan][*] Starting live Nmap scan on target:[/bold cyan] [bold white]{target}[/bold white]"
    )
    console.print(f"[cyan][*] Using Nmap flags:[/cyan] {nmap_flags}")
    console.print("[cyan][*] Streaming live Nmap output...[/cyan]\n")

    try:
        command = ["nmap"] + nmap_flags.split() + [target]
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )

        scan_output = []
        if process.stdout:
            for line in process.stdout:
                # Cetak ke terminal dengan warna redup (dim) agar tidak mencolok
                console.print(line, end="", style="dim")
                scan_output.append(line)

        process.wait()

        if process.returncode != 0:
            console.print(
                f"\n[bold red][Error] Nmap scan failed with return code {process.returncode}.[/bold red]"
            )
            sys.exit(1)

        console.print(
            "\n[bold green][+] Nmap scan completed successfully.[/bold green]"
        )
        return "".join(scan_output)

    except FileNotFoundError:
        console.print(
            "[bold red][Error] Nmap is not installed. Run 'sudo apt install nmap'.[/bold red]"
        )
        sys.exit(1)
    except KeyboardInterrupt:
        console.print(
            "\n[bold yellow][-] Nmap scan cancelled by user (KeyboardInterrupt).[/bold yellow]"
        )
        sys.exit(1)
