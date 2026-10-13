import sys
from pathlib import Path
from rich.console import Console
from markdown_pdf import MarkdownPdf, Section

console = Console()


def save_report(content: str, output_md_path: Path) -> None:
    """Saves the generated Markdown report and automatically exports it to PDF."""
    try:
        output_md_path.parent.mkdir(parents=True, exist_ok=True)

        # 1. Save as Markdown (.md)
        with open(output_md_path, "w", encoding="utf-8") as file:
            file.write(content)
        console.print(f"[bold blue][+] Markdown saved to:[/bold blue] {output_md_path}")

        # 2. Convert and Save as PDF (.pdf)
        pdf = MarkdownPdf(toc_level=0)  # Menonaktifkan Daftar Isi otomatis
        pdf.add_section(Section(content))

        # Mengganti ekstensi file .md menjadi .pdf
        output_pdf_path = output_md_path.with_suffix(".pdf")
        pdf.save(str(output_pdf_path))

        console.print(
            f"[bold blue][+] PDF exported successfully to:[/bold blue] {output_pdf_path}"
        )

    except Exception as e:
        console.print(
            f"[bold red][Error] Failed to save or convert the report: {e}[/bold red]"
        )
        sys.exit(1)
