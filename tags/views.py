from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from tags.models import Tag
from tags.forms import TagForm
from posts.utils import ObjectCreateMixin, ObjectUpdateMixin

def tags_list_view(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tags_list.html', context={'tags': tags})


def tag_detail_view(request, id):
    tag = get_object_or_404(Tag, id=id)
    return render(request, 'tags/tag_detail.html', context={'tag': tag})


class TagCreateView(View, ObjectCreateMixin):
    
     form = TagForm
     template = 'tags/tag_create.html'

    
class TagUpdateView(View, ObjectUpdateMixin):

    obj_class = Tag
    template = 'tags/tag_update.html'
    form = TagForm
    

class TagDeleteView(View):

    def get(self, request, id):
        post = get_object_or_404(Tag, id=id)
        return render(request, 'tags/tag_delete.html', context={'post': post})

    def post(self, request, id):
        post = get_object_or_404(Tag, id=id)
        post.delete()
        return redirect(reverse('tags_list_url'))
