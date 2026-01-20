import os
import sys
import datetime

# Cách dùng: python3 chall.py <Event> <Category> <Challenge_Name>
# Ví dụ: python3 chall.py TetCTF Web SimpleUpload
now = datetime.datetime.now() 
def create_structure():
    if len(sys.argv) < 4:
        print("Usage: python init_chal.py <Event> <Category> <Challenge_Name>")
        return

    event = sys.argv[1]
    category = sys.argv[2]
    chal_name = sys.argv[3]
    year = str(now.year) #current year 

    
    path = os.path.join(year, event, category, chal_name)
    
    
    os.makedirs(os.path.join(path, "files"), exist_ok=True)
    os.makedirs(os.path.join(path, "images"), exist_ok=True)

    readme_path = os.path.join(path, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# {chal_name}\n\n")
            f.write(f"**Category:** {category}\n")
            f.write("**Event:** " + event + "\n\n")
            f.write("## Description\n> ...\n\n")
            f.write("## Solution\nWriteup here...\n")   
    
    print(f"[+] Created challenge structure at: {path}")

if __name__ == "__main__":
    create_structure()
