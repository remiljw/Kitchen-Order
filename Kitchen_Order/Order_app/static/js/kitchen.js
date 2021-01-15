orderSocket.onmessage = function(message) {
    var data = JSON.parse(message.data);
    var order = $("#order")
    var ele = $('<tr></tr>')
    console.log(data)
    ele.append(
        $("<td></td>").text(data.number)
    )
    ele.append(
        $("<td></td>").text(data.details)
    )
    ele.append(
        $("<td></td>").text(data.time_taken)
    )
    ele.append(
        $("<td></td>").text(data.taken_by)
    )
    ele.append(
        $("<td></td>").text(data.fulfilled)
    )
    
    link = 'fulfill-order/'+ data.number +'/'
    ele.append(
        $("<td></td>").append($('<a href="'+link+'">'+'Fulfill Order'+'</a>'))
    )
    
 
    order.append(ele)
};

