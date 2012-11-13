# coding: utf-8
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, DetailView, ListView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from busao.models import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'config.views.home', name='home'),
    # url(r'^config/', include('config.foo.urls')),


    url(r'^$', ListView.as_view(model=Cidade, template_name='home.html'), name='home'),
    url(r'^consulta/$', 'busao.views.consulta', name='consulta'),




    # url(r'^$', 'venda.views.vendas', name='home'),
    #url(r'^home$', TemplateView.as_view(template_name='home.html'), name='home'),
    #url(r'^consulta/$', TemplateView.as_view(template_name='consulta.html'), name='consulta'),
    # url(r'^consulta/$', 'venda.views.consulta', name='consulta'),

    url(r'^identificar-se/$', TemplateView.as_view(template_name='identificar.html'), name='identificar-se'),
    url(r'^cadastro/$', 'cliente.views.cliente_cadastro', name='cadastro'),

    #url(r'^home/$', 'cliente.views.consulta', name='consulta'),
    url(r'^consulta/$', 'consulta.views.Consulta_Venda', name='comprar'),
    url(r'^consultalugar/$', 'venda.views.escolherlugar', name='proximo'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # # contato
    # url(r'^contato/send/$', 'app.contato.views.contato_send', name='contato_send'),

    # # project
    # url(r'^$', include('app.appsite.urls', namespace='appsite')),
    # # url(r'^exposicao/$', 'app.appsite.views.exposicao', name='exposicao'),
    # url(r'^exposicao/(?P<slug>[\w_-]+)/?$', DetailView.as_view(queryset=Exposicao.objects.filter(ativo=True),template_name='exposicao.html'), name='exposicao'),
    # url(r'^exposicao/(?P<slug>[\w_-]+)/fotos/$', ListView.as_view(model=ObraExposicao, template_name='exposicao_fotos.html'), name='fotos'),
    # url(r'^exposicao-nav/$', ListView.as_view(model=Exposicao, template_name='exposicao_nav.html'), name='exposicao_nav'),
)