/**
 * Created by daniel on 5/11/16.
 */
var button = $('#irb-open-button');
var menu = $('#irb-navbar');


button.on('click', function(){
    menu.toggleClass("open-state");
})
