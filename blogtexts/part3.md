in blog/models.py we add

from wagtail.snippets.models import register_snippet

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


and change:

from django import forms
from modelcluster.fields import ParentalKey, ParentalManyToManyField

class PostPage(Page):
    body = RichTextField(blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]


python manage.py makemigrations
python manage.py migrate


back in blog/models.py add:


from taggit.models import TaggedItemBase, Tag as TaggitTag

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('PostPage', related_name='post_tags')

@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True



and change:

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager

class PostPage(Page):
    body = RichTextField(blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    tags = ClusterTaggableManager(through='blog.BlogPageTag', blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]


python manage.py makemigrations
python manage.py migrate


In post_page.html add:

{% if page.tags.all.count %}
    <div class="tags">
        <h3>Tags</h3>
        {% for tag in page.tags.all %}
            <button type="button">{{ tag }}</button>
        {% endfor %}
    </div>
{% endif %}

{% with categories=page.categories.all %}
    {% if categories %}
        <h3>Categories</h3>
        <ul>
            {% for category in categories %}
                <li style="display: inline">
                    {{ category.name }}
                </li>
            {% endfor %}
        </ul>
    {% endif %}
{% endwith %}
