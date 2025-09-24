from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
import torch
from PIL import Image
import cv2  # For sketch processing
import numpy as np

# Load fine-tuned model with LoRA
pipe = StableDiffusionPipeline.from_pretrained("models/lora_adapter", torch_dtype=torch.float16)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
img2img_pipe = StableDiffusionImg2ImgPipeline.from_pretrained("models/lora_adapter", torch_dtype=torch.float16)
img2img_pipe = img2img_pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_from_text(prompt, steps=50):
    image = pipe(prompt, num_inference_steps=steps).images[0]
    return image

def generate_from_image(input_image_path, prompt, strength=0.75):
    init_image = load_image(input_image_path).resize((512, 512))
    image = img2img_pipe(prompt, image=init_image, strength=strength, guidance_scale=7.5).images[0]
    return image

def process_sketch(sketch_path):
    # Edge detection for sketches
    img = cv2.imread(sketch_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(img, 100, 200)
    edges_pil = Image.fromarray(edges)
    return edges_pil

def customize_with_lora(base_image, customization_prompt):
    # Apply LoRA for refinement (simplified; adjust LoRA weights dynamically)
    refined_image = img2img_pipe(customization_prompt, image=base_image, strength=0.5).images[0]
    return refined_image

# Example usage
if __name__ == "__main__":
    text_image = generate_from_text("A cozy modern living room with white curtains and wooden floor")
    text_image.save("figures/sample_output_text2img.png")
    
    sketch = process_sketch("data/sample_inputs/sketch_example.png")
    img_image = generate_from_image(sketch, "Modern bedroom with blue walls")
    img_image.save("figures/sample_output_img2img.png")