
cd blogsite

run python manage.py startapp blog to create new app in this Django project, then add blog to INSTALLED_APPS in wagtail_tuto/settings/base.py to enable it in this Django project.


edit blog/models.py to be:

from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class BlogPage(Page):
    description = models.CharField(max_length=255, blank=True,)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]

class PostPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


python manage.py makemigrations
python manage.py migrate

in the admin create a test blog-page and post-page

Also create these files:

Create blog/templates/blog/blog_page.html

{% load wagtailcore_tags %}

{% block content %}
    <h1>{{ page.title }}</h1>

    <div class="intro">{{ page.description }}</div>

    {% for post in page.get_children %}
        <h2><a href="{% pageurl post %}">{{ post.title }}</a></h2>
    {% endfor %}

{% endblock %}

Create blog/templates/blog/post_page.html

{% load wagtailcore_tags %}

{% block content %}
    <h1>{{ page.title }}</h1>

    {{ page.body|richtext }}

    <p><a href="{{ page.get_parent.url }}">Return to blog</a></p>

{% endblock %}


You should now be able to visit these test pages.


