from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup', views.signup, name='signup'),
    path('creatures/', views.creatures_index, name='index'),
    path('creatures/<int:creature_id>/', views.creatures_detail, name='detail'),
    path('creatures/create/', views.CreatureCreate.as_view(), name='creatures_create'), # as_view() returns the CreatureCreate class as a function, because path() requires a function
    path('creatures/<int:pk>/update', views.CreatureUpdate.as_view(), name='creatures_update'),
    path('creatures/<int:pk>/delete', views.CreatureDelete.as_view(), name='creatures_delete'),
    path('creatures/<int:creature_id>/add_feeding', views.add_feeding, name='add_feeding'),
    # associate a toy with a cat (M:M)
    path('creatures/<int:creature_id>/assoc_snack/<int:snack_id>/', views.assoc_snack, name='assoc_snack'),
    # unassociate a toy and cat
    path('creatures/<int:creature_id>/unassoc_snack/<int:snack_id>/', views.unassoc_snack, name='unassoc_snack'),
    path('snacks/', views.SnackList.as_view(), name='snacks_index'),
    path('snacks/<int:pk>/', views.SnackDetail.as_view(), name='snacks_detail'),
    path('snacks/create/', views.SnackCreate.as_view(), name='snacks_create'),
    path('snacks/<int:pk>/update/', views.SnackUpdate.as_view(), name='snacks_update'),
    path('snacks/<int:pk>/delete/', views.SnackDelete.as_view(), name='snacks_delete'),
]