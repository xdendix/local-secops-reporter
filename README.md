# Local SecOps Reporter

An AI-powered, completely offline Command Line Interface (CLI) tool designed for Cybersecurity Freelancers and Penetration Testers. It automates the process of running Nmap scans and generating professional, client-ready Executive Summary PDFs using a local LLM.

**Built for the Hacktoberfest 2026 "Side Hustle" Challenge.**

## Why This Exists (The Side Hustle)

As a cybersecurity consultant, scanning a client's infrastructure is fast, but writing the report takes hours. However, feeding sensitive client infrastructure data (like vulnerable open ports) into third-party APIs like ChatGPT is a massive breach of Data Privacy and Non-Disclosure Agreements (NDAs).

This tool solves that by utilizing Google's **Gemma 2B** open-weight model running 100% locally on your machine.

- **Absolute Data Privacy:** Zero data leaves your laptop.
- **Zero Cost:** $0 API costs, maximizing freelance profit margins.
- **Client Ready:** Automatically converts the AI output into a beautifully formatted PDF with customized agency branding.

## Features

- **End-to-End Automation:** Runs Nmap, captures the output, analyzes vulnerabilities, and exports a PDF in one single command.
- **Dynamic Branding:** Inject your client's name and your agency's name directly into the report via CLI arguments.
- **Beautiful Terminal UI:** Built with `rich` to provide live streaming logs and elegant loading spinners so you always know what the script is doing.
- **Offline First:** Powered by Ollama and Gemma 2B. No internet connection required for the AI analysis.

## Prerequisites

Before running this tool, ensure you have the following installed on your Ubuntu/Linux system:

1. **Python 3.10+**
2. **Nmap** (`sudo apt install nmap`)
3. **Ollama** (Running locally with the `gemma2:2b` model pulled: `ollama run gemma2:2b`)

## Installation

1. Clone this repository:

   ```bash
   git clone [https://github.com/yourusername/local-secops-reporter.git](https://github.com/yourusername/local-secops-reporter.git)
   cd local-secops-reporter
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   _(Or manually install: `pip install rich markdown-pdf ollama`)_

## Usage

Run the tool using the following command structure:

```bash
python main.py -t <TARGET> --client "<CLIENT_NAME>" --agency "<AGENCY_NAME>"
```

### Examples:

**1. Default Quick Scan:**

```bash
python main.py -t scanme.nmap.org --client "Acme Corporation" --agency "Dendi Security Labs"
```

**2. Deep Scan with Custom Nmap Flags & Specific Output Name:**

```bash
python main.py -t scanme.nmap.org --nmap-flags "-p- -A --script vuln" --client "Acme Corp" --agency "Dendi Sec" -o output/deep_scan_report.md
```

_(Note: The tool will automatically generate both the `.md` and `.pdf` files in the output directory)._

## Project Structure

```text
local-secops-reporter/
├── modules/
│   ├── __init__.py
│   ├── config.py          # AI System Prompts and configurations
│   ├── scanner.py         # Nmap execution and real-time streaming
│   ├── ai_engine.py       # Ollama LLM integration
│   └── utils.py           # Markdown saving and Auto-PDF export
├── input/
├── output/                # Generated reports go here
├── main.py                # Main CLI entry point
├── requirements.txt       # Python dependencies
├── .gitignore             # Ignored files (venv, outputs, cache)
└── README.md
```

## ⚠️ Disclaimer

This tool is designed for educational purposes and authorized security auditing only. Do not use this tool to scan targets without explicit, written permission from the system owner.
