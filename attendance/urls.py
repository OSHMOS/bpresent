from django.contrib import admin
from django.urls import path
from .views import base_views, card_views, name_views

urlpatterns = [
    # base_views
    path('', base_views.index, name='index'),
    path('how', base_views.how, name='how'),
    path('profile/', base_views.profile, name='profile'),
    path('privacy/', base_views.privacy, name='privacy'),
    # card_views
    path('list/', card_views.CardListView.as_view(), name='card_list'),
    path('detail/<int:pk>', card_views.CardDetailView.as_view(), name='card_detail'),
    path('create/', card_views.CardCreateView.as_view(), name='card_create'),
    path('update/<int:pk>', card_views.CardUpdateView.as_view(), name='card_update'),
    path('delete/<int:pk>', card_views.CardDeleteView.as_view(), name='card_delete'),
    path('create/csv/<int:pk>', card_views.card_to_csv, name='card_to_csv'),
    # name_views
    path('name/create/<int:pk>', name_views.name_create, name='name_create'),
    path('name/update/<int:name_id>', name_views.name_update, name='name_update'),
    path('name/delete/<int:name_id>', name_views.name_delete, name='name_delete'),
    path('name/attend/<int:name_id>', name_views.name_attend, name='name_attend'),
    path('name/late/<int:name_id>', name_views.name_late, name='name_late'),
    path('name/absent/<int:name_id>', name_views.name_absent, name='name_absent'),
]
