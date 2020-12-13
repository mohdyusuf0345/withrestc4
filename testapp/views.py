from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # Class Level Hide Csrf
from django.utils.decorators import method_decorator  # Class Level Hide Csrf
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')  # Post Class Level Hide Csrf
class EmployeeCrudCbv(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        p_data = JSONParser().parse(stream)
        id = p_data.get('id', None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        p_data = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=p_data)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Resource Create Successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        p_data = JSONParser().parse(stream)
        id = p_data.get('id')
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp, data=p_data)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Resource Updated Successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        p_data = JSONParser().parse(stream)
        id = p_data.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = {'msg': 'Resource Deleted Successfully'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')
