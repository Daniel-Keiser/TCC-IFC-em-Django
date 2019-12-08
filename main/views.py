from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, EventUpdateForm, AlmoUpdateForm, BandaRegisterForm
from .models import Profile, Evento, Almossom, Banda, Galeria, ProgramacaoAlmossom


def cadastro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/cadastro.html', {'form': form})

@login_required

def profile(request):
    if request.method == 'POST':
        
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
   
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        # messages.success(request, f'Att account')
        # return redirect('profile')


    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)



def index(request):
    almossoms = Almossom.objects.all()
    return render(request, 'index.html' , {'almossoms': almossoms})



def events(request):
    eventos = Evento.objects.all()
    return render(request, 'events.html', {'eventos': eventos})

def event_edit(request, id):
    evento = Evento.objects.get(id=id)
    if request.method == 'POST':
        form = EventUpdateForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('events')
    form = EventUpdateForm(instance=evento)
    return render(request, 'event_edit.html', {'evento': evento, 'form': form})
    

def almo_edit(request, id):
    almossom = Almossom.objects.get(id=id)
    if request.method == 'POST':
        form = AlmoUpdateForm(request.POST, request.FILES, instance=almossom)
        if form.is_valid():
            form.save()
            return redirect('index')

    if (request.user.is_authenticated):
        bandas = getBandasByUser(request.user)
        form = AlmoUpdateForm(instance=almossom)
        return render(request, 'almo_edit.html', {'almossom': almossom, 'form': form, 'bandas': bandas})
    else:
        form = AlmoUpdateForm(instance=almossom)
        return render(request, 'almo_edit.html', {'almossom': almossom, 'form': form})


def about(request):
    return render(request, 'about.html')

def galeria(request):
    galerias = Galeria.objects.all()
    return render(request, 'galeria.html', {'galerias': galerias})

def cadastro_banda(request):
    if request.method == 'POST':
        form = BandaRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = BandaRegisterForm(initial={'lider':request.user})
    return render(request, 'cadastrobanda.html', {'form': form})


def programacao_almo(request):
    pass

def getBandasByUser(user):
    bandas = Banda.objects.filter(lider=user)
    return bandas

def subscribe(request, almo_id, banda_id):
    banda = Banda.objects.get(id=banda_id)
    almossom = Almossom.objects.get(id=almo_id)
    novaBanda = ProgramacaoAlmossom(banda=banda, almossom=almossom)
    novaBanda.save()
  
    return redirect('almo_edit', id=almo_id)

def unsubscribe(request, almo_id, banda_id):
    banda = Banda.objects.get(id=banda_id)
    almossom = Almossom.objects.get(id=almo_id)
    almossom.bandas.through.objects.filter(banda_id=banda_id).delete()
    # deleteBanda = ProgramacaoAlmossom(banda=banda, almossom=almossom).delete()
    # deleteBanda.save()

    return redirect('almo_edit', id=almo_id)

    
def search(request):
    if request.method == 'POST':    
        busca = request.POST['search_field']
        bandas = Banda.objects.filter(nome__contains=busca)
        # usuario = Profile.objects.filter(user__contains=busca)
        return render(request, 'search.html', {'bandas': bandas})
        # return render(request, 'search.html', {'usuario': usuario})
    return redirect('index')



























































    
