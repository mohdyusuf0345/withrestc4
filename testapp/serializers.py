from rest_framework import serializers
from .models import Employee


def multiples_of_1000(value):  # Validation By  Validator Attribute
    if value % 1000 != 0:
        raise serializers.ValidationError('Employee Salary Should Be Multiples of 1000')


class EmployeeSerializer(serializers.ModelSerializer):
    e_sal = serializers.FloatField(validators=[multiples_of_1000])

    class Meta:
        model = Employee
        fields = '__all__'
# class EmployeeSerializer(serializers.Serializer):  # Belongs To 13 Video
#     e_no = serializers.IntegerField()
#     e_name = serializers.CharField(max_length=64)
#     e_sal = serializers.FloatField(validators=[multiples_of_1000])
#     e_addr = serializers.CharField(max_length=64)
#
#     def validate_e_sal  (self, value):   # Field Level Validation
#         if value < 5000:
#             raise serializers.ValidationError('Employee Salary Should Be Minimum 5000')
#         return value
#
    # def validate(self, data):    # Object Level Validation
    #     e_name = data.get('e_name')
    #     e_sal = data.get('e_sal')
    #     if e_name.lower() == 'yusuf':
    #         if e_sal < 50000:
    #             raise serializers.ValidationError("Yusuf Salary Should Be 50000")
    #     return data
#
#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.e_no = validated_data.get('e_no', instance.e_no)
#         instance.e_name = validated_data.get('e_name', instance.e_name)
#         instance.e_sal = validated_data.get('e_sal', instance.e_sal)
#         instance.e_addr = validated_data.get('e_addr', instance.e_addr)
#         instance.save()
#         return instance
