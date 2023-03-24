from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy

from django.contrib import messages

# from django.db.models import F

# from django.views.generic.edit import FormView
# from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Savingacc, Creditacc
from .models import SavingDetail, CreditDetail  #not using

# from django.contrib.auth.models import BaseUserManager


# from django.contrib.auth.views import LoginView

# Create your views here.


# class Sample(LoginRequiredMixin, ListView):
#     model = Savingacc
#     context_object_name = 'sample'

# class SampleTwo(ListView):
#     model = Savingacc
#     context_object_name = 'see-form'
#         fields = '__all__'
#     template_name = 'ocean_cs/savingacc_form.html'
#         success_url = reverse_lazy('sample')

# class SavingaccCreate(CreateView):
#     model = Savingacc
#         # model = Creditacc
#     fields = '__all__'
#     success_url = reverse_lazy('sample')

# class SavingDetail(CreateView):
#     model = SavingDetail
#         model = Creditacc
#     fields = '__all__'
#         success_url = reverse_lazy('sample')

class CustomLoginView(LoginView):
    template_name = 'ocean_cs/login.html'
    fields = '__all__'  #instead of field = [title, descriptio....]
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')


class RegisterPage(FormView):
    template_name = 'ocean_cs/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')
        return super(RegisterPage,  self).get(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_picks(sender, instance, created, **kwargs):
    if created:
        # Savingacc.objects.create(user=user.request)
        Savingacc.objects.create(camount=0)
        Creditacc.objects.create(camount=0)


@login_required(login_url='/login/')
def main(request):
    return render(request, 'ocean_cs/selection.html', {})


@login_required(login_url='/login/')
def viewsav(request):
    if request.method == 'POST':
        # data = Savingacc.objects.all()
        data = Savingacc.objects.filter(user=request.user) #request.user

        for a in data:
            namt = int(a.camount)

        print(namt)
        # messages.info(request, 'my name')
    
    return render(request, 'ocean_cs/index.html', {'camt': namt})


@login_required(login_url='/login/')
def HomePage(request):
    if request.method == 'POST':
        deposite = int(request.POST['deposit'])
        data = Savingacc.objects.filter(user=request.user)

        for a in data:
            if deposite < 0:
                messages.info(request, 'invalid credentials!!!')
                return redirect('HomePage')
            elif deposite == 0:
                messages.info(request, 'there is no such deposite!!!')
                return redirect('HomePage')
            else:
                ndept = deposite + int(a.camount)

        # new_dept = Savingacc(camount=deposite)
        new_dept = Savingacc.objects.filter(user=request.user).update(camount=ndept)
        # TemperatureData.objects.filter(id=1).update(value=F('value') + 1)
        # new_dept.save()

        # template_name = 'ocean_cs/index.html'

    return render(request, 'ocean_cs/index.html', {})

# This is good idea but,

# class MyAccountManager(BaseUserManager):
#     def create_user(self, username, password):

#         if not username:
#             raise ValueError('please add an username')
        
#         user = self.model(username= username, password= password)

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password):

#         user= self.create_user(username= username, password= password)

#         user.is_activate = True
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


@login_required(login_url='/login/')
def home(request):
    if request.method == 'POST':
        withdraw = int(request.POST['withdraw'])
        data = Savingacc.objects.filter(user=request.user)

        for a in data:
            if withdraw < 0:
                messages.info(request, 'invalid credentials!!!')
                return redirect('home')
            elif withdraw == 0:
                messages.info(request, 'there is no such withdraw!!!')
                return redirect('home')
            elif withdraw > int(a.camount):
                messages.info(request, 'balance can not be negative!!!')
                return redirect('home')
            else:
                nwith = int(a.camount) - withdraw

        new_with = Savingacc.objects.filter(user=request.user).update(camount=nwith)
    return render(request, 'ocean_cs/index.html', {})


    #------------------------------------------------
    

@login_required(login_url='/login/')
def viewcred(request):
    if request.method == 'POST':
        data = Creditacc.objects.filter(user=request.user)

        for a in data:
            namt = (-1)*(int(a.camount))

        print(namt)
        # messages.info(request, 'my name')
    
    return render(request, 'ocean_cs/indexcre.html', {'camt': namt})


@login_required(login_url='/login/')
def creditdep(request):
    if request.method == 'POST':
        deposite = int(request.POST['deposit'])
        data = Creditacc.objects.filter(user=request.user)

        for a in data:
            if deposite < 0:
                messages.info(request, 'invalid credentials!!!')
                return redirect('creditdep')
            elif deposite == 0:
                messages.info(request, 'there is no such deposite!!!')
                return redirect('creditdep')
            elif deposite > (-1)*(int(a.camount)):
                messages.info(request, 'it is not saving account keep free from your credit!!!')
                return redirect('creditdep')
            else:
                ndept = int(a.camount) + deposite

        # new_dept = Savingacc(camount=deposite)
        new_dept = Creditacc.objects.filter(user=request.user).update(camount=ndept)
        # TemperatureData.objects.filter(id=1).update(value=F('value') + 1)
        # new_dept.save()

        # template_name = 'ocean_cs/index.html'

    return render(request, 'ocean_cs/indexcre.html', {})


@login_required(login_url='/login/')
def creditwith(request):
    if request.method == 'POST':
        withdraw = int(request.POST['withdraw'])
        data = Creditacc.objects.filter(user=request.user)

        for a in data:
            if withdraw < 0:
                messages.info(request, 'invalid credentials!!!')
                return redirect('creditwith')
            elif withdraw == 0:
                messages.info(request, 'there is no such withdraw!!!')
                return redirect('creditwith')
            else:
                nwith = int(a.camount) - withdraw

        new_with = Creditacc.objects.filter(user=request.user).update(camount=nwith)
    return render(request, 'ocean_cs/indexcre.html', {})


    # inv_id = request.GET.get('inv_id').split(',')

    # for i in inv_id:
    #       summary = Invoice.objects.filter(id=i).annotate(result=F('unit_price') * F('num_units')).aggregate(Sum('result'))['result__sum']
    #     Savingacc = SavingDetail.objects.raw('''select id as id,sum(unit_price * num_units) as sum from restapi_invoice where inv_id = {}'''.format(i))
    #      Savingacc = SavingDetail.objects.raw('''select id as id,sum(unit_price * num_units) as sum from restapi_invoice where inv_id = {}'''.format(i))
    #     x = SavingDetail.objects.get(pk=Savingacc[0])
    #      Summary.objects.update_or_create(invo_id_id=x, defaults={"sum": summary[1]})
    #     p = Savingacc(sum=Savingacc[1])
    #     p.save()
    #     p.invo_id.add(x)


# class SavingDetailUp(FormView):
#     template_name = 'ocean/insert.html'
#     form_class = 

# def sample(request):
#     return HttpResponse("hello world")
    # return render(request, "Hello world")


# class CustomLoginView(LogView):
#     template_name = 'base/login.html'
#     redirect_authenticated_user = True

#     def get_success_url(self):
#         return reverse_lazy('oceans')