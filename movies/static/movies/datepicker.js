const birthdate = document.getElementById('id_birthdate')
birthdate.addEventListener("click",function() {openDatepicker()})



function openDatepicker(){
    new Litepicker({
        element: document.getElementById('id_birthdate'),
        singleMode: true,
    })
}