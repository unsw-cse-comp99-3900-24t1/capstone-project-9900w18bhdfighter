from . import views, groups_views
from rest_framework.routers import SimpleRouter
from django.urls import path

url = SimpleRouter(trailing_slash=False)
url.register(r'api/users', views.UserAPIView)
url.register(r'api/areas', views.AreaAPIView)
url.register(r'api/messages', views.MessageAPIView)
url.register(r'api/contacts', views.ContactAPIView)
url.register(r'api/group-messages', views.GroupMessageAPIView)
url.register(r'api/groups', views.GroupPreferenceAPIView)
url.register(r'api/group-projects', views.GroupProjectsLinkAPIView)
urlpatterns = [
    path("login/", views.student_login, name="student_login"),
    path("project_creation/", views.project_creation, name="project_creation"),
    path("student_signup/", views.student_signup, name="student_signup"),
    path("project_update/<int:id>/", views.project_update, name="project_update"),
    path("group_creation/", views.group_creation, name="group_creation"),
    path("projects/", views.get_projects_list, name="get_projects_list"),
    path("projects/createdBy/<str:email>/", views.get_project_list_creator, name="get_project_list_creator"),
    path("projects/ownBy/<str:email>/", views.get_project_list_owner, name="get_project_list_owner"),
    path("projects/own_and_create/<str:creator>/<str:owner>/", views.get_project_list_owner_creator, name="get_project_list_owner"),
    path("projects/<int:id>/", views.get_project, name="get_project_detail"),
    path("group_join/", views.group_join, name="group_join"),
    path("group_leave/", views.group_leave, name="group_leave"),
    path("groups/<int:id>/", views.get_groups_list_by_project, name="get_group_detail"),
    path("groups/", views.groups_list_del, name="groups_list_del"),
    path('api/notifications', views.create_notification, name='create_notification'),
    path('api/notifications/<int:user_id>/', views.fetch_notifications, name='fetch_notifications'),
    path('api/notifications/<int:notificationReceiverId>/status', views.update_notification_status,name='update_notification_status'),
    path('api/notifications/<int:notificationReceiverId>/delete', views.delete_notification,name='delete_notification'),
    path('api/group-projects/<int:projectID>/<int:groupID>/', views.GroupProjectsLinkAPIView.as_view({'delete': 'destroy'})),
    path('api/groups/autocomplete-name',views.autocomplete_groups,name='autocomplete_groups'),
]


urlpatterns += url.urls