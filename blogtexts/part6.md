
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

