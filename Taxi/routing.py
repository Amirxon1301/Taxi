from django.urls import path


from django.urls import path

from users.consumers import OrderConsumer

websocket_urlpatterns = [
    path("ws/orders/", OrderConsumer.as_asgi()),
]