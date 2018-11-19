from django.urls import path
from . import views
# from django.urls import path include
# from rest_framework_nested import routers
# from views import DomainViewSet, NameserverViewSet


# router = routers.SimpleRouter()
# router.register('schools/', SchoolsViewSet)

# domains_router = routers.NestedSimpleRouter(
# router, 'schools/', lookup='schools/')
# domains_router.register('students/', StudentsViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('schools/', views.schools_list),
    path('schools/<int:pk>/', views.school_detail),
    path('students/', views.students_list),
    path('students/<int:pk>/', views.student_detail),
    # path('^', include(router.urls)),
    # path('^', include(domains_router.urls)),
]
