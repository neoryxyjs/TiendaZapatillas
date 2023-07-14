
$("#categoria_vacia")[0].style.display="none";
$("#categoria_muy_larga")[0].style.display="none";



function validarNombreCategoria(){
    let nombre = $("#nombreCategoria")[0].value;
    $("#categoria_vacia")[0].style.display="none";
    $("#categoria_muy_larga")[0].style.display="none";

    $("#nombreCategoria")[0].classList.remove("is-invalid");
    $("#nombreCategoria")[0].classList.add("is-valid");

    if (nombre.trim().length == 0){
        $("#categoria_vacia")[0].style.display="inline";
        $("#categoria_muy_larga")[0].style.display="none";

        $("#nombreCategoria")[0].classList.add("is-invalid");
        return false;
    }
    if(nombre.trim().length > 32){
        $("#categoria_vacia")[0].style.display="inline";
        $("#categoria_muy_larga")[0].style.display="inline";
        
        $("#nombreCategoria")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

function validarNuevaCategoria(){
    if(!validarNombreCategoria()) return;
    document.getElementById("nuevaCategoria").submit();
}

function validarEditarCategoria(){
    if(!validarNombreCategoria()) return;
    document.getElementById("editarCategoria").submit();
}