import json
from datetime import datetime
from .models import Order
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class WSConsumer(AsyncWebsocketConsumer):

    #Get Formatted date from string, but keeps flunctuating, works one minute, doesn't the next.
    def _get_date_time(self, date_time):
        parsed = datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S.%f%z')
        formatted = parsed.strftime('%b. %d, %Y, %-I:%M %p')
        formatted = formatted.replace('AM', 'a.m.').replace('PM', 'p.m.')
        return formatted    
    
    #Retrieve full data of newly placed order
    @database_sync_to_async
    def _get_order_info(self, number):
        order_info = Order.objects.get(order_number=number)
        order_dict ={}
        order_dict['taken_by'] = order_info.taken_by.username
        order_dict['is_fulfilled'] = order_info.is_fulfilled
        order_dict['fulfilled_by'] = order_info.fulfilled_by
        order_dict['order_date_time'] = order_info.order_date_time
        json_post = json.dumps(order_dict, sort_keys=True, default=str)
        order_post  =json.loads(json_post)
        return order_post

    
    async def connect(self):
        #Join room group
        self.groupname = 'new_orders'
        await self.channel_layer.group_add(
                    self.groupname,
                    self.channel_name,
                )      
        await self.accept()

   
    async def disconnect(self, code):
        #Leave Room group
        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name,
        )
        await super().disconnect(code)


    #Receive message from room group
    async def take_order(self, event):
        number = event['number']
        details = event['details']
        info = await self._get_order_info(number)
        time_taken = await self._get_date_time(info['order_date_time'])
        # time_taken = info['order_date_time']
        taken_by = info['taken_by']
        fulfilled = info['is_fulfilled']
        fulfilled_by = info['fulfilled_by']       
 
        #Sends Message to WebSocket
        await self.send(text_data=json.dumps({   
    
                'number' : number,
                'details' : details,
                'time_taken': time_taken,
                'taken_by': taken_by,
                'fulfilled': fulfilled,
                'fulfilled_by':fulfilled_by,
     
                 }))

    #Receive message from WebSocket
    async def receive(self, text_data):
        order_data_json = json.loads(text_data)
        number = order_data_json['number']
        details = order_data_json['details']
        time_taken = order_data_json['time_taken']
        taken_by = order_data_json['taken_by']
        fulfilled = order_data_json['fulfilled']
        fulfilled_by = order_data_json['fulfilled_by']       

        #Send message to room group
        await self.channel_layer.group_send(
            self.groupname,
            {   
                'type': 'take_order',
                'number' : number,
                'details' : details,
                'time_taken': time_taken,
                'taken_by': taken_by,
                'fulfilled': fulfilled,
                'fulfilled_by':fulfilled_by,
            }
        )




        
   
