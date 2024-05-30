# As views são funções que são chamadas ao acessar determinada url (urls.py), com o objetivo de enviar e receber dados

# Imports default
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Model é a representação de algum objeto.
from app.models import Users

# Serializando os dados é transformar os dados em objetos JSON
from app.serializers import UsersSerializer

# Decorators com os verbos permitidos
@api_view(['GET', 'POST'])
def listar_inserir_usuarios(request):
    if request.method == 'GET':
        # Todo.objects.all() retorna um dado do tipo QuerySet, que é basicamente uma lista de todos os objetos de uma determinada classe
        users = Users.objects.all()
        # Serializa a lista de objetos, transforma num JSON
        serializer = UsersSerializer(users, many = True)
        # Response
        return Response(serializer.data)
    

    if request.method == 'POST':
        # Pega os dados da requisição e tenta transformar em JSON
        serializer = UsersSerializer(data = request.data)
        
        # Salva se os dados inseridos estivem no formato correto
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Decorators com os verbos permitidos 
@api_view(['GET', 'PUT', 'DELETE'])
def atualizar_deletar_usuarios(request, pk):
    try:
        users = Users.objects.get(pk = pk)
    except Users.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    # Se a requisição for GET, vai transformar num objeto JSON e vai retornar os dados
    if request.method == 'GET':
        serializer = UsersSerializer(users)
        return Response(serializer.data)
    
    # Se a requisição for PUT, temos que validar se a requisição que chegou esta valida
    elif request.method == 'PUT':
        serializer = UsersSerializer(users, data = request.data)
        
        # Se estiver valida, salvamos e retornar ele salvo
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)        
        
        # Se estiver inválida
        return Response(serializer.erros, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        users.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)