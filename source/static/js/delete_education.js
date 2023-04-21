$(document).ready(function (){
    let deleteBtnList = $(".delete-education")


    for (let deleteBtn of deleteBtnList) {
        $(deleteBtn).click(function deleteEducation(event) {
            event.preventDefault()
            let csrfToken = $("input[name='csrfmiddlewaretoken']").attr("value")
            let educationId = $(deleteBtn).data("education-id")
            console.log(educationId)
            $.ajax({
                url: $(this).attr("href"),
                method: 'POST',
                headers: {"X-CSRFToken": csrfToken},
                data: {education_id: educationId},
                success: function (data, status) {
                    $(`#education-card-${educationId}`).remove()
                    console.log(data);
                    console.log(status);
                },
                error: function (response, status) {
                    console.log(status);
                    console.log(response);
                }
            });
        });
    }
})