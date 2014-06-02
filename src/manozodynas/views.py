from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import LoginForm
from .forms import WordForm
from .forms import TranslationForm
from django.contrib.auth import login
from models import Word, Translation
from django.shortcuts import redirect

def index_view(request):
    return render(request, 'manozodynas/index.html', {})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginForm()
    #import ipdb; ipdb.set_trace()
    return render(request, 'manozodynas/login.html', {'form':form})

def words_view(request):
    words = Word.objects.all()
    form = WordForm()
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'manozodynas/words.html', {'words': words, 'form': form})
        else:
            return render(request, 'manozodynas/words.html', {'words': words, 'form': form})

    if request.method == 'GET':
        return render(request, 'manozodynas/words.html', {'words': words, 'form': form})

def words_del_view(request, key):
    words = Word.objects.all()
    form = WordForm()
    if request.method == 'GET':
        try:
            word = Word.objects.get(pk=key).delete()
        except Word.DoesNotExist:
            raise Http404
    return redirect('words')

def translations_view(request, key):
    word = Word.objects.get(pk=key)
    translations = Translation.objects.filter(word=word)

    if request.method == 'GET':
        return render(request, 'manozodynas/translations.html', {'translations': translations})

def translation_add_view(request):
    form = TranslationForm()
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'manozodynas/translation-add.html', {'form': form})
        else:
            return render(request, 'manozodynas/translation-add.html', {'form': form})
    if request.method == 'GET':
        return render(request, 'manozodynas/translation-add.html', {'form': form})

