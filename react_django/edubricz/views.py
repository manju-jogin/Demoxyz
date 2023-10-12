from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Student,Parent
from .serializers import StudentSerializer,ParentSerializer
from rest_framework import exceptions

def get_student_data(self, filters={}):
    queryset = self.filter_queryset(self.get_queryset())
    queryset1 = queryset.order_by('roll_no')
    serializer = self.get_serializer(queryset1, many=True)
    return serializer.data


class StudentViewSet(viewsets.ModelViewSet):
    filterset_fields = ['first_name','last_name','standrad','roll_no','date_of_birth','phone','gender']
    serializer_class = StudentSerializer
    http_method_names = ['get','post']

    def get_queryset(self):
        queryset = Student.objects.all()
        standard = self.request.query_params.get('standard')
        if standard is not None:
            queryset = queryset.filter(standrad=standard)
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset1 = queryset.order_by('roll_no')
        serializer = self.get_serializer(queryset1, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            custom_data = {"message": "Student created successfully","student_id": student.id,}
            return Response(custom_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            updated_student = serializer.save()
            custom_data = {"message": "Student updated successfully","student_id": updated_student.id,}
            return Response(custom_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        custom_data = {
            "message": "Student deleted successfully",
            "student_id": instance.id,
        }
        return Response(custom_data, status=status.HTTP_204_NO_CONTENT)
    
# class ParentViewSet(viewsets.ModelViewSet):
#     serializer_class = ParentSerializer
#     queryset = Parent.objects.all()

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         standard = self.request.query_params.get('standard')
#         if standard is not None:
#             queryset = queryset.filter(student__standrad=standard)
#         return queryset
    
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         queryset = queryset.order_by('father_name')
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

        







    
