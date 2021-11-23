from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
  
  
class HelloView(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        content = {'message': request.user.username}
        return Response(content)



@api_view(['GET'])
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created. You are now able to login!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form' : form})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def userlist(request):

	if request.method == 'GET' :

		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)


	
	if request.method == 'POST' :

		serializer = UserSerializer(data = request.data)

		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def userlist1(request, pk):


	if request.method == 'GET':

		users = User.objects.get(id=pk)
		serializer = UserSerializer(users, many=False)
		return Response(serializer.data)

	if request.method == 'PUT' :

		user = User.objects.get(id=pk)
		serializer = UserSerializer(instance= user, data = request.data)

		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)

	if request.method == 'DELETE' :

		user = User.objects.get(id=pk)
		user.delete()
		return Response("Item deleted")


@api_view(['GET'])
def game(request):


	lg = 'Bundesliga'
	cn = 'Germany'

	response = requests.get("https://livescore-api.com/api-client/competitions/list.json?key=Qdu97DrMm5SMhnoF&secret=CpSObOZ09Kxl1VfS9K1hns3JyWwQkUvX")

	pass_times = response.json()['data']

	leagues = []

	for d in pass_times['competition']:

	    if len(d['countries']) == 0 :
	        if d['name'] == lg :
	            yu = d['id']
	            leagues.append(yu)
	            print(d)

	    for k in d['countries']:

	        ui = k['name']
	        if d['name'] == lg and ui == cn :
	            yu = d['id']
	            leagues.append(yu)
	            print(d)

	parameters = {
	    'competition_id' : leagues[0]
	}

	scorer = requests.get("https://livescore-api.com/api-client/competitions/goalscorers.json?competition_id=224&key=Qdu97DrMm5SMhnoF&secret=CpSObOZ09Kxl1VfS9K1hns3JyWwQkUvX", params=parameters)

	mn = scorer.json()['data']

	i=0
	for d in mn['goalscorers']:

	    if i >= 1:
	        break
	    else:
	        return Response(d)
	        i=i+1