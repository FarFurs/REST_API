from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer


@api_view(['GET'])
def getArticle(response):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)    
    return Response(serializer.data)


@api_view(['GET'])
def getComment_all(response):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getComment_to_articles(response):
    comments = Comment.objects.filter(parent_id = None)
    serializer = CommentSerializer(comments, many=True) 
    return Response(serializer.data)


@api_view(['GET'])
def getComment_to_comments(response):
    comments = Comment.objects.exclude(parent_id = None)
    serializer = CommentSerializer(comments, many=True) 
    return Response(serializer.data)

@api_view(['POST'])
def addArticle(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def addComment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
