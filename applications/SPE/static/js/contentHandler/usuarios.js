(function(){

$('#usuariosIndex').ready(function(){
    var ajaxHandler = AjaxHandler();

    var usuarios = [],
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

        ajaxHandler.count('usuarios',options).success(function(res){
            max = res;
            $('#cantidad').html(max.toString());
            getUsuarios();
        })
    }

    function getUsuarios(){
        ajaxHandler.find('usuarios',options).success(function(res){
            usuarios = JSON.parse(res);
            if (usuarios.length > 0){
                $("#elBody").loadTemplate('#template', usuarios);
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

    // Funcion que trae mas usuarios para paginacion

    function getMoreUsuarios(evt){
        filters.page = usuarios.length.toString();

        options.data = $.param(filters,true);
        //AJAX CALL TO SERVER
        ajaxHandler.find('usuarios',options).success(function(res){
            res = JSON.parse(res);
            for (var i = 0; i < res.length; i++){
                usuarios.push(res[i]);
            }
            disableButtonOnMax();

            $("#elBody").loadTemplate('#template',res,{append:true});
        });
    }

    // Cambio de area de trabajo

    function changeArea(evt){
        area = $(this).val();

        if (area){
            filter["area"] = area;
        }
        else {
            delete filter.area
        }

        filters.filter = JSON.stringify(filter);

        getInfo();
    }

    //Desabilitar boton de MAS

    function disableButtonOnMax(){
        if ((max) && (usuarios.length.toString() != max)) {
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
                search["key"] = "first_name"
                search["value"] = val;
            } else {
                search = {}
            }

            filters.searchTerm = JSON.stringify(search);

            getInfo();
        }, ms);
    }


    $('#target').change(changeArea);
    $('#search').keyup(searchTerm);
    $('#next').click(getMoreUsuarios);
    $('.uai-table-header').click(changeOrder);
});
})();
