

$("#save").on("click", () => {

    let title = $("#cardTitle").val();
    let text = $("#cardText").val();

    if (title === "" || text === ""){
        alert("Please fill both the fields");
        return;
    }
    let formData = $("#cardForm").serialize();

    $.ajax({
        method: 'post',
        url: '/',
        data: formData,

        success: (data) => {
            if (data.error){
                alert(data.msg);
                return;
            }
            let card_html = `<div class="col-md-3" id="card_`+data.id+`">
            <div class="card" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title">Title: `+data.title+`</h5>
                    <h5 class="card-title">Text: `+data.text+`</h5>
                    <div class="row">
                        <div class="col">
                            <button type="button" class="btn btn-danger remove" data-href="`+data.id+`" data-text="`+data.title+`">Remove</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>`

        $("#cards").append(card_html);
        $("#cardForm")[0].reset();
        }
    })
})

$(document).on("click", ".remove", (e) => {

    let elem = $(e.currentTarget);
    
    let id = elem.attr("data-href")
    let text = elem.attr("data-text")
    
    $("#modal_body").html(text)

    $("#deleteBtn").attr("data-id", id);

    $("#exampleModal").modal("show");
})

$("#deleteBtn").on("click", (e) => {
    let elem = $(e.currentTarget);
    let pk = elem.attr("data-id")
    $.ajax({
        method: 'get',
        url: '/delete/'+pk,
        data: {},
        success: (data) => {
            $("#exampleModal").modal("hide");
            $("#card_"+pk).remove();
        }
    })
})