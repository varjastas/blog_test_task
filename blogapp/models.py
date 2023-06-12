from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    tags = models.ManyToManyField(Tag, related_name="blogs")
    full_image = models.ImageField(upload_to='full_images/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Function that creates thumbnail image by resizing full image to 150x150
        
        super().save(*args, **kwargs)

        img = Image.open(self.full_image)

        img.thumbnail((150, 150), Image.ANTIALIAS)

        output = BytesIO()
        img.save(output, format='JPEG', quality=85)
        output.seek(0)
        self.thumbnail = InMemoryUploadedFile(output, 'ImageField', f"{self.full_image.name.split('.')[0]}.jpg", 'image/jpeg', sys.getsizeof(output), None)
        super().save(update_fields=['thumbnail'])