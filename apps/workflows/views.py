# Django
from django.views.generic import View
from django.http import JsonResponse
from django.apps import apps


class TransitionView(View):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        transition_name = kwargs.get("transition")
        object = self.get_object()
        if not hasattr(object, transition_name):
            message = "The transition %s does not exists." % transition_name
            return self.error(message)
        transition = getattr(object, transition_name)
        transition()
        object.save()
        return self.success("Success action.")

    def get_object(self):
        app_name = self.kwargs.get("app")
        model_name = self.kwargs.get("model")
        pk = self.kwargs.get("pk")
        model_class = apps.get_model(app_name, model_name)
        object = model_class.objects.get(pk=pk)
        return object

    def success(self, message):
        response = {"message": message}
        return JsonResponse(response, status=200)

    def error(self, message):
        response = {"error": message}
        return JsonResponse(response, status=400)
