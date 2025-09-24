// Use this in exported HTML for interactive 3D view
// Embed generated image as texture on 3D models (e.g., room walls)
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Load generated texture
const loader = new THREE.TextureLoader();
const texture = loader.load('generated_room.png'); // Replace with output path

// Create room geometry (simple box)
const geometry = new THREE.BoxGeometry(10, 5, 10);
const material = new THREE.MeshBasicMaterial({ map: texture, side: THREE.DoubleSide });
const room = new THREE.Mesh(geometry, material);
scene.add(room);

camera.position.z = 15;

function animate() {
    requestAnimationFrame(animate);
    room.rotation.y += 0.005;
    renderer.render(scene, camera);
}
animate();