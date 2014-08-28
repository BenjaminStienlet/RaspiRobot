$(document).ready(function(){
   
    var ws_servo = new WebSocket("ws://192.168.0.33:8080/servo");
    var ws_camera_servo = new WebSocket("ws://192.168.0.33:8080/camera_servo");
    var ws_motor = new WebSocket("ws://192.168.0.33:8080/motor");
    
    ws_servo.onmessage = function (msg) {
       ("div#angle").text(msg);
    };   
     
    ws_camera_servo.onmessage = function (msg) {
       ("div#camera_angle").text(msg);
    };
    
    ws_motor.onmessage = function (msg) {
       ("div#speed").text(msg);
    };

    $('#submit_angle').click(function(event) {
        ws_servo.send($('#new_angle').val());
    });

    $('#submit_camera_angle').click(function(event) {
        ws_servo.send($('#new_camera_angle').val());
    });

    $('#submit_speed').click(function(event) {
        ws_motor.send($('#new_speed').val());
    });
});
