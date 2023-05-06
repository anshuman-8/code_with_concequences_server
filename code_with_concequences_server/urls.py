from django.contrib import admin
from django.urls import path, include
from blank_funds.views import getOrganisation, getOrganisations, createOrganisation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blank_funds.urls'), name='api'),
    # path('api/organisations',getOrganisations),
    # path('api/organisation',getOrganisation),
    # path('api/createOrg',createOrganisation)
]
