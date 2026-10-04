"""Check local dependencies without showing secrets or calling paid APIs."""

import importlib
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".venv" / "matplotlib-cache"))

packages = {
    "OpenAI": "openai", "Environment variables": "dotenv",
    "Arrays": "numpy", "Dataframes": "pandas", "Charts": "matplotlib",
    "Tokenization": "tiktoken", "Foundry": "azure.ai.inference",
    "Machine learning": "sklearn", "Notebook kernel": "ipykernel",
    "Notebook widgets": "ipywidgets",
    "Browser notebooks": "jupyterlab",
}
failed = False
print(f"Python: {sys.version.split()[0]}")
for name, module in packages.items():
    try:
        importlib.import_module(module)
        print(f"OK: {name}")
    except ImportError:
        print(f"MISSING: {name} ({module})")
        failed = True

if not failed:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")

    def configured(name):
        value = os.getenv(name, "").strip()
        return bool(value) and not value.startswith("<") and "your" not in value.lower()

    for provider, variables in {
        "OpenAI": ["OPENAI_API_KEY"],
        "Azure OpenAI": ["AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT"],
        "Foundry Models": ["AZURE_INFERENCE_ENDPOINT", "AZURE_INFERENCE_CREDENTIAL", "AZURE_INFERENCE_CHAT_MODEL"],
    }.items():
        status = "settings present (not authenticated)" if all(map(configured, variables)) else "needs credentials for API exercises"
        print(f"{provider}: {status}")

print("\nStart with START-HERE.md. Reading and practice.py work without credentials.")
sys.exit(1 if failed else 0)
