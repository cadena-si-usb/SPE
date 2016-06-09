var AjaxHandler = (function(){

    var route = '/';

    function find(table,options){
        options.url = route + table + '/get/';
        options.type = 'GET'

        return $.ajax(options);
    }
    
    function count(table,options){
        options.url = route + table + '/count/';
        options.type = 'GET'

        return $.ajax(options);
    }

    function update(options){
        options.url = 'update/'
        options.type = 'PUT'

        return $.ajax(options);
    }

    var publicAPI = {
        find: find,
        count: count,
        update: update
    }

    return publicAPI
})
