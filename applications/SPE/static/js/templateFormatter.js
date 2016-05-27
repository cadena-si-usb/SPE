(function(){
    $(document).ready(function(){
        $.addTemplateFormatter('AddPath',function(value,template){
            return template + value + "/preinscripcion"
        });

        $.addTemplateFormatter('Capitalize',function(value,template){
            return value.toLowerCase().replace( /\b./g, function(a){ return a.toUpperCase(); } );
        });

        $.addTemplateFormatter('Quantity',function(value,template){
            var className = ""

            if (!value) {
                className = "active";
            }

            return className
        });
    });
})();
