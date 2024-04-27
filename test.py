from artwork import generate_art
import os

print("generating images")

# generating new folder
os.makedirs("test", exist_ok=True)

for i in range(1, 11):
		filepath = os.path.join("test", f"test-{i}.png")
		generate_art(filepath)

