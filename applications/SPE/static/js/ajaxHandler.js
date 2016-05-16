var AjaxHandler = (function(){

    function find(options){
        options.url = 'get/'
        options.type = 'GET'

        return $.ajax(options);
    }
    
    function count(options){
        options.url = 'count/'
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
