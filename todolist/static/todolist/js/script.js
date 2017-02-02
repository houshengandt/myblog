/**
 * Created by housh on 2017/1/24.
 */

$(document).ready(function () {
    $('input[class="uk-checkbox"]').each(function () {
        $(this).on('click', function () {
            var task_id = $(this).attr('id');
            if($(this).is(':checked')==true) {
                $(this).next().text("已完成");
                $('div[task-id=' + task_id + ']').addClass('uk-text-muted');
                $.get('/complete-task/', { pk: task_id })
            }else {
                $(this).next().text("未完成");
                $('div[task-id=' + task_id + ']').removeClass('uk-text-muted');
                $.get('/uncomplete-task/', { pk: task_id })
            }
        })
    });
    $('#uncompleted-button').click(function () {
        $(window).scrollTo('#uncompleted', 800);
    })
});
