$(document).ready(function () {
    $(".new_folder").mouseover(function(e) {
        e.preventDefault();
        $(".new_folder .static_text").removeClass('static_text');
        $(this).addClass('active_text')
    })
    $(".new_file").mouseover(function(e) {
        e.preventDefault();
        $(".new_file .static_text").removeClass('static_text');
        $(this).addClass('active_text')
    })
})
