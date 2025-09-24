import streamlit as st
from generate import generate_from_text, generate_from_image, customize_with_lora, process_sketch
from PIL import Image
import os
import tempfile

st.set_page_config(page_title="AI 3D Room Designer", layout="wide")

st.title("AI-Driven Diffusion and LoRA Models for Customizable 3D Room Visualization")
st.markdown("Enter text, upload sketches or mood boards, and customize your dream room in real-time!")

# Multimodal Input
input_type = st.selectbox("Input Type", ["Text Description", "Sketch", "Mood Board"])

if input_type == "Text Description":
    prompt = st.text_area("Describe your room:", "A cozy modern living room with white curtains and wooden floor")
    if st.button("Generate"):
        with st.spinner("Generating..."):
            image = generate_from_text(prompt)
            st.image(image, caption="Generated Room")
            st.session_state['base_image'] = image

elif input_type == "Sketch":
    uploaded_file = st.file_uploader("Upload Sketch", type=["png", "jpg"])
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.getvalue())
            sketch_path = tmp.name
        processed_sketch = process_sketch(sketch_path)
        st.image(processed_sketch, caption="Processed Sketch")
        prompt = st.text_input("Additional Prompt:")
        if st.button("Generate"):
            with st.spinner("Generating..."):
                image = generate_from_image(sketch_path, prompt)
                st.image(image, caption="Generated Room from Sketch")
                st.session_state['base_image'] = image

elif input_type == "Mood Board":
    uploaded_file = st.file_uploader("Upload Mood Board Image", type=["png", "jpg"])
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.getvalue())
            mood_path = tmp.name
        st.image(mood_path, caption="Mood Board")
        prompt = st.text_input("Describe based on mood board:")
        if st.button("Generate"):
            with st.spinner("Generating..."):
                image = generate_from_image(mood_path, prompt, strength=0.6)
                st.image(image, caption="Generated Room from Mood Board")
                st.session_state['base_image'] = image

# Customization Section
if 'base_image' in st.session_state:
    st.header("Customize Your Design")
    custom_prompt = st.text_area("Customization Instructions:", "Change walls to blue and add a modern sofa")
    if st.button("Refine with LoRA"):
        with st.spinner("Refining..."):
            refined = customize_with_lora(st.session_state['base_image'], custom_prompt)
            st.image(refined, caption="Customized Room")
            st.session_state['base_image'] = refined  # Iterative loop

    # Export to 3D (Basic HTML with Three.js)
    if st.button("Export to 3D View"):
        # Generate simple HTML with Three.js (embed image as texture)
        html = """
        <html><body>
        <script src="https://threejs.org/build/three.js"></script>
        <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);
        const geometry = new THREE.BoxGeometry();
        const material = new THREE.MeshBasicMaterial({ map: new THREE.TextureLoader().load('figures/sample_output_text2img.png') });
        const cube = new THREE.Mesh(geometry, material);
        scene.add(cube);
        camera.position.z = 5;
        function animate() { requestAnimationFrame(animate); cube.rotation.x += 0.01; cube.rotation.y += 0.01; renderer.render(scene, camera); }
        animate();
        </script>
        </body></html>
        """
        st.download_button("Download 3D HTML", html, file_name="3d_room_view.html")

# Sidebar: Metrics from Poster
st.sidebar.header("Project Metrics")
st.sidebar.markdown("""
- Design Quality: 9.2/10
- Customization Accuracy: 96%
- Generation Time: ~10s
- Refinement Time: <5s
""")