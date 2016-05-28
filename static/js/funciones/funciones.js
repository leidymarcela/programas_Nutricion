function buscar_ajax() {
    return $.ajax({
        url: "/buscar_beneficiario/",
        type: 'get',
        data: {numero_documento: $("#numid").val()}
    });
}
function barrios() {
    $.ajax({
            url: "/barrio/",
            type: 'get',
            data: {comuna: $("#comunas").val()},
        })
        .done(function (data) {
            $("#barrio").html("<option value'0'>Seleccione</option>");
            for (var i = 0; i < data.length; i++) {
                $("#barrio").append("<option value='" + data[i].pk + "'>" + data[i].fields.name + "</option>");
            }
        })
}
$(window).ready(function(){
    $("#button_buscar").click(function() {
        buscar_ajax()
        .done(function (data) {
            if (data.resultado == 0) {
                var error = 'El beneficiario no existe o el campo número de identificación se encuentra vacio';
                $("#numid").focus();
                $("#resp").text(error);
                $("#res").delay().slideUp(200, function () {
                    $(this).show(500);
                    $(this).delay(2000).hide(1000);
                });
            }
            else {
                $("#ids").val(data.id);
                $("#nombres").text(data.name + ' ' + data.apellido);
                $("#documentos").text(data.documento + ' ' + data.numero_documento);
                $("#programas").text(data.programa);
                $("#fecha_de_registro").text(data.fecha_registro);
                $("#button_transferir").show();
            }
        })
        .fail(function () {
            var error = "El campo Número de id esta vacio";
            $("#nombres").text(error);
            $("#numid").focus();
        });
    });

    $("#comunas").change( function(){
        barrios();
    });
    $(function() {
        $( document ).tooltip();
    });

    $("#button_transferir").click(function() {
        buscar_ajax()
        .done(function (data) {
            if (data.resultado == 0) {
                var error = 'No encontrado';
                $("#nombres").text(error);
            }
            else {
                $("#nombre").val(data.name);
                $("#apellido").val(data.apellido);
                $("#documento").val(data.documento_id);
                $("#numero_documento").val(data.numero_documento);
                $("#programa").val(data.programa_id);
                $("#fecha_nacimiento").val(data.fecha_de_nacimiento);
                $("#direccion").val(data.direccion);
                $("#comunas").val(data.comuna);
                $("#eps").val(data.eps_id);
                $("#barrio").append("<option value='" + data.barrio_id + "' selected>" + data.barrio + "</option>");

                $("#form-modificar").delay().slideUp(800, function () {
                    $(this).show(1000);
                });
            }
        })
        .fail(function () {
            var error = " ";
            $("#nombres").text(error);
            $("#numid").focus();
        });
    });
    $('#form-modificar').hide();
    $('#button_transferir').hide();
    $('#res').hide();

    $("#respuesta").delay(3000).slideUp(500, function () {
            $(this).hide(2000);
    });

    $('#imprimir_lista').click( function(){
            $('#respuesta1').hide(3000);
            window.open('/generar_pdf', '_blank');
    });

});