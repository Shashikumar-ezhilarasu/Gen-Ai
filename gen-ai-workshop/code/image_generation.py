import os


def demo():
    """Attempt to run diffusers pipeline. If libraries or CUDA are not available,
    print a message and point to the fallback SVG/PNG in examples/outputs.
    """
    try:
        from diffusers import StableDiffusionPipeline
        import torch
    except Exception:
        print("diffusers/torch not available — using pre-generated example in examples/outputs/")
        fallback = os.path.join(os.path.dirname(__file__), "..", "examples", "outputs", "demo_image_example.svg")
        print("Fallback image:", os.path.normpath(fallback))
        return

    # Check for CUDA available; if not, fail gracefully
    if not torch.cuda.is_available():
        print("CUDA not available — image generation requires GPU. Use the fallback image in examples/outputs/")
        fallback = os.path.join(os.path.dirname(__file__), "..", "examples", "outputs", "demo_image_example.svg")
        print("Fallback image:", os.path.normpath(fallback))
        return

    try:
        model_id = "runwayml/stable-diffusion-v1-5"
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
        pipe = pipe.to("cuda")
        prompt = "A minimal, modern illustration of a robot teaching a class, flat vector style"
        image = pipe(prompt, num_inference_steps=20, guidance_scale=7.5).images[0]
        out_path = os.path.join(os.path.dirname(__file__), "..", "examples", "outputs", "demo_image_example.png")
        out_path = os.path.normpath(out_path)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        image.save(out_path)
        print(f"Saved example to {out_path}")
    except Exception as e:
        print("Image generation failed:", e)
        fallback = os.path.join(os.path.dirname(__file__), "..", "examples", "outputs", "demo_image_example.svg")
        print("Using fallback image:", os.path.normpath(fallback))


if __name__ == "__main__":
    demo()
