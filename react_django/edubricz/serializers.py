from rest_framework import serializers
from .models import Student, Parent, Subject, Marks

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'