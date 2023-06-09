from .models import Post, Response
from .forms import PostForm, ResponsesFilterForm

from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect


class Index(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 5


class PostItem(DetailView):
    model = Post
    template_name = 'post_item.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Response.objects.filter(author_id=self.request.user.id).filter(post_id=self.kwargs.get('pk')):
            context['respond'] = "Откликнулся"
        elif self.request.user == Post.objects.get(pk=self.kwargs.get('pk')).author:
            context['respond'] = "Мое_объявление"
        return context


class CreatPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.has_perm('board.add_post'):
            return HttpResponseRedirect(reverse('account_profile'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = User.objects.get(id=self.request.user.id)
        post.save()
        return redirect(f'/post/{post.id}')


class EditPost(PermissionRequiredMixin, UpdateView):
    model = Post
    permission_required = 'callboard.change_post'
    template_name = 'edit_post.html'
    success_url = '/create/'
    form_class = PostForm

    def dispatch(self, request, *args, **kwargs):
        author = Post.objects.get(pk=self.kwargs.get('pk')).author.username
        if self.request.user.username == 'admin' or self.request.user.username == author:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Редактировать объявление может только его автор")

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.object.get(pk=id)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/post/' + str(self.kwargs.get('pk')))


class DeletePost(PermissionRequiredMixin, DeleteView):
    model = Post
    permission_required = 'callboard.change_post'
    template_name = 'delete_post.html'
    success_url = '/index'
    queryset = Post.objects.all()
    form_class = PostForm

    def dispatch(self, request, *args, **kwargs):
        author = Post.objects.get(pk=self.kwargs.get('pk')).author.username
        if self.request.user.username == 'admin' or self.request.user.username == author:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Удалить объявления может только его автор")


title = str("")


class Responses(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'responses.html'
    context_object_name = 'responses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Responses, self).get_context_data(**kwargs)
        global title

        if self.kwargs.get('pk') and Post.objects.filter(id=self.kwargs.get('pk')).exists():
            title = str(Post.objects.get(id=self.kwargs.get('pk')).title)
            print(title)
        context['form'] = ResponsesFilterForm(self.request.user, initial={'title': title})
        context['title'] = title
        if title:
            post_id = Post.objects.get(title=title)
            context['filter_responses'] = list(Responses.object.filter(post_id=post_id).order_by('-dateCreation'))
            context['response_post_id'] = post_id.id
        else:
            context['filter_responses'] = list(
                Responses.object.filter(post_id__author_id=self.request.user).order_by('-dateCreation'))
            context['myresponses'] = list(
                Responses.object.filter(author_id=self.request.user).order_by('-dateCreation'))
            return context

    def post(self, request, *args, **kwargs):
        global title
        title = self.request.POST.get('title')

        if self.kwargs.get('pk'):
            return HttpResponseRedirect('/responses')
        return self.get(request,  *args, **kwargs)

#@login_required








