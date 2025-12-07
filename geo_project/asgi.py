# geo_project/geo_project/asgi.py
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geo_project.settings')

# এই লাইনটা সবার আগে থাকতেই হবে
django_asgi_app = get_asgi_application()

# এরপর চ্যানেলস ইমপোর্ট করো
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

# তোমার routing.py ইমপোর্ট
import tracking.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                tracking.routing.websocket_urlpatterns
            )
        )
    ),
})