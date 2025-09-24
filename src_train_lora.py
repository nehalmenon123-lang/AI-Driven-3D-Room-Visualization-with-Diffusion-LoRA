import torch
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
from diffusers.utils import load_image
from peft import LoraConfig, get_peft_model
from datasets import load_dataset
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import os

# Load base Stable Diffusion model
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Apply LoRA configuration for efficient fine-tuning
lora_config = LoraConfig(
    r=16,  # Rank
    lora_alpha=32,
    target_modules=["to_q", "to_v", "to_k", "to_out.0"],  # UNet attention layers
    lora_dropout=0.1,
    bias="none"
)
pipe.unet = get_peft_model(pipe.unet, lora_config)

# Load dataset (e.g., from Hugging Face or local)
# Assume dataset has 'image' and 'text' columns
dataset = load_dataset("path/to/room_dataset", split="train")  # Or local: load_dataset("imagefolder", data_dir="data/room_dataset")
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

# Training loop (fine-tune on interior design data)
optimizer = torch.optim.AdamW(pipe.unet.parameters(), lr=1e-4)
num_epochs = 5

for epoch in range(num_epochs):
    for batch in dataloader:
        images = batch["image"]
        texts = batch["text"]
        # Preprocess and train (simplified; use full diffusers trainer for production)
        latents = pipe.vae.encode(images).latent_dist.sample()
        noise = torch.randn_like(latents)
        timesteps = torch.randint(0, pipe.scheduler.num_train_timesteps, (latents.shape[0],), device=latents.device)
        noisy_latents = pipe.scheduler.add_noise(latents, noise, timesteps)
        # Forward pass and loss (noise prediction)
        noise_pred = pipe.unet(noisy_latents, timesteps, encoder_hidden_states=texts).sample
        loss = torch.nn.functional.mse_loss(noise_pred, noise)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}/{num_epochs} completed.")

# Save LoRA adapter
pipe.save_pretrained("models/lora_adapter")

# Generate sample and plot
prompt = "A cozy modern living room with white curtains and wooden floor"
image = pipe(prompt, num_inference_steps=50).images[0]
image.save("figures/sample_output_text2img.png")
plt.imshow(image)
plt.title("Sample Text-to-Image Output")
plt.show()