# Wave-Ring
Growing 3D Jewellery with Pure Python

What if you could grow a piece of jewellery from a single mathematical idea ?
Traditional jewellery is either carved, cast, or forged. But in the age of computational design, we can use logic to define beauty. In this project, I’ll show you how to use a simple Sine Wave the same math that describes sound and light, to generate a high-end, parametric 3D ring.
We aren't using any CAD software or complex 3D modeling tools. We are using 100% Python code and the power of a modern computer to turn raw numbers into a physical Computational Jewel.
Whether you are a coder who wants to wear your work or a maker curious about generative art, this guide will take you from a blank screen to a 3D-printable masterpiece.

Software
- Python 3: This is our design engine. It’s free and open-source.
- Mac Users: Python comes pre-installed. You’ll use IDLE (bundled with Python) to run the script.
- Windows Users: Download it from Python.org. (Make sure to check "Add Python to PATH" during installation).
- 3D Viewer: To see your creation.
Mac: Built-in Quick Look (just hit Spacebar on the file).
Windows: Built-in 3D Viewer app.

Hardware
A Computer: Any modern laptop or desktop.
And optionally a 3D printer to test your results

Before we code, we need to understand the geometry. Our ring is based on a Torus (a donut shape). To make it a Wave Ring, we tell the computer to change the thickness of the band as it travels around your fingers
We use a Sine function to create the ripples: 
- n (Waves): The number of peaks (e.g., 7 waves).
- A (Amplitude): How the ripples are.
- θ (Theta): The angle around the circle (0 to 360∘).
By wrapping this wave around a 3D coordinate system (X,Y,Z), we transform it into a solid, wearable form.

Just run the script in IDLE and it will automatically open an 3D preview, also the ring can be customised by just tuning the values.
