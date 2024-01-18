from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Myapp.models import Cartao
from Myapp.forms import CartaoForm

def index(request):
    if request.method == 'POST':
        form = CartaoForm(request.POST)
        if form.is_valid():
            form.save()
            # return render(request, 'core/home.html', {'form': LojistaForm(), 'sucesso': True})
            return render(request, 'Myapp/obrigado.html')
    else:
        form = CartaoForm()
    
    return render(request, 'Myapp/index.html', {'form': form})

