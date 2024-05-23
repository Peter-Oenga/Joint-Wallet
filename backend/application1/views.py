from django.http import Http404
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework import generics
from .serializers import MemberSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MonthlySaving, Fine
from .serializers import MonthlySavingSerializer, FineSerializer
from django.utils import timezone



MINIMUM_SAVINGS = 400.00
FINE_AMOUNT = 50.00

class MemberListView(APIView):
    def get(self, request):
        members = CustomUser.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MemberDetailView(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        member = self.get_object(pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk):
        member = self.get_object(pk)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        member = self.get_object(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
def index(request):
    return render(request, "index.html", {})

def inner_page(request):
    return render(request, "inner-page.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have succesfully logged in!')
            return redirect('index')
        
        else:
            messages.success(request, "There was a problem please try again later")
            return redirect('login')

    else:
        return render(request, "login.html", {})
    

def logout_user(request):
    pass

def register(request):
    return render(request, "register.html", {})

class MemberListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = MemberSerializer

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = MemberSerializer


class MonthlySavingListCreateAPIView(generics.ListCreateAPIView):
    queryset = MonthlySaving.objects.all()
    serializer_class = MonthlySavingSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        member_id = data.get('member')
        savings_amount = float(data.get('savings_amount'))

        # Create the saving record
        response = super().create(request, *args, **kwargs)
        
        # Check if savings meet the minimum requirement
        if savings_amount < MINIMUM_SAVINGS:
            Fine.objects.create(
                member_id=member_id,
                fine_amount=FINE_AMOUNT,
                fine_date=timezone.now().date()
            )
        
        return response

class MonthlySavingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonthlySaving.objects.all()
    serializer_class = MonthlySavingSerializer

class FineListAPIView(generics.ListAPIView):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer

class FineDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer
