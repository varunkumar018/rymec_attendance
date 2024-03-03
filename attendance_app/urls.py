from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, BatchViewSet, SubjectsViewSet, StaffViewSet, StudentsViewSet, AttendanceViewSet, SchemaViewSet, StudentFilterView, AttendanceFilterView

router = DefaultRouter()
router.register(r'branches', BranchViewSet)
router.register(r'batches', BatchViewSet)
router.register(r'subjects', SubjectsViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'students', StudentsViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'schema', SchemaViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('filter/student/', StudentFilterView.as_view(), name='student_filter'),  # Add path to StudentFilterView

    path('filter/attendance/', AttendanceFilterView.as_view(), name='attendance_filter'),  # Add path to AttendanceFilterView

]
