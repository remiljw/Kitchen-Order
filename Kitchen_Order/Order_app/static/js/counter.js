$(document).ready(function(e) {
    $('#new_order').submit(function(e) { // On form submit event
        $.ajax({ // create an AJAX call...
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            success: function(response) { // on success..
                if (response.success) {
                    document.getElementById("new_order").reset();
                    $('.message').html(response.success);
                    setTimeout(function(){
                        $('.message').hide()
                    }, 1000) }
                else if(response.err_code == 400){
                    for(var key in response.error){
                        document.getElementById("new_order").reset();
                        $('.message').html(response.error[key][0]);
                        setTimeout(function(){
                        $('.message').hide()
                    }, 1000) }}
                     
            
            },
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
        return false;
        
    });
    e.preventDefault();
    
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