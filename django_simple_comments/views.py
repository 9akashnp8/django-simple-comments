from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CommentSerializer
from .utils import get_comments


class CommentListView(APIView):

    def post(self, request):
        payload = request.data
        app_label = payload.get("app_label")
        model_name = payload.get("model_name")
        object_id = payload.get("object_id")

        comments = get_comments(
            app_label=app_label, model=model_name, object_id=object_id)

        # OR if you've configured a generic field on your model, pointing
        # to this model, you can do the following:
        # model_class = ct.model_class()
        # comments = model_class.<field_name>.all()

        data = CommentSerializer(comments, many=True)
        return Response(data.data)
