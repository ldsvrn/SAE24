from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("sensors/liste",views.liste_sensors),
    path('sensors/modif/<int:id>', views.modif_sensors),
    path('sensors/save/<int:id>', views.save_modif_sensors),
    path('sensors/data/<int:id>', views.filtre_par_sensor),
    path('sensors/csv/<int:id>', views.export_csv),
    path('sensors/filtre_liste/<int:id>', views.filtre_par_date_et_capteur),
    path('sensors/filtre/<int:id>', views.page_filtre_sensors),

    
    path('data/liste', views.liste_data),
    path('data/filtre', views.page_filtre),
    path('data/liste_filtre', views.filtre_par_date)
]
