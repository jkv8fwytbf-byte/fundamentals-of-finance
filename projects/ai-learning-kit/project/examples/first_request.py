"""One real API request, using a current zero-price model you choose.

From project/: python3 examples/first_request.py MODEL_ID
Requires OPENROUTER_API_KEY. See README.md. Never prints the key.
"""
import json
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lab import LabError, OpenRouter, catalog, eligible, save_json

def main():
    if len(sys.argv) != 2:
        raise LabError("Supply one model ID from: python3 compare.py models --free")
    client = OpenRouter(os.environ.get("OPENROUTER_API_KEY"))
    models = {m["id"]: m for m in catalog()}
    model = models.get(sys.argv[1])
    if model is None or not eligible(model):
        raise LabError("Choose a currently available, compatible zero-price model.")
    request = {"model": model["id"], "messages": [{"role": "user", "content":
               "Explain the difference between a model and a provider in two sentences."}],
               "max_tokens": 180, "temperature": 0, "stream": False}
    response = client.complete(model, request)
    save_json(Path(__file__).resolve().parents[1] / "runs/first-response.json", response)
    print(json.dumps(response, indent=2))

if __name__ == "__main__":
    try: main()
    except LabError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(2)
