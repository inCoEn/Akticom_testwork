$("#uploading_form").submit(function (event) {
    event.preventDefault();
    console.log($("#uploading_form"));
    console.log($("#id_csv_file").val());
    $.ajax("getajax", {data:$("#uploading_form").val(), csrfmiddlewaretoken:'{{csrf_token}}'});
});
