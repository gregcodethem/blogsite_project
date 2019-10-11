
You don't need to this step in wagtail >=2.6.2
add to settings/base.py

INSTALLED_APPS = [
...
 "wagtail.contrib.routable_page",
...
]
if you are using an earlier version of wagtail, check at this link:
http://docs.wagtail.io/en/v2.6.2/reference/contrib/routablepage.html 
selecting the version you're using in the right hand corner to see the name you need to import.

in blog/models.py add:

from wagtail.contrib.routable_page.models import RoutablePageMixin, route


and change the BlogPage model to:

class BlogPage(RoutablePageMixin, Page):
    """
    RoutablePageMixin has to come before Page
    """

    description = models.CharField(max_length=255, blank=True,)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(BlogPage, self).get_context(request, *args, **kwargs)
        context['posts'] = self.posts
        context['blog_page'] = self
        return context

    def get_posts(self):
        return PostPage.objects.descendant_of(self).live()

    @route(r'^tag/(?P<tag>[-\w]+)/$')
    def post_by_tag(self, request, tag, *args, **kwargs):
        self.search_type = 'tag'
        self.search_term = tag
        self.posts = self.get_posts().filter(tags__slug=tag)
        return Page.serve(self, request, *args, **kwargs)

    @route(r'^category/(?P<category>[-\w]+)/$')
    def post_by_category(self, request, category, *args, **kwargs):
        self.search_type = 'category'
        self.search_term = category
        self.posts = self.get_posts().filter(categories__slug=category)
        return Page.serve(self, request, *args, **kwargs)

    @route(r'^$')
    def post_list(self, request, *args, **kwargs):
        self.posts = self.get_posts()
        return Page.serve(self, request, *args, **kwargs)



also add:
from datetime import datetime

add date to PostPage:

class PostPage(Page):
    body = RichTextField(blank=True)
    date = models.DateTimeField(
        verbose_name="Post date",
        default=datetime.today
    )
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    tags = ClusterTaggableManager(through='blog.BlogPageTag', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel('date'),
    ]

    @property
    def blog_page(self):
        return self.get_parent().specific

    def get_context(self, request, *args, **kwargs):
        context = super(PostPage, self).get_context(request, *args, **kwargs)
        context['blog_page'] = self.blog_page
        return context


We can now simplify the blog_page.html:

{% load wagtailcore_tags %}

{% block content %}
    <h1>{{ blog_page.title }}</h1>

    <div class="intro">{{ blog_page.description }}</div>

    {% for post in posts %}
        <h2><a href="{% pageurl post %}">{{ post.title }}</a></h2>
    {% endfor %}

{% endblock %}



and edit post_page.html:

{% load wagtailcore_tags wagtailroutablepage_tags%}

{% block content %}
    <h1>{{ page.title }}</h1>

    {{ page.body|richtext }}

    <p><a href="{{ page.get_parent.url }}">Return to blog</a></p>

{% endblock %}


{% if page.tags.all.count %}
    <div class="tags">
        <h3>Tags</h3>
        {% for tag in page.tags.all %}
            <a href="{% routablepageurl blog_page "post_by_tag" tag.slug %}">{{ tag }}</a>
        {% endfor %}
    </div>
{% endif %}

{% with categories=page.categories.all %}
    {% if categories %}
        <h3>Categories</h3>
        <ul>
            {% for category in categories %}
                <li style="display: inline">
                    <a href="{% routablepageurl blog_page "post_by_category" category.slug %}">{{ category.name }}</a>
                </li>
            {% endfor %}
        </ul>
    {% endif %}
{% endwith %}


We can also update post_page.html so it's a bit clearer:

{% block content %}
    <h1>{{ post.title }}</h1>

    {{ post.body|richtext }}

    <p><a href="{{ post.get_parent.url }}">Return to blog</a></p>

{% endblock %}
