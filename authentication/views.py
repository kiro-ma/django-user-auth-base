from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db import IntegrityError, transaction
from django.contrib.auth.models import User

class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Você está autenticado!'}
        return Response(content)
    
    def post(self, request):
        user_obj = request.data

        try:
            with transaction.atomic():
                User.objects.create_user(**user_obj)

            return Response(status=201)

        except IntegrityError as e:
            print(f"Integrity error: {e}")
            return Response({"detail": "Dados inválidos ou duplicados."}, status=400)

        except Exception as e:
            print(f"Error: {e}")
            return Response({"detail": "Ocorreu um erro ao criar o usuário."}, status=500)

