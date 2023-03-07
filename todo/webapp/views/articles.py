from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, FormView

from webapp.models import Task

from webapp.forms import TaskForm


def add_view(request):
    form = TaskForm()
    if request.method == 'GET':
        context = {
            'form': form
        }
        print(context)
        return render(request, 'article_create.html', context)
    form = TaskForm(request.POST)
    if not form.is_valid():
        context = {
            'form': form
        }
        return render(request, 'article_create.html', context)
    task = form.save()
    # return redirect(reverse('article-detail', kwargs={pk=article.pk)})
    return redirect('article_detail', pk=task.pk)


class ArticleView(TemplateView):
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class ArticleUpdateView(FormView):
    template_name = 'article_update.html'
    form_class = TaskForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = TaskForm(instance=context['task'])
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task = form.save()
            return redirect('article_detail', pk=task.pk)

        context = {
            'form': form,
            'task': task,
        }
        return render(request, 'article_update.html', context=context)


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'article_confirm_delete.html', context={'task': task})


def confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
