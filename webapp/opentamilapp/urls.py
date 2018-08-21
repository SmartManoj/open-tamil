"""opentamilweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import sys
from django.shortcuts import redirect
from django.conf.urls import url
from .views import *

PYTHON26 = sys.version.find('2.6') >= 0

urlpatterns = [
    url(r'^$', index,name="home"),
    url(r'^apidoc/$',lambda r: redirect("/static/sphinx_doc/_build/html/index.html")),
    url(r'^tts_demo/$',tts_demo,name="tts_demo"),
    url(r'^translite/$', trans,name="translite"),
    url(r'^tsci/$', uni,name="tsci"),
    url(r'^keechu/$', keechu,name="keechu"),
    url(r'^sandhi-check/$', sandhi_check,name="sandhi"),
    url(r'^spell/$', spl,name="spell"),
    url(r'^rever/$', rev,name="rever"),
    url(r'^number/$', num,name="number"),
    url(r'^anagram/$', anag,name="anagram"),
    url(r'^unigram/$', unig,name="unigram"),
    url(r'^ngram/$', ngra,name="ngram"),
    url(r'^vaypaadu/$',vaypaadu,name="multiplication"),
    url(r'^number/(?P<num>\d+)/$', numstr,name="numstr"),
    url(r'^tsci/(?P<tsci>.+?)/$', unicod,name="unicod"),
    url(r'^keechu/(?P<k1>.+?)/$', keech,name="keech"),
    url(r'^sandhi-checker/$', call_sandhi_check,name="sandhi_check"),
    url(r'^translite/(?P<tan>.+?)/$', translite,name="phonetic"),
    url(r'^spell/(?P<k1>.+?)/$', spell_check,name="spell_check"),
    url(r'^ngram/(?P<ng>.+?)', test_ngram,name="test_ngram"),
    url(r'^anagram/(?P<word>.+?)/$', anagram,name="ta_anagram"),
    url(r'^unigram/(?P<word>.+?)/$', test_basic,name="ta_unigram"),
    url(r'^revers/(?P<word>.+?)/$', revers,name="ta_revers"),
    url(r'^xword/$',xword,name='ta_xword'),
    url(r'^summarizer/',summarizer,name='ta_summarizer'),
    url(r'^morse/(?P<direction>.+)/(?P<word>.+)/$',morse,name='ta_morse'),
    url(r'^morse/$', morse_code,name="morse_code"),
]

if not PYTHON26:
    urlpatterns.extend( [
        url(r'^classify-word/$', classify_word,name="classify_word"),
        url(r'^get-classify/$', get_classify,name="classifier")] )
