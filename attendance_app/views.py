from rest_framework import viewsets, generics
from .models import Branch, Batch, Subjects, Staff, Students, Attendance, Schema
from .serializers import BranchSerializer, BatchSerializer, SubjectsSerializer, StaffSerializer, StudentsSerializer, AttendanceSerializer, SchemaSerializer
from django_filters.rest_framework import DjangoFilterBackend


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [IsClgAdmin]
    #     elif self.action in "create":
    #         permission_classes = [IsClgAdmin]  
    #     elif self.action in ["update", "partial_update"]:
    #         permission_classes = [IsClgAdmin]
    #     elif self.action == "destroy":
    #         permission_classes = [IsClgAdmin]
    #     else:
    #         permission_classes = [permissions.AllowAny]
    #     return [permission() for permission in permission_classes]

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [IsClgAdmin]
    #     elif self.action in "create":
    #         permission_classes = [IsClgAdmin]  
    #     elif self.action in ["update", "partial_update"]:
    #         permission_classes = [IsClgAdmin]
    #     elif self.action == "destroy":
    #         permission_classes = [IsClgAdmin]
    #     else:
    #         permission_classes = [permissions.AllowAny]
    #     return [permission() for permission in permission_classes]

class SchemaViewSet(viewsets.ModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [IsClgAdmin]
    #     elif self.action in "create":
    #         permission_classes = [IsClgAdmin]  
    #     elif self.action in ["update", "partial_update"]:
    #         permission_classes = [IsClgAdmin]
    #     elif self.action == "destroy":
    #         permission_classes = [IsClgAdmin]
    #     else:
    #         permission_classes = [permissions.AllowAny]
    #     return [permission() for permission in permission_classes]

class SubjectsViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action in "create":
    #         permission_classes = [IsDeptAdmin]  
    #     elif self.action in ["update", "partial_update"]:
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action == "destroy":
    #         permission_classes = [IsDeptAdmin]
    #     else:
    #         permission_classes = [permissions.AllowAny]
    #     return [permission() for permission in permission_classes]

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action in "create":
    #         permission_classes = [IsDeptAdmin]  
    #     elif self.action in ["update", "partial_update"]:
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action == "destroy":
    #         permission_classes = [IsDeptAdmin]
    #     else:
    #         permission_classes = [permissions.AllowAny]
    #     return [permission() for permission in permission_classes]

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action in "create":
    #         permission_classes = [IsDeptAdmin]  
    #     elif self.action in ["update", "partial_update"]:
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action == "destroy":
    #         permission_classes = [IsDeptAdmin]
    #     else:
    #         permission_classes = [permissions.AllowAny]
    #     return [permission() for permission in permission_classes]

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [permissions.IsAuthenticated]
    #     elif self.action in "create":
    #         permission_classes = [IsStaff]  
    #     elif self.action in ["update", "partial_update"]:
    #         permission_classes = [IsStaff]
    #     elif self.action == "destroy":
    #         permission_classes = [IsStaff]
    #     else:
    #         permission_classes = [permissions.AllowAny]
    #     return [permission() for permission in permission_classes]

class StudentFilterView(generics.ListAPIView):
    serializer_class = StudentsSerializer

    queryset = Students.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sem', 'branch', 'batch', 'sec']  # Define fields for filtering

class AttendanceFilterView(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    queryset = Attendance.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['branch', 'batch', 'sem', 'sec', 'subject', 'date']  # Define fields for filtering
