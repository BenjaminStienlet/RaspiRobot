
$(document).ready(function(){
   
    var ws_movement = new WebSocket('ws://' + ip_addr + ':8080/movement');

    var movement_data = {'F': 0, 'B': 0, 'L': 0, 'R': 0};

    function send_movement_data() {
        ws_movement.send(JSON.stringify(movement_data));
    }
    
    ws_movement.onmessage = function (msg) {
       console.info('WS movement message: ' + msg)
    };

    //--------- KEYBOARD CONTROLS ---------//
    var movement_keys = {'w': 'F', 's': 'B', 'a': 'L', 'd': 'R'};
    var on_keydown = 1;
    var on_keyup = 0;

    $(window).on('keydown', function(event) {
        var key = event.key;
        console.info('WS movement: key down: ' + key);
        if (key in movement_keys) {
            movement_data[movement_keys[key]] = on_keydown;
            send_movement_data();
        }
    });

    $(window).on('keyup', function(event) {
        var key = event.key;
        if (key in movement_keys) {
           movement_data[movement_keys[key]] = on_keyup;
           send_movement_data();
        }
    });

    //--------- TOUCHSCREEN CONTROLS ---------//

    //--------- GAMEPAD CONTROLS ---------//
});
