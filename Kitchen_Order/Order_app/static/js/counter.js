$(document).ready(function() {
    $('#new_order').submit(function() { // On form submit event
        $.ajax({ // create an AJAX call...
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            success: function(response) { // on success..
                document.getElementById("new_order").reset();
                $('.message').html(response.success); // update the DIV
            },
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
        return false;
    });
});



document.querySelector('#submit').onclick = function(e) {
const numberInputDom = document.querySelector('#id_order_number');
const detailsInputDom = document.querySelector('#id_order_details');
const number = numberInputDom.value;
const details = detailsInputDom.value;
orderSocket.send(JSON.stringify({
    'number': number,
    'details' : details,
    'time_taken': '',
    'taken_by': '',
    'fulfilled': '',
    'fulfilled_by':'',

    }));
console.log('data sent')
}; 