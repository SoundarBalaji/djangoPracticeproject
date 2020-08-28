from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Collection,Piece
from django.views import generic
from .forms import UserForm
from django.contrib.auth import authenticate,login
from django.views.generic import View

#f/n calling method
# def index(request):
#     all_collection = Collection.objects.all()
#     con = {
#         'all_collection': all_collection
#     }
#     return render(request, "genre//genretemplate.html", con)
#
# # Create your views here.
#
#
# def details(request, genre_id):
#     #return HttpResponse("<h1>The genre id is: " + str(genre_id) + "</  h1>")
#     citem=Collection.objects.get(pk=genre_id)
#     Pitem=Piece.objects.filter(collection=citem)
#     context={
#         "Pitem" : Pitem
#     }
#     return  render(request, "genre//detailstemplate.html", context)

#genric class call method:

class index(generic.ListView):
    template_name = 'genre/genretemplate.html'

    def get_queryset(self):
        return Collection.objects.all()

class details(generic.DetailView):
    model = Collection
    template_name = 'genre/detailstemplate.html'

class UserFormView(View):
    form_class=UserForm
    template_name ='genre/formtemplate.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'forms':form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data('username')
            password = form.cleaned_data('password')
            user.set_password(password)
            user.save()

            newuser = authenticate(username=username,password=password)

            if newuser is not None:
                if newuser.is_active:
                    login(request,newuser)
                    return redirect("index/")

        return render(request,self.template_name,{'forms':form})
