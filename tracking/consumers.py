# tracking/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class LocationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "live_locations"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        print(f"WebSocket connected: {self.channel_name}")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        lat = data.get('latitude')
        lng = data.get('longitude')
        user = self.scope["user"].username if self.scope["user"].is_authenticated else "Anonymous"

        # সবাইকে ব্রডকাস্ট করা হচ্ছে
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'location_update',
                'latitude': lat,
                'longitude': lng,
                'user': user
            }
        )

    async def location_update(self, event):
        await self.send(text_data=json.dumps({
            'latitude': event['latitude'],
            'longitude': event['longitude'],
            'user': event['user']
        }))