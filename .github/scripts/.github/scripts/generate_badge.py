import os
import json

# Konfigurasi folder dan badge label
config = {
    "wallpaper": {
        "keyword": "img",
        "label": "Wallpaper Desktop"
    },
    "portrait": {
        "keyword": "PTR",
        "label": "Wallpaper Portrait"
    }
}

output_dir = "badges"
os.makedirs(output_dir, exist_ok=True)

def count_files_containing(folder, keyword):
    count = 0
    for filename in os.listdir(folder):
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
            continue
        if keyword.lower() in filename.lower():
            count += 1
    return count

# Proses setiap folder
for folder, info in config.items():
    keyword = info["keyword"]
    label = info["label"]
    count = count_files_containing(folder, keyword)

    badge = {
        "schemaVersion": 1,
        "label": label,
        "message": f"{count} files",
        "color": "blue"
    }

    # Simpan file badge
    filename = label.lower().replace(" ", "-")  # contoh: wallpaper-desktop.json
    with open(os.path.join(output_dir, f"{filename}.json"), "w") as f:
        json.dump(badge, f)
