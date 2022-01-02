from django.urls import path
from muzica_clasica import views

urlpatterns = [
    path('',views.index, name='home'),

    path('composers/', views.composers_view, name='composers'),
    path('compositions/', views._composition_view, name='_composition'),
    path('catalogues/', views._catalogues_view, name='_catalogues'),

    path('composition/<int:id>', views.compositions_view, name='composition'),
    path('catalogue/<int:id>', views.catalogues_view, name='catalogues'),

    path('composers/composer-add/', views.add_composer, name='composer_add'),
    path('composers/composer-delete/<int:id>', views.delete_composer,
         name='composer_delete'),
    path('composers/composer-edit/<int:id>', views.update_composer,
         name='composer_update'),

    path('compositions/composition-add/', views.add_composition,
         name='composition_add'),
    path('compositions/composition-delete/<int:id>', views.delete_composition,
         name='composition_delete'),
    path('compositions/composition-edit/<int:id>', views.update_composition,
         name='composition_update'),

    path('catalogues/catalogue-add/', views.add_catalogue,
         name='catalogue_add'),
    path('catalogues/catalogue-delete/<int:id>', views.delete_catalogue,
         name='catalogue_delete'),
    path('catalogues/catalogue-edit/<int:id>', views.update_catalogue,
         name='catalogue_update'),
]
