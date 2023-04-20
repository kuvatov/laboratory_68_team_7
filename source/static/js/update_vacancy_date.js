$(document).ready(function() {
    $('#update-date-btn').click(function() {
        var vacancyId = $('.vacancy_card').data('vacancy-id');
        var csrfToken = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            url: '/vacancies/' + vacancyId + '/update_date/',
            type: 'POST',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrfToken
            },
            success: function(data) {
                $('#updated-at').text(data.updated_at);
            }
        });
    });
});
