$(document).ready(function(){
   
    var ws_log = new WebSocket('ws://' + ip_addr + ':8080/log');
    
    ws_log.onmessage = function (msg) {
       var obj = JSON.parse(msg);
       var table_row = $('<tr>
                        <td class="' + obj["type"] + '">' + obj["type"] + '</td>
                        <td>' + obj["time"] + '</td>
                        <td>' + obj["module"] + '</td>
                        <td>' + obj["description"] + '</td>
                        </tr>');
       $('#log_table tbody').prepend(table_row);
    };

});
