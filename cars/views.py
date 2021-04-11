from rest_framework import viewsets
from cars.models import User, Car
from cars.serializer import UserSerializer, CarSerializer, RegisterSerializer
from rest_framework import filters, generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail

class CarViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = CarSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id']

    def get_queryset(self):
        car = Car.objects.all()
        return car


class UserViewSet(viewsets.ModelViewSet):
     permission_classes = (IsAuthenticated, IsAdminUser)
     serializer_class = UserSerializer

     def get_queryset(self):
         user = User.objects.all()
         return user

     def create(self, request, *args, **kwargs):
         data = request.data
         user = User.objects.create(username=data["username"], email=data["email"], password=make_password(data["password"]))
         user.save()

         for car in data["cars"]:
             car_obj = Car.objects.get(id=car['id'])
             user.cars.add(car_obj)
         serializer = UserSerializer(user)
         return Response(serializer.data)

     def update(self, request, *args, **kwargs):

         data = request.data
         user = User.objects.get(id=self.kwargs['pk'])
         user.username = data["username"]
         user.email = data["email"]
         user.password = make_password(data["password"])
         user.save()

         user.cars.clear()

         for car in data["cars"]:
             car_obj = Car.objects.get(id=car['id'])
             user.cars.add(car_obj)

         serializer = UserSerializer(user)


         # отправка письма пользователю
         #to_mail = user.email

         #send_mail('Subject here', 'Вам назначены машины. ', 'artbazik@gmail.com', [to_mail, ], fail_silently=False, )

         return Response(serializer.data)


class UserCreate(generics.CreateAPIView):
     permission_classes = (IsAuthenticated, IsAdminUser)
     queryset = User.objects.all()
     serializer_class = UserSerializer


class UserUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(generics.GenericAPIView):

    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

