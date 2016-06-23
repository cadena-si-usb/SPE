(function(){

    $('#mis_pasantias_index').ready(function(){
        var ajaxHandler = AjaxHandler();

        var misPasantias = [],
            materias = [],
            max, area, options = {},
            filters = {order:'id',side:'>',limit:'4',page:'0'},
            filter = {
                "pasantias": {
                    "estudiante": 6
                }
            },
            search = {},
            codigos_materia = {},
            currentUser = {};

        function activate(){
            ajaxHandler.getCurrentUser().success(function(res){
                currentUser = JSON.parse(res);
                getInfo();
            });
        }

        activate();

        function getInfo(){
            options = {};

            if (filters.page && filters.page != "") {
                filters.page = "0";
            }

            options.data = $.param(filters,true);

            if (currentUser.estudiante) {
                getMaterias();
                //getMisPasantias();
            }
        }

        function getMisPasantias(){
            var params = jQuery.extend(true, {}, options);
            
            filter = {
                "pasantias": {
                    "estudiante": currentUser.estudiante.id
                }
            }

            filters.filter = JSON.stringify(filter["pasantias"]);

            params.data = $.param(filters,true);

            ajaxHandler.find('mis_pasantias',params).success(function(res){
                misPasantias = JSON.parse(res);

                if (misPasantias.length > 0){
                    var codigo, pasantia;

                    for (var i = 0; i < misPasantias.length; i++) {
                        codigo = misPasantias[i].Materia.codigo;
                        pasantia = misPasantias[i].Pasantia;
                        pasantia.periodo = misPasantias[i].Periodo;
                        
                        if (!codigos_materia[codigo]) {
                            codigos_materia[codigo] = [];
                        }

                        codigos_materia[codigo].push(pasantia)
                    }

                    for (var key in codigos_materia) {
                        $("#" + key).loadTemplate('#tmplPasantias', codigos_materia[key]);
                    }
                }
                else {
                    var template = '<tr><td class="text-center" colspan="42">',
                        msg = "No hay elementos en la tabla";

                    template += msg + "</td></tr>";

                    $("#pasantias").html(template);
                }
            });
        }

        function getMaterias(){
            var params = jQuery.extend(true, {}, options);

            if (filter["materias"]) {
                filters.filter = JSON.stringify(filter["materias"]);
            } else {
                delete filters.filter
            }

            params.data = $.param(filters,true);

            ajaxHandler.find('materias',params).success(function(res){
                materias = JSON.parse(res);
                if (materias.length > 0){
                    for (var i = 0; i < materias.length; i++) {
                        codigos_materia[materias[i].codigo] = [];
                    }

                    $("#materias").loadTemplate('#tmplMaterias', materias);
                }
                else {
                    var template = '<tr><td class="text-center" colspan="42">',
                        msg = "No hay elementos en la tabla";

                    template += msg + "</td></tr>";

                    $("#materias").html(template);
                }

                getMisPasantias();
            });
        }
    });
})();
/**
 * Created by daniel on 5/16/16.
 */
