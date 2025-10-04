import argparse
import os


def demo():
    """Try to run a light text generation demo. If transformers is not available
    or model init fails, print the pre-generated fallback output instead.
    """
    try:
        from transformers import pipeline
    except Exception:
        # fallback: print pre-generated output
        fallback = os.path.join(os.path.dirname(__file__), "..", "examples", "outputs", "demo_text_example.txt")
        fallback = os.path.normpath(fallback)
        if os.path.exists(fallback):
            with open(fallback, "r") as f:
                print(f.read())
        else:
            print("Transformers not installed and fallback output not found.")
        return

    try:
        # small model for demo / classroom (runs on CPU)
        generator = pipeline("text-generation", model="distilgpt2")
        prompt = "You are an AI tutor. Write a 3-line, encouraging tip for someone starting with generative AI:"
        out = generator(prompt, max_length=60, num_return_sequences=1, do_sample=True)
        print(out[0]['generated_text'])
    except Exception as e:
        # If model loading or generation fails, use fallback text file
        fallback = os.path.join(os.path.dirname(__file__), "..", "examples", "outputs", "demo_text_example.txt")
        fallback = os.path.normpath(fallback)
        print("Generation failed — showing fallback output. Error:", e)
        if os.path.exists(fallback):
            with open(fallback, "r") as f:
                print(f.read())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', action='store_true', help='Run the example demo')
    args = parser.parse_args()
    if args.example:
        demo()
    else:
        print('Run with --example to execute the demo')
