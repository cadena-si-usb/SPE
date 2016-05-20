(function(){

    $('#misPasantiasIndex').ready(function(){
        var ajaxHandler = AjaxHandler();

        var misPasantias = [],
            max, area, options = {},
            filters = {order:'id',side:'>',limit:'4',page:'0'},
            filter = {
                id_estudiante: "1"
            },
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

            filters.filter = JSON.stringify(filter);

            options.data = $.param(filters,true);

            ajaxHandler.count('pasantias',options).success(function(res){
                max = res;
                $('#cantidad').html(max.toString());
                getMisPasantias();
            })
        }

        function getMisPasantias(){
            ajaxHandler.find('pasantias',options).success(function(res){
                misPasantias = JSON.parse(res);
                if (misPasantias.length > 0){
                    $("#elBody").loadTemplate('#template', misPasantias);
                }
                else {
                    var template = '<tr><td class="text-center" colspan="42">',
                        msg = "No hay elementos en la tabla";

                    template += msg + "</td></tr>";

                    $("#elBody").html(template);
                }
            });
        }
    });
})();
/**
 * Created by daniel on 5/16/16.
 */
