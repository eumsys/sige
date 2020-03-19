$(document).ready(function(){

	var socket = new WebSocket('ws://127.0.0.1:8000/sucursales/');
	socket.onopen = websocket_conexion_ok;
	socket.onmessage = websocket_msj_recibido;

	

});

function websocket_conexion_ok(){
	alert('La conexión se ha establecidoo');
}

function websocket_msj_recibido(e){
	alert('mensaje recibido');
	datos = JSON.parse(e.data);
	$('.progress-bar').css('width', datos.nombre +'%')
	/*
	codigo = '<div class="col s12">'				+
				'<div class="nombre">'				+
					'<h4>'+ datos.nombre +'</h4>'	+
				'</div>'							+
				'<div class="contenido">'			+
					'<p>'+ datos.mensaje +'</p>'	+
				'</div>'							+
			'</div>';
	$('#conversacion').append(codigo);
	*/
}