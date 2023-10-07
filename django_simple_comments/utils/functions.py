from django.contrib.contenttypes.models import ContentType

from django_simple_comments.models import Comment


def get_comments(app_label: str, model: str, object_id: str):
    """Return QuerySet of Comments linked to a given model object.

    Args:
        app_label (str): ContentType app_label
        model (str): ContentType model name
        object_id (str): id of the object for whom comments are required

    Returns:
        QuerySet: Queryset that contains all/any comments linked
            to the give object.
    """
    ct = ContentType.objects.get(app_label=app_label, model=model)
    comments = Comment.objects.filter(
        content_type=ct, object_id=object_id).order_by("-created_at")
    return comments
