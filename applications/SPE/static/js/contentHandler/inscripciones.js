(function(){

$('#inscripcionesIndex').ready(function(){
    var ajaxHandler = AjaxHandler();

    var inscripciones = [],
        max, area, options = {},
        filters = {order:'id',side:'>',limit:'4',page:'0'},
        filter = {},
        search = {};

    function activate(){
        getInfo();
    }

    activate();

    function getInfo(){
        options = {};

        if (filters.page && filters.page != "") {
            filters.page = "0";
        }

        options.data = $.param(filters,true);

        ajaxHandler.count('inscripciones',options).success(function(res){
            max = res;
            $('#cantidad').html(max.toString());
            getInscripciones();
        })
    }

    function getInscripciones(){
        ajaxHandler.find('inscripciones',options).success(function(res){
            inscripciones = JSON.parse(res);
            if (inscripciones.length > 0){
                $("#elBody").loadTemplate('#template', inscripciones);
            }
            else {
                var template = '<tr><td class="text-center" colspan="42">',
                    msg = "No hay elementos en la tabla";

                template += msg + "</td></tr>";

                $("#elBody").html(template);
            }
        });
    }

    // Cambiar orden de los elementos

    function changeOrder(evt){
        var order = this.id,
            side = filters.side,
            current = filters.order;

        if (order != current){
            filters.order = order;
            filters.side = '>'
        }
        else {
            if (filters.side === '>') {
                filters.side = '<'
            }
            else {
                filters.side = '>'
            }
            filters.order = order;
        }

        setCaret($(this));

        getInfo();
    }

    function setCaret(elem){
        var isOrdered = $('#orderBy').length,
            caret;

        if (isOrdered){
            $('#orderBy').remove();
        }

        if (filters.side === ">"){
            caret = "down"
        }
        else {
            caret = "up"
        }

        var fa = "fa fa-caret-square-o-" + caret
        elem.append(" <i id='orderBy' class='"+ fa +"'></i>")
    }

    // Funcion que trae mas inscripciones para paginacion

    function getMoreInscripciones(evt){
        filters.page = inscripciones.length.toString();

        options.data = $.param(filters,true);
        //AJAX CALL TO SERVER
        ajaxHandler.find('inscripciones',options).success(function(res){
            res = JSON.parse(res);
            for (var i = 0; i < res.length; i++){
                inscripciones.push(res[i]);
            }
            disableButtonOnMax();

            $("#elBody").loadTemplate('#template',res,{append:true});
        });
    }

    //Desabilitar boton de MAS

    function disableButtonOnMax(){
        if ((max) && (inscripciones.length.toString() != max)) {
            $("#next").prop('disabled',false);
        }
        else {
            $("#next").prop('disabled',true);
        }
    }

    //Buscador

    function searchTerm(evt){
        var delay = (function(){
            var timer = 0;
            return function(callback, ms){
            clearTimeout(timer);
            timer = setTimeout(callback, ms);
            };
        })();

        var val = this.value,
            ms = 200;

        delay(function(){
            if (val){
                search["key"] = "nombre"
                search["value"] = val;
            } else {
                search = {}
            }

            filters.searchTerm = JSON.stringify(search);

            getInfo();
        }, ms);
    }

    function updateInscripcion(item, changes){
        changes = {
            id: 1,
            nombre: "prueba"
        };

        options.data = changes;

        ajaxHandler.update(options).then(function(res){
            res = JSON.parse(res);
        });
    }

    $('#updateInscripcion').click(updateInscripcion);
    $('#search').keyup(searchTerm);
    $('#next').click(getMoreInscripciones);
    $('.uai-table-header').click(changeOrder);
});
})();
