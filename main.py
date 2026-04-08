import math
 
def create_wave_ring_obj(filename="parametric_wave_ring.obj"):
    print("Calculating vertices for the computational jewel...")
    vertices = []
    faces = []
    

    R = 10.0       # Main radius of the ring (in mm)
    r_base = 1.5   # Base thickness
    segments = 150 # Smoothness around the finger
    sides = 40     # Smoothness of the band's curvature
    waves = 5      #  waves around the ring
    wave_amp = 0.6 #  the thickness changes 
    
  
    for i in range(segments):
        theta = 2.0 * math.pi * i / segments
        
      
        r_current = r_base + wave_amp * math.sin(waves * theta)
        
        for j in range(sides):
            phi = 2.0 * math.pi * j / sides
      
            x = (R + r_current * math.cos(phi)) * math.cos(theta)
            y = (R + r_current * math.cos(phi)) * math.sin(theta)
            z = r_current * math.sin(phi)
            
            vertices.append((x, y, z))

    for i in range(segments):
        next_i = (i + 1) % segments
        for j in range(sides):
            next_j = (j + 1) % sides
            
            v1 = i * sides + j + 1
            v2 = next_i * sides + j + 1
            v3 = next_i * sides + next_j + 1
            v4 = i * sides + next_j + 1
            
    
            faces.append((v1, v2, v3))
            faces.append((v1, v3, v4))
            
   
    print(f"Writing {len(vertices)} vertices and {len(faces)} faces to {filename}...")
    with open(filename, 'w') as f:
        f.write("# Generative Wave Ring - Pure Python\n")
        for v in vertices:
            f.write(f"v {v[0]:.4f} {v[1]:.4f} {v[2]:.4f}\n")
        for face in faces:
            f.write(f"f {face[0]} {face[1]} {face[2]}\n")
            
    print(f"Success! {filename} is ready for rendering.")
 
create_wave_ring_obj()
import os
import platform
 
 
 
if __name__ == "__main__":
    filename = "parametric_wave_ring.obj"
    create_wave_ring_obj(filename)
    
    # Check if the user is on Mac or Windows and open the file
    if platform.system() == "Darwin":       # macOS
        os.system(f"open {filename}")
    elif platform.system() == "Windows":    # Windows
        os.startfile(filename)

