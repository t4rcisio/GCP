from rest_framework.response import Response
from rest_framework import status

def newUser(request):

    dados = request.data

    name = dados["name"]
    mail = dados["mail"]
    password = dados["password"]


    if not name or not mail or not password:
        return Response({"erro": "Parâmetros obrigatórios faltando"}, status=status.HTTP_400_BAD_REQUEST)


    resposta = {
        "mensagem": "Usuário criado com sucesso!",
    }



    return Response(resposta, status=status.HTTP_200_OK)