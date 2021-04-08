from django.urls import path
from .views import NewCourse,ViewCourse,UpdateCourse,DeleteCourse
urlpatterns=[
    path("new/",NewCourse.as_view(),name="course-new"),
    path("view/",ViewCourse.as_view(),name="course-view"),
    path("update/<int:pk>",UpdateCourse.as_view(),name="course-update"),
    path("delete/<int:pk>",DeleteCourse.as_view(),name="course-delete")

]