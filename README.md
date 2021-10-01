
# App de Gestão de Imagens

## Imagens

<p align="center">
  <img src="https://github.com/dg-veiga/django-image-analyser/blob/master/readme-images/index-page.jpg" width="90%" title="Home page">
</p>

<p align="center">
  <img src="https://github.com/dg-veiga/django-image-analyser/blob/master/readme-images/upload-page.jpg" width="90%" title="Upload">
</p>

<p align="center">
  <img src="https://github.com/dg-veiga/django-image-analyser/blob/master/readme-images/image-page.jpg" width="90%" title="Imagem">
</p>

<p align="center">
  <img src="https://github.com/dg-veiga/django-image-analyser/blob/master/readme-images/analysis-modal.jpg" width="90%" title="Modal de análise">
</p>

<p align="center">
  <img src="https://github.com/dg-veiga/django-image-analyser/blob/master/readme-images/delete-image-modal.jpg" width="90%" title="Modal de exclusão">
</p>

## Download e instalação
```bash
$ git clone https://github.com/dg-veiga/django-image-analyser
$ cd django-image-analyser
```

Tendo o docker-compose instalado na sua instância, basta executar o comando:
```bash
$ sudo docker-compose up --build 
```

E para executar depois de instalado: 
```bash
$ sudo docker-compose up
```

Com isso o aplicativo irá rodar automaticamente no localhost:8000.

## Views e endpoints da API
```python
### ===> URLS do site <===
## ====================================================================
path('', index, name='index'),

path('upload-image/', upload_image, name='upload-image'),

path('image/<str:pk>/', get_image, name='get-image'),

path('image/<str:pk>/create-analysis/', create_analysis, name='create-analysis'),

path('api/delete-analysis/<int:aid>/<int:iid>/', delete_analysis, name="delete-analysis"),

path('api/update-analysis/<int:aid>/<int:iid>/', update_analysis, name="update-analysis"),

path('api/delete-image/<int:pk>/', delete_image, name="delete-image"),

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
```

## Trabalhos futuros
- [ ] Construção de testes unitários.
- [ ] Filtrar as tags de datetime para 'Y-m-d H:i'
- [ ] Melhorar população do banco de dados de amostra
