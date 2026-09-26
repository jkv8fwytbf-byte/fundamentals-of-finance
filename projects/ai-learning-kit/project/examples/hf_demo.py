"""Optional Week 3 exercise. Install torch and transformers in a virtual environment.

First run downloads model files from Hugging Face; subsequent runs can reuse cache.
The classifier runs on CPU. This script was syntax-checked; model weights are not
bundled and the download/inference exercise must be run separately.
"""
import json

def main():
    try:
        from transformers import pipeline
    except ImportError:
        raise SystemExit("Install the optional packages first: python3 -m pip install torch transformers")
    model_id = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    classify = pipeline("sentiment-analysis", model=model_id, device=-1)
    sentences = ["The instructions were clear and the experiment worked.",
                 "The instructions were confusing and the experiment failed.",
                 "Wonderful, another broken installation to spend my evening fixing."]
    print(json.dumps({"model": model_id, "revision": getattr(classify.model.config, "_commit_hash", None),
                      "results": list(zip(sentences, classify(sentences)))}, indent=2))

if __name__ == "__main__":
    main()
