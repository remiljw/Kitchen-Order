import json
from .models import Order
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class WSConsumer(AsyncWebsocketConsumer):
    
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

    # @database_sync_to_async
    # def _get_order_info(self, number):
    #     order_info = (Order.objects.filter(order_number=number).values('order_date_time', 'taken_by', 'is_fulfilled', 'fulfilled_by'))
    #     json_post = json.dumps(list(order_info), sort_keys=True, default=str)
    #     order_post  =json.loads(json_post)
    #     return order_post
  

    async def connect(self):
        self.groupname = 'new_orders'
        await self.channel_layer.group_add(
                    self.groupname,
                    self.channel_name,
                )      
        await self.accept()

   
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name,
        )
        await super().disconnect(code)



    async def take_order(self, event):
        number = event['number']
        details = event['details']
        info = await self._get_order_info(number)
        time_taken = info['order_date_time']
        taken_by = info['taken_by']
        fulfilled = info['is_fulfilled'] 
        fulfilled_by = info['fulfilled_by']       
 

        await self.send(text_data=json.dumps({   
    
                'number' : number,
                'details' : details,
                'time_taken': time_taken,
                'taken_by': taken_by,
                'fulfilled': fulfilled,
                'fulfilled_by':fulfilled_by,
     
                 }))


    async def receive(self, text_data):
        order_data_json = json.loads(text_data)
        number = order_data_json['number']
        details = order_data_json['details']
        time_taken = order_data_json['time_taken']
        taken_by = order_data_json['taken_by']
        fulfilled = order_data_json['fulfilled']
        fulfilled_by = order_data_json['fulfilled_by']       

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




        
   
