from diffusers import StableDiffusionPipeline
import torch
import os

def demo():
    model_id = "runwayml/stable-diffusion-v1-5"
    # This example assumes a GPU-enabled Colab environment. If you are running locally
    # ensure you have CUDA and the correct torch version installed.
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    prompt = "A minimal, modern illustration of a robot teaching a class, flat vector style"
    image = pipe(prompt, num_inference_steps=20, guidance_scale=7.5).images[0]
    out_path = "examples/outputs/demo_robot_teaching.png"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    image.save(out_path)
    print(f"Saved example to {out_path}")

if __name__ == "__main__":
    demo()
