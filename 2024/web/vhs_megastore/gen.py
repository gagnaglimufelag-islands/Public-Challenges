import yaml
from pathlib import Path 

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

# Read the owner.json file
with open(HERE / "server/owners.json", "r") as f:
    owner_data = f.read()

# Replace the keyword "FLAG" with the actual flag
modified_owner_data = owner_data.replace("FLAG", "1221 Bowery St, Brooklyn, NY 11224, USA. "+FLAG)

# Write the modified data back to the owner.json file
with open(HERE / "server/owners.json", "w") as f:
    f.write(modified_owner_data)