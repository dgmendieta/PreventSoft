from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import DocumentListView, UserListView, EppListView
from .views import HazardListView, PrecautionListView, ToolListView

urlpatterns = [
    path('', views.index, name='index'),
    #documents urls
    path('documents/document', views.document_view, name='document'),
    path('documents/document_list', DocumentListView.as_view(), name='document_list'),
    path('documents/document_edit/<int:pk>/', views.document_edit, name='document_edit'),
    path('documents/document_detail/<int:pk>/', views.document_detail, name='document_detail'),
    path('documents/document_export/<int:pk>/', views.document_export, name='document_export'),
    #users urls
    path('users/user_register', views.user_register, name='user_register'),
    path('users/user_list', UserListView.as_view(), name='user_list'),
    path('users/user_edit/<int:pk>/', views.user_edit, name='user_edit'),
    path('users/user_delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('users/logout', views.logout_view, name='logout'),
    #epp's urls
    path('epps/epp_new', views.epp_new, name='epp_new'),
    path('epps/epp_list', EppListView.as_view(), name='epp_list'),
    path('epps/epp_edit/<int:pk>/', views.epp_edit, name='epp_edit'),
    path('epps/epp_delete/<int:pk>/', views.epp_delete, name='epp_delete'),
    #hazards urls
    path('hazards/hazard_new', views.hazard_new, name='hazard_new'),
    path('hazards/hazard_list', HazardListView.as_view(), name='hazard_list'),
    path('hazards/hazard_edit/<int:pk>/', views.hazard_edit, name='hazard_edit'),
    path('hazards/hazard_delete/<int:pk>/', views.hazard_delete, name='hazard_delete'),
    #precautions urls
    path('precautions/precaution_new', views.precaution_new, name='precaution_new'),
    path('precautions/precaution_list', PrecautionListView.as_view(), name='precaution_list'),
    path('precautions/precaution_edit/<int:pk>/', views.precaution_edit, name='precaution_edit'),
    path('precautions/precaution_delete/<int:pk>/', views.precaution_delete, name='precaution_delete'),
    #tools urls
    path('tools/tool_new', views.tool_new, name='tool_new'),
    path('tools/tool_list', ToolListView.as_view(), name='tool_list'),
    path('tools/tool_edit/<int:pk>/', views.tool_edit, name='tool_edit'),
    path('tools/tool_delete/<int:pk>/', views.tool_delete, name='tool_delete'),
    #admin url
    path('admin/', admin.site.urls),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#if settings.DEBUG:
#	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	