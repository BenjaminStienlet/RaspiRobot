
$(document).ready(function(){
   
    var ws_movement = new WebSocket('ws://' + ip_addr + ':8080/movement');

    var movement_data = {'F': 0, 'B': 0, 'L': 0, 'R': 0};
    
    var send_treshold = 0.05;

    function send_movement_data(new_movement_data) {
        var send = false;
        for (var key in movement_data) {
            if (Math.abs(movement_data[key] - new_movement_data[key]) > send_treshold) {
                send = true;
            }
        }
        if (send) {
            movement_data = jQuery.extend({}, new_movement_data);
            ws_movement.send(JSON.stringify(movement_data));
        }
    }
    
    ws_movement.onmessage = function (msg) {
       console.info('WS movement message: ' + msg)
    };

    //--------- KEYBOARD CONTROLS ---------//
    var movement_keys = {'w': 'F', 's': 'B', 'a': 'L', 'd': 'R'};
    var on_keydown = 1;
    var on_keyup = 0;

    $(window).on('keydown', function(e) {
        var key = e.key;
        if (key in movement_keys) {
            var new_movement_data = jQuery.extend({}, movement_data);
            new_movement_data[movement_keys[key]] = on_keydown;
            send_movement_data(new_movement_data);
        }
    });

    $(window).on('keyup', function(e) {
        var key = e.key;
        if (key in movement_keys) {
           var new_movement_data = jQuery.extend({}, movement_data);
           new_movement_data[movement_keys[key]] = on_keyup;
           send_movement_data(new_movement_data);
        }
    });

    //--------- TOUCHSCREEN CONTROLS ---------//
    var move_location = {};
    var camera_location = {};
    var circle_radius = 50;

    $('#page').bind('touchstart', function(e){
        e.preventDefault();

        var touch = e.originalEvent.touches[0] || e.originalEvent.changedTouches[0];
        var x = touch.pageX;
        var y = touch.pageY;

        var el;
        if (x < $(window).width() / 2) {
            el = $('#move_circle');
            move_location = {'x': x, 'y': y};
        }
        else {
            el = $('#camera_circle');
            camera_location = {'x': x, 'y': y};
        }

        el.removeClass('hidden');

        el.css({
            "height": 2 * circle_radius,
            "width": 2 * circle_radius,
            "position": absolute,
            "top": y - circle_radius,
            "left": x - circle_radius
        }); 
    });

    $('#page').bind('touchend', function(e){
        e.preventDefault();
        
        if (x < $(window).width() / 2) {
            el = $('#move_circle');
            move_location = {};
        }
        else {
            el = $('#camera_circle');
            camera_location = {};
        }

        el.removeAttr("style");
        el.addClass('hidden');
    });

    $('#page').bind('touchmove', function(e){
        e.preventDefault();

        var touch = e.originalEvent.touches[0] || e.originalEvent.changedTouches[0];
        var x = touch.pageX;
        var y = touch.pageY;

        var x_diff;
        var y_diff;

        if (x < $(window).width() / 2) {
            x_diff = x - move_location['x'];
            y_diff = y - move_location['y'];
            
            if (x_diff > circle_radius) {
                x_diff = circle_radius;
            }
            if (y_diff > circle_radius) {
                y_diff = circle_radius;
            }
            
            if (x_diff < -circle_radius) {
                x_diff = -circle_radius;
            }
            if (y_diff < -circle_radius) {
                y_diff = -circle_radius;
            }
            
            x_diff /= circle_radius;
            y_diff /= circle_radius;
            
            var new_movement_data = {};
            if (x_diff > 0) {
                new_movement_data['R'] = x_diff;
                new_movement_data['L'] = 0;
            }
            else {
                new_movement_data['L'] = -x_diff;
                new_movement_data['R'] = 0;
            }

            if (y_diff > 0) {
                new_movement_data['B'] = y_diff;
                new_movement_data['F'] = 0;
            }
            else {
                new_movement_data['F'] = -y_diff;
                new_movement_data['B'] = 0;
            }

            send_movement_data(new_movement_data);
            
        }
        else {
            x_diff = x - camera_location['x'];
            y_diff = y - camera_location['y'];
        }
    });

    //--------- GAMEPAD CONTROLS ---------//
});
