from django.contrib import admin
from evento.models import *

# Register your models here.
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(Autor)
admin.site.register(EventoCientifico)
admin.site.register(ArtigoCientifico)