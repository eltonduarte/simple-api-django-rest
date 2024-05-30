# Uma API simples para estudos

## Pré-requisitos: 
 - Python instalado no computador
```  
https://www.python.org/
```
 
 - Dependências instaladas através do requirements.txt
```  
pip install -r requirements.txt
```

- Iniciar o ambiente virtual
```  
\simple-api-django-rest\env\Scripts>activate
```
 
Iniciar servidor django (neste exemplo usamos o de testes mesmo)
```  
python manage.py runserver
```
Neste ponto sua API deverá está rodando no endereço http://127.0.0.1:8000/.


# Endpoints

Os seguintes endpoints estão configurados:

## Página inicial

- `/` - GET

## Usuários (users)

- `/users` - GET - Lista todos os usuários 
- `/users` - POST - Cria um novo usuário
- `/users/:id` - GET - Lista o usuário com o ID informado 
- `/users/:id` - PUT - Atualiza o usuário com o ID informado 
- `/users/:id` - DELETE - Apaga o usuário com o ID informado 


**Dados válidos para usuários (JSON)**

```
{
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz"
}
```
