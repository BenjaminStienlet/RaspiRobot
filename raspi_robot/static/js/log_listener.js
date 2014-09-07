$(document).ready(function(){
   
    var ws_log = new WebSocket('ws://' + ip_addr + ':8080/log');
    
    ws_log.onmessage = function (msg) {
       var obj = JSON.parse(msg);
       var table_row = $('<tr>
                        <td class="type, ' + obj["type"] + '"></td>
                        <td class="time">' + obj["time"] + '</td>
                        <td class="module">' + obj["module"] + '</td>
                        <td class="description">' + obj["description"] + '</td>
                        </tr>');
       $('#log_table tbody').prepend(table_row);
    };

});
