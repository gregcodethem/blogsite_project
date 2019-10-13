
Copy files from finished templates
remove wagtailmd from tags in: base.html, blog_page.html, post_page.html


Run python manage.py startapp wagtailmd,

then put wagtailmd into installed_apps


make utils.py in wagtailmd, and copy:
from django.db.models import TextField
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.utils.widgets import WidgetWithScript


class MarkdownField(TextField):
    def __init__(self, **kwargs):
        super(MarkdownField, self).__init__(**kwargs)


class MarkdownPanel(FieldPanel):
    def __init__(self, field_name, classname="", widget=None, **kwargs):
        super(MarkdownPanel, self).__init__(
            field_name,
            classname=classname,
            widget=widget,
            **kwargs
        )

        if self.classname:
            if 'markdown' not in self.classname:
                self.classname += "markdown"
        else:
            self.classname = "markdown"




Most of the steps from Markdown tutorial


pipenv install Markdown

pipenv install wagtailmenus

$ python manage.py migrate wagtailmenus


that's all tutorial 12


now the extra tutorial - run scss the python way

pipenv install django_compressor
pipenv install django-libsass



tutorial 9

pipenv install Pygments

and edited wagtailmd/templatetags/wagtailmd.py

Not finished tutorial 9


Tutorial 10

Go through all, also in models.py, make sure PostPage model has context:

    def get_context(self, request, *args, **kwargs):
        context = super(PostPage, self).get_context(request, *args, **kwargs)
        context['blog_page'] = self.blog_page
        context['post'] = self
        return context

Mine was missing the context['post'] line which was referred to in a django error.

It seems it was this context['post'] part that was causing the errors before.

