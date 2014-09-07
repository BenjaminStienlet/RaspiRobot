$(document).ready(function(){
   
    var ws_log = new WebSocket('ws://' + ip_addr + ':8080/log');
    
    ws_log.onmessage = function (msg) {
        var obj = JSON.parse(msg.data);
        for (var i = 0; i < obj.length; i++){
           var table_row = $('<tr>\
                            <td class="type ' + obj[i]["type"] + '"></td>\
                            <td class="time">' + obj[i]["time"] + '</td>\
                            <td class="module">' + obj[i]["module"] + '</td>\
                            <td class="description">' + obj[i]["description"] + '</td>\
                            </tr>');
           $('#log_table_body').prepend(table_row);
        }
    };

});
