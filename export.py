from artwork import generate_art
import os

print("generating images")

# generating new folder
os.makedirs("exports", exist_ok=True)

filepath = os.path.join("exports", f"export.png")
generate_art(filepath)


