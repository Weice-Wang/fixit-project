from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, Tag
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import MaintainingForm, TagForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def item_index(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'items/index.html', {'items': items})

def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    tags = Tag.objects.all()
    tags_item_doesnt_have = Tag.objects.exclude(id__in = item.tags.all().values_list('id'))
    maintaining_form = MaintainingForm()
    return render(request, 'items/detail.html', {'item': item, 'maintaining_form': maintaining_form, 'tags': tags_item_doesnt_have})

class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['name', 'brand', 'category', 'price', 'warranty', 'purchase_date', 'description']
    
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['brand', 'category', 'price', 'warranty', 'purchase_date', 'description']

    
class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = '/items/'

def add_maintaining(request, item_id):
    form = MaintainingForm(request.POST)
    if form.is_valid():
        new_maintaining = form.save(commit=False)
        new_maintaining.item_id = item_id
        new_maintaining.save()
    return redirect('item-detail', item_id=item_id)


class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = TagForm

class TagList(LoginRequiredMixin, ListView):
    model = Tag

class TagDetail(LoginRequiredMixin, DetailView):
    model = Tag


class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    form_class = TagForm

class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = '/tags/'


def associate_tag(request, item_id, tag_id):
    Item.objects.get(id=item_id).tags.add(tag_id)
    return redirect('item-detail', item_id=item_id)


def remove_tag(request, item_id, tag_id):
    item = Item.objects.get(id=item_id)
    item.tags.remove(tag_id)
    return redirect('item-detail', item_id=item.id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('item-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


