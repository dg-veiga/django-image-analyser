from django.conf.urls import url 
from django.urls import path
from .views import *

app_name = 'base'
 
urlpatterns = [ 
    
    ### ===> URLS do site <===
    ## ====================================================================
    path('', index, name='index'),
    
    path('upload-image/', upload_image, name='upload-image'),

    path('image/<str:pk>/', get_image, name='get-image'),

    path('image/<str:pk>/create-analysis/', create_analysis, name='create-analysis'),

    ### ===> URLS da API <===
    ## ====================================================================
    # lista todas as imagens
    path('api/images/', get_images_api, name='get-images-api'),

    # cria imagens com o endereço
    path('api/image/create-image/', create_image_api, name="create-image-api"),

    # retorna dados das imagens com análises
    path('api/image/<int:pk>/', get_image_api, name="get-image-api"),

    # deleta imagens e análises relaciondas
    path('api/delete-image/<int:pk>/', delete_image_api, name="delete-image-api"),

    # cria análise da imagem com id=pk
    path('api/image/<int:pk>/create-analysis/', create_analysis_api, name="create-analysis-api"),

    # deleta análise com id=pk
    path('api/update-analysis/<int:pk>/', update_analysis_api, name="update-analysis-api"),

    # deleta análise com id=pk
    path('api/delete-analysis/<int:pk>/', delete_analysis_api, name="delete-analysis-api"),

    # lista todas as análises
    path('api/analyses/', analyses_list_api, name="analyses-list-api"),
]