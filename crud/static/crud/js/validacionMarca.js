
$("#marca_vacia")[0].style.display="none";
$("#marca_muy_larga")[0].style.display="none";


function validarNombreMarca(){
    let nombre = $("#nombreMarca")[0].value;
    $("#marca_vacia")[0].style.display="none";
    $("#marca_muy_larga")[0].style.display="none";

    $("#nombreMarca")[0].classList.remove("is-invalid");
    $("#nombreMarca")[0].classList.add("is-valid");

    if (nombre.trim().length == 0){
        $("#marca_vacia")[0].style.display="inline";
        $("#marca_muy_larga")[0].style.display="none";

        $("#nombreMarca")[0].classList.add("is-invalid");
        return false;
    }
    if(nombre.trim().length > 32){
        $("#marca_vacia")[0].style.display="none";
        $("#marca_muy_larga")[0].style.display="inline";
        
        $("#nombreMarca")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

function validarNuevaMarca(){
    if(!validarNombreMarca()) return;
    document.getElementById("nuevaMarca").submit();
}

function validarEditarMarca(){
    if(!validarNombreMarca()) return;
    document.getElementById("editarMarca").submit();
}
