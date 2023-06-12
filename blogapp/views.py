from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Blog, Tag
from .serializers import BlogListSerializer, BlogDetailSerializer, TagSerializer
from rest_framework.decorators import action
from django.views.static import serve

def manifest(request):
    response = serve(request, 'manifest.json', r'D:\programming\test_tasks\blog_test_task\frontend\build')
    response['Content-Type'] = 'application/manifest+json'
    return response

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BlogListSerializer
        return BlogDetailSerializer

    # Get blog by id
    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        blog = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(blog)
        return Response(serializer.data)
    
    # Get the last 3 blogs
    @action(detail=False, methods=['get'])
    def latest_blogs(self, request):
        latest_blogs = Blog.objects.all().order_by('-created_at')[:3]
        serializer = BlogListSerializer(latest_blogs, many=True)
        return Response(serializer.data)

# Create new tag
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# Get all blogs by a specific tag
class BlogsByTagView(generics.ListAPIView):
    serializer_class = BlogListSerializer

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        return get_list_or_404(Blog, tags__name=tag_name)
