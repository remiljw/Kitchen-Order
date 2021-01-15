var ws_url = 'ws://' + window.location.host + '/ws/orders/';
var orderSocket = new WebSocket(ws_url);

function connect() {
  orderSocket.onopen = function() {
   console.log('Connection established');
  };
 

  orderSocket.onclose = function(e) {
    console.log('Socket is closed. Reconnect will be attempted in 1 second.', e.reason);
    setTimeout(function() {
    var ws_url = 'ws://' + window.location.host + '/ws/orders/';
    var orderSocket = new WebSocket(ws_url);
    console.log('Connection established');
    }, 1000);
  };

  orderSocket.onerror = function(err) {
    console.error('Socket encountered error: ', err.message, 'Closing socket');
    orderSocket.close();
  };
}
connect();
