(function(){
	$('#perfil_estudiante').ready(function(){
		$("#actualizar_usuario").submit(function( event ) {
			event.preventDefault();
			$.ajax({
				data: $("#actualizar_usuario").serialize(),
				url: '/SPE/usuarios/actualizar',
				type: 'PUT'
			});

			$(location).attr('href', '/SPE/usuarios/perfil')
		});
	});
})();
