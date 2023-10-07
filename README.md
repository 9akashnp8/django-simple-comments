# Django Simple Comments

It's in the name. Simple. Bare bone comments system for Django app.

Based on the Django [ContentTypes framework](https://docs.djangoproject.com/en/4.2/ref/contrib/contenttypes)

## Installation
```bash
pip install django-simple-comments
```

## Usage
1. Add `django_simple_comments` to your INSTALLED_APPS.

2. Run `python manage.py migrate`

3. Create a 'comments' field on your model and set to Django ContentTypes's GenericRelation field.

```py
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from django_simple_comments.models import Comment

class YourModel(models.Model):
    ...
    comments = GenericRelation(Comment)
```

4. Add comments. If you have the object, you can use the .add() method to link a Comment object to it.

```py
from django_simple_comments.models import Comment
from .models import YourModel

your_object = YourModel.objects.first()
comment = Comment(content="Sample Comment")

your_object.comments.add(comment)
```

5. Query comments linked to your object.

There are multiple methods to query comments,

1. Helper function that queries by app_label, model & id of object.

```py
from django_simple_comments.utils.functions import get_comments

comments = get_comments("app_label", "your_model", 1)
```

2. Query by reverse relation

```py
object = YourModel.objects.first()
comments = object.comments.all() # replace "comments" with your field name
```

Refer the following for more info: https://docs.djangoproject.com/en/4.2/ref/contrib/contenttypes/#generic-relations
