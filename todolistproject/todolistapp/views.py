from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import todo
from .models import tag
from .serializers import todoSerializer
from .serializers import tagSerializer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello API!")

@api_view(["GET"])
def todolist(req):
    todos = todo.objects.all()
    serializer = todoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def todocreate(req):
    serializer = todoSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(["DELETE"])
def tododelete(req, pk):
    todo = todo.objects.get(id=pk)
    todo.delete()
    return Response("Delete Success")


@api_view(["PUT"])
def todoupdate(req, pk):
    todo = todo.objects.get(id=pk)
    serializer = todoSerializer(todo, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# @api_view(["GET"])
# def taglist(req):
#     tags = tag.objects.all()
#     serializer = tagSerializer(tags, many=True)
#     return Response(serializer.data)


# @api_view(["POST"])
# def tagcreate(req):
#     serializer = tagSerializer(data=req.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)


# @api_view(["DELETE"])
# def tagdelete(req, pk):
#     tag = tag.objects.get(id=pk)
#     tag.delete()
#     return Response("Delete Success")


# @api_view(["PUT"])
# def tagupdate(req, pk):
#     tag = tag.objects.get(id=pk)
#     serializer = tagSerializer(tag, data=req.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)  
# @api_view(['GET'])
# def randomAPI(request, id):
#     totalCalcs = Calc.objects.all()	# ????????? ???????????? ????????? ?????? ????????????
#     randomCalcs = random.sample(list(totalCalcs), id)   # id??? ???????????? ?????? ??????
#     serializer = CalcSerializer(randomCalcs, many=True) # ????????? ???????????? ?????? ?????????????????? ?????????
#     return Response(serializer.data)

