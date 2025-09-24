<p align="center">
  <img src="figures/system_architecture.png" alt="System Architecture" width="600">
</p>

<h1 align="center">AI-Driven Diffusion and LoRA Models for Customizable 3D Room Visualization and Design Enhancement</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/PyTorch-2.0%2B-orange?style=for-the-badge&logo=pytorch" alt="PyTorch">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/stars/yourusername/ai-room-designer?style=for-the-badge" alt="Stars">
  <img src="https://img.shields.io/badge/Design%20Quality-9.2%2F10-green?style=for-the-badge" alt="Design Quality">
</p>

<p align="center">
  <em>Revolutionize interior design with AI: Generate photorealistic 3D rooms from text, sketches, or mood boards, and customize in real-time with LoRA-powered precision. Built for creators, by creators.</em>
</p>

## 🌟 Project Spotlight
In a world where design dreams meet digital reality, this capstone project from Vellore Institute of Technology (VIT) transforms how we visualize spaces. Traditional tools are clunky and exclusive—ours is intuitive, AI-fueled, and accessible to all. Leveraging **Stable Diffusion** for generative magic and **LoRA** for sleek customizations, we bridge creativity and technology to craft immersive 3D room experiences.

From cozy living rooms to sleek offices, input your vision via text ("A minimalist bedroom with ocean views"), upload a sketch, or drop a mood board—watch as AI renders photorealistic designs in seconds. Iterate effortlessly: Swap furniture, tweak lighting, or refine textures without starting over. Backed by rigorous research (30+ references on diffusion, LoRA, and interior AI), this tool addresses key gaps like multimodal support and real-time feedback.

**Key Metrics from User Studies** (as per poster):
- **Design Quality**: 9.2/10 – Praised for realism, coherence, and aesthetics.
- **Customization Accuracy**: 96% – Precise modifications without scene disruption.
- **Performance**: Initial generation ~10s; refinements <5s.
- **User Satisfaction**: High usability for pros and novices alike.

<p align="center">
  <img src="figures/sample_output_text2img.png" alt="Text-to-Image Sample" width="400">
  <img src="figures/sample_output_img2img.png" alt="Image-to-Image Sample" width="400">
</p>

## 🚀 Features That Shine
- **Multimodal Mastery**: Text prompts, sketches (edge-detected with OpenCV), mood boards (style extraction).
- **Diffusion-Powered Generation**: Create initial layouts with Stable Diffusion, trained on interior datasets.
- **LoRA Magic**: Low-rank adaptation for efficient, non-destructive customizations—change colors, furniture, lighting on the fly.
- **Real-Time Refinement Loop**: Iterative feedback for adaptive co-creation.
- **Photorealistic Outputs**: High-res renders exportable as PNG/JPEG/FBX/HTML (with Three.js for 3D interaction).
- **Scalable & Secure**: Modular architecture, GPU-optimized, with cloud-ready deployment.
- **Explainable AI**: Visual logs of changes to build user trust.

## 🛠️ Installation & Setup
1. **Clone the Repo**:
