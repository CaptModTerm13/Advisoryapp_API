function toggleDescription(selectElement) {
    var descriptionContainer = document.getElementById("descriptionContainer");
    var descriptionInput = document.getElementById("Description");

    if (selectElement.value === "option4") {
        descriptionContainer.style.display = "block";
        descriptionInput.required = true;
    } else {
        descriptionContainer.style.display = "none";
        descriptionInput.required = false;
    }
}
window.addEventListener("DOMContentLoaded",function(){
    var form=document.querySelector("form");
    form.addEventListener("submit",function(event){
        var activitySelect=document.getElementById("activity_type");
        if(activitySelect.value=="option0"){
            event.preventDefault();
            alert("Please select a valid option")
        }
    });
});
