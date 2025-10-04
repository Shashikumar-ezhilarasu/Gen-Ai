from transformers import pipeline
import argparse

def demo():
    # small model for demo / classroom (runs on CPU)
    generator = pipeline("text-generation", model="distilgpt2")
    prompt = "You are an AI tutor. Write a 3-line, encouraging tip for someone starting with generative AI:"
    out = generator(prompt, max_length=60, num_return_sequences=1, do_sample=True)
    print(out[0]['generated_text'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', action='store_true', help='Run the example demo')
    args = parser.parse_args()
    if args.example:
        demo()
    else:
        print('Run with --example to execute the demo')
