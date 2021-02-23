from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Blog, Tag
from .serializers import BlogSerializer


@api_view(["GET", "POST"])
def get_post_blogs(request):
    if request.method == "GET":
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


""" FOR THE TAG CREATION
categories = self.request.POST.get('categoriesString').split(',')
for category in categories:
    Category.objects.create(
        project=Project.objects.get(id=self.object.id),
        name=category
    )
"""


@api_view(["GET", "DELETE", "PUT"])
def get_delete_put_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    elif request.method == "DELETE":
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
