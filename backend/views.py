from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RD
from .models import DB
from .serializer import RDSerializer
from .serializer import DBSerializer
from django.db import connection
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
# from django.utils import timezone
from datetime import datetime

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is not None:

            # Check if user is a superuser
            is_superuser = user.is_superuser

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)

            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'is_superuser': is_superuser
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class RDCreateView(APIView):
    serializer_class = RDSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            emp_id = serializer.validated_data['emp_id']
            member = serializer.validated_data['member']
            position = serializer.validated_data['position']
            remarks = serializer.validated_data['remarks']
            created_at = datetime.now().date()
            
            query = "INSERT INTO backend_rd (emp_id, member, position, remarks, created_at) VALUES (%s, %s, %s, %s, %s)"
            with connection.cursor() as cursor:
                cursor.execute(query, [emp_id, member, position, remarks, created_at])

            return Response({'message': 'RD created successfully'}, status=201)

        return Response(serializer.errors, status=400)
    

class RDListView(APIView):
    serializer_class = RDSerializer

    def get(self, request, format=None):
        # query = "SELECT * FROM backend_rd"
        query = "SELECT emp_id, member, position, remarks, created_at FROM backend_rd"
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()

        rd_list = []
        for row in results:
            rd = {
                'emp_id': row[0],
                'member': row[1],
                'position': row[2],
                'remarks': row[3],
                'Date': row[4],
            }
            rd_list.append(rd)

        return Response(rd_list, status=200)

class DBListView(APIView):
    serializer_class = DBSerializer

    def get(self, request, format=None):
        # query = "SELECT * FROM backend_db"
        query = "SELECT emp_id, member, position, remarks, created_at FROM backend_db"
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()

        rd_list = []
        for row in results:
            rd = {
                'emp_id': row[0],
                'member': row[1],
                'position': row[2],
                'remarks': row[3],
                'Date': row[4],
            }
            rd_list.append(rd)

        return Response(rd_list, status=200)

class DBCreateView(APIView):
    serializer_class = DBSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            emp_id = serializer.validated_data['emp_id']
            member = serializer.validated_data['member']
            position = serializer.validated_data['position']
            remarks = serializer.validated_data['remarks']
            created_at = datetime.now().date()
            
            query = "INSERT INTO backend_db (emp_id, member, position, remarks, created_at) VALUES (%s, %s, %s, %s, %s)"
            with connection.cursor() as cursor:
                cursor.execute(query, [emp_id, member, position, remarks, created_at])

            return Response({'message': 'RD created successfully'}, status=201)

        return Response(serializer.errors, status=400)
