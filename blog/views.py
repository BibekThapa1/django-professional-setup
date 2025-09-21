from rest_framework import viewsets
from .models import Post
from .serializers import BlogSerializer
from rest_framework.response import Response
from .filters import PostFilter

class BlogViewset(viewsets.ModelViewSet):
    
    def create(self, request):
        try:
            serializer = BlogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    def list(self, request):
        try:
            all = Post.objects.all()
            print(request.GET)
            filterset = PostFilter(request.GET, queryset=all)
            filtered = filterset.qs
            return Response(BlogSerializer(filtered, many=True).data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)