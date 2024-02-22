from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, BatchViewSet, SubjectsViewSet, StaffViewSet, StudentsViewSet, AttendanceViewSet, SchemaViewSet

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
]
