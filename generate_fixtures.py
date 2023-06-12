import os
import json
from faker import Faker
from random import randint
from PIL import Image

fake = Faker()

# Generate blog data
blogs = []
for _ in range(10):
    blog = {
        "model": "blogapp.blog",
        "pk": _ + 1,
        "fields": {
            "title": fake.sentence(),
            "content": " ".join(fake.paragraphs(nb=3)),
            "created_at": fake.date_time_this_decade().isoformat(),
            "slug": fake.slug(),
        }
    }
    blogs.append(blog)

# Generate tag data
tags = []
for _ in range(10):
    tag = {
        "model": "blogapp.tag",
        "pk": _ + 1,
        "fields": {
            "name": fake.word(),
        }
    }
    tags.append(tag)

# Associate tags with blogs
for blog in blogs:
    num_tags = randint(1, 5)
    blog["fields"]["tags"] = [tag["pk"] for tag in tags[:num_tags]]

# Generate and save image files
image_dir = os.path.join(os.path.dirname(__file__), "media", "full_images")
thumbnail_dir = os.path.join(os.path.dirname(__file__), "media", "thumbnails")
os.makedirs(image_dir, exist_ok=True)

for blog in blogs:
    image_file = os.path.join(image_dir, f"image_{blog['pk']}.jpg")
    image = Image.new("RGB", (200, 200), color=(randint(0, 255), randint(0, 255), randint(0, 255)))
    
    image.save(image_file)
    blog["fields"]["full_image"] = fr"full_images/image_{blog['pk']}.jpg"
    
    thumbnail_file = os.path.join(thumbnail_dir, f"image_{blog['pk']}.jpg")
    thumbnail = image.resize((150, 150))
    thumbnail.save(thumbnail_file)
    blog["fields"]["thumbnail"] = f"thumbnails/image_{blog['pk']}.jpg"

    if os.path.exists(image_file):
        print(f"The file '{image_file}' exists.")
    else:
        print(f"The file '{image_file}' does not exist.")

# Save fixture files
fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")
os.makedirs(fixtures_dir, exist_ok=True)

with open(os.path.join(fixtures_dir, "blogs.json"), "w") as f:
    json.dump(blogs, f, indent=2)

with open(os.path.join(fixtures_dir, "tags.json"), "w") as f:
    json.dump(tags, f, indent=2)
