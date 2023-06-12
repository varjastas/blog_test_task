from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blogapp.models import Blog, Tag
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from io import BytesIO

class BlogAPITests(APITestCase):

    def setUp(self):
        # Creating test data for test scenarios
        self.tag = Tag.objects.create(name='sample-tag')
        
        self.blog1 = Blog.objects.create(title='Blog 1', content='Content 1', full_image=r'full_images/image_1.jpg')
        self.blog1.tags.add(self.tag)
        self.blog2 = Blog.objects.create(title='Blog 2', content='Content 2', full_image=r'full_images/image_2.jpg')
        self.blog2.tags.add(self.tag)
        self.blog3 = Blog.objects.create(title='Blog 3', content='Content 3', full_image=r'full_images/image_3.jpg')
        self.blog3.tags.add(self.tag)

    def test_create_blog(self):
        # Creating new blog using API
        url = reverse('blog-list')
        image_io = BytesIO()
        image = Image.new('RGB', (100, 100), color='blue')
        image.save(image_io, format='JPEG')

        image_file = SimpleUploadedFile("image.jpg", image_io.getvalue(), content_type="image/jpeg")

        data = {
            'title': 'New Blog',
            'content': 'New Content',
            'tags': [self.tag.id],
            'full_image': image_file    
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_tag(self):
        # Creating new tag using API
        url = reverse('tag-list')
        data = {'name': 'New Tag'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_latest_blogs(self):
        # Getting last 3 blogs using API
        url = reverse('blog-latest-blogs')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        
    def test_get_blog_detail(self):
        # Getting specific blog using API
        url = reverse('blog-detail-api', args=[self.blog1.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.blog1.title)
        
    def test_get_blogs_by_tag(self):
        # Getting all blogs by specific tag using API
        url = reverse('blogs-by-tag', args=[self.tag.name])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)