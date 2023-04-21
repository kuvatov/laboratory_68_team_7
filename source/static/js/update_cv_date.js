$(document).ready(function () {

    let updateCVBtnList = $(".updateCVBtn")
    console.log(updateCVBtnList)

    for (let updateCVBtn of updateCVBtnList) {
        $(updateCVBtn).click(function updateCvDate(event) {
            event.preventDefault()
            let csrfToken = $("input[name='csrfmiddlewaretoken']").attr("value");
            $.ajax({
                url: $(this).attr("href"),
                type: 'POST',
                dataType: 'json',
                headers: {"X-CSRFToken": csrfToken},
                success: function (data) {
                    console.log(data.cv_id)
                    console.log(data.updated_at)
                    let updatedCvTime = $(`small[data-cvId="${data.cv_id}"]`)
                    updatedCvTime.text(`Обновлен ${data.updated_at}`);
                }
            });
        });
    }
    ;
});