var AjaxHandler = (function(){

    var route = '/';

    function getCurrentUser(){
        var options = {};

        options.url = route + 'usuarios/getCurrentUser/';
        options.type = 'GET'

        return $.ajax(options);
    }

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

    function create(options){
        options.url = 'create/'
        options.type = 'POST'

        return $.ajax(options);
    }

    var publicAPI = {
        find: find,
        count: count,
        update: update,
        create: create,
        getCurrentUser: getCurrentUser
    }

    return publicAPI
})
