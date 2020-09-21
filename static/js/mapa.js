$(document).ready(function() {
    $(function() {
        $('[data-toggle="popover"]').popover()
    })

    $('.popover-dismiss').popover({
        trigger: 'focus'
    })
});

// Hacen que los popover salgen donde se hace click. 

$('path').click(function(e) {

    $('.popover').hide();
    var id = $(this).attr('id');
    document.getElementById(id + "_pop").removeAttribute("hidden");

    var offset = $(this).offset();
    var left = e.pageX;
    var top = e.pageY;
    var theHeight = $('.popover').height();
    $('#' + id + '_pop').show();
    $('#' + id + '_pop').css('left', (left + 10) + 'px');
    $('#' + id + '_pop').css('top', (top - (theHeight / 2) - 10) + 'px');
    console.log(id + '_pop');

});

$(document).on('click', function(event) {
    if (!$(event.target).closest('path').length) {
        $('.popover').hide();
    }
});