from PIL import Image
import os
def generate_art(filepath):
		img = Image.new("RGBA", (2000, 2000), color = (255, 255, 0, 255))
		img.save(filepath)
  
if __name__ == "__main__":
		print("generating an artwork from art.py")
		os.makedirs("test", exist_ok=True)
		