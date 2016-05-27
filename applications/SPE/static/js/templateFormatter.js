(function(){
    $(document).ready(function(){
        $.addTemplateFormatter('AddPath',function(value,template){
            return template + value
        });

        $.addTemplateFormatter('Capitalize',function(value,template){
            return value.toLowerCase().replace( /\b./g, function(a){ return a.toUpperCase(); } );
        });

        $.addTemplateFormatter('ObtenerAnio',function(value,template){
            things = value.split(" ")
            console.log(things)
            return things[things.length-1]
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
