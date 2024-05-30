from rest_framework import serializers
from app.models import Users

# Serializando os dados é transformar os dados em objetos JSON
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'username', 'email']