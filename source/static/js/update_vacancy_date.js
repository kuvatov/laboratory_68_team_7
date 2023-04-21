$(document).ready(function () {
    let updateVacancyButtonList = $(".update_vacancy_button")
    for (let updateVacancyButton of updateVacancyButtonList) {
        $(updateVacancyButton).click(function updateVacancyDate(event) {
            event.preventDefault()
            let csrfToken = $("input[name='csrfmiddlewaretoken']").attr("value");
            $.ajax({
                url: $(this).attr("href"),
                type: 'POST',
                dataType: 'json',
                headers: {"X-CSRFToken": csrfToken},
                success: function (data) {
                    let vacancyId = data.vacancy_id;
                    let elementId = `#updated_at_${vacancyId}`;
                    $(elementId).text(data.updated_at)
                }
            });
        });
    };
});
