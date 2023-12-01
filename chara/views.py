from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CharaMakeForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import CharaMake
from django.views.generic import FormView
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views.generic import DetailView, DeleteView, UpdateView



class IndexView(ListView):
    template_name = 'index.html'
    queryset = CharaMake.objects.order_by('posted_at')
    paginate_by = 9

@method_decorator(login_required, name='dispatch')
class CreateCharaView(CreateView):
    form_class = CharaMakeForm
    template_name = 'post_chara.html'
    success_url = reverse_lazy('chara:post_done')

    def form_valid(self,form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):    
    template_name = 'post_success.html'

class CategoryView(ListView):
    template_name ='index.html'
    paginate_by = 9
    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = CharaMake.objects.filter(
          category=category_id).order_by('-posted_at')
        return categories
    
class UserView(ListView):
    template_name = 'index.html'
    paginate_by = 9
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = CharaMake.objects.filter(
          user=user_id).order_by('-posted_at')
        return user_list
    
class DetailView(DetailView):
    template_name = 'detail.html'
    model = CharaMake

 

class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 9
    def get_queryset(self):
        queryset = CharaMake.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset

class CharaDeleteView(DeleteView):
    model = CharaMake
    template_name ='chara_delete.html'
    success_url = reverse_lazy('chara:chara_question')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

class CharaQuestionView(DeleteView):
    model = CharaMake
    template_name = 'chara_question.html'
    success_url = reverse_lazy('chara:chara_after')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class CharaAfterView(TemplateView):
    template_name = 'chara_after.html'

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('chara:contact')
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = \
          '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}'\
          .format(name, email, title, message)
        from_email = 'admin@example.com'
        to_list = ['admin@example.com']
        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list)
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class EditView(UpdateView):
    template_name = 'hensyuu.html'
    model = CharaMake
    success_url = reverse_lazy('chara:post_done')
    fields = ['user', 'category', 'title', 'comment', 'image1']
    def form_valid(self,form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)