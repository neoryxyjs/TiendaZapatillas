
$("#nombre_vacio")[0].style.display="none";
$("#nombre_muy_largo")[0].style.display="none";

$("#marca_vacia")[0].style.display="none";

$("#categoria_vacia")[0].style.display="none";

$("#precio_vacio")[0].style.display="none";

$("#encabezado_vacio")[0].style.display="none";
$("#encabezado_muy_largo")[0].style.display="none";

$("#descripcion_vacia")[0].style.display="none";
$("#descripcion_muy_larga")[0].style.display="none";

function validarNombre(){
    let nombre = $("#nombre")[0].value;
    $("#nombre_vacio")[0].style.display="none";
    $("#nombre_muy_largo")[0].style.display="none";

    $("#nombre")[0].classList.remove("is-invalid");
    $("#nombre")[0].classList.add("is-valid");

    if (nombre.trim().length == 0){
        $("#nombre_vacio")[0].style.display="inline";
        $("#nombre_muy_largo")[0].style.display="none";

        $("#nombre")[0].classList.add("is-invalid");
        return false;
    }
    if(nombre.trim().length > 32){
        $("#nombre_vacio")[0].style.display="none";
        $("#nombre_muy_largo")[0].style.display="inline";
        
        $("#nombre")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

function validarMarca(){
    let marca = document.getElementById("marca");
    let marcaSeleccionada = marca.value;
    $("#marca_vacia")[0].style.display="none";
    $("#marca")[0].classList.remove("is-invalid");
    $("#marca")[0].classList.add("is-valid");
    if(marcaSeleccionada == ""){
        $("#marca_vacia")[0].style.display="inline";
        $("#marca")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

function validarCategoria(){
    let categoria = document.getElementById("categoria");
    let categoriaSeleccionada = categoria.value;
    $("#categoria_vacia")[0].style.display="none";
    $("#categoria")[0].classList.remove("is-invalid");
    $("#categoria")[0].classList.add("is-valid");
    if(categoriaSeleccionada == ""){
        $("#categoria_vacia")[0].style.display="inline";
        $("#categoria")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

function validarPrecio(){
    let precio = $("#precio")[0].value;
    $("#precio_vacio")[0].style.display="none";

    $("#precio")[0].classList.remove("is-invalid");
    $("#precio")[0].classList.add("is-valid");

    if (precio.trim().length == 0){
        $("#precio_vacio")[0].style.display="inline";

        $("#precio")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

function validarEncabezado(){
    let nombre = $("#encabezado")[0].value;
    $("#encabezado_vacio")[0].style.display="none";
    $("#encabezado_muy_largo")[0].style.display="none";

    $("#encabezado")[0].classList.remove("is-invalid");
    $("#encabezado")[0].classList.add("is-valid");

    if (nombre.trim().length == 0){
        $("#encabezado_vacio")[0].style.display="inline";
        $("#encabezado_muy_largo")[0].style.display="none";

        $("#encabezado")[0].classList.add("is-invalid");
        return false;
    }
    if(nombre.length > 100){
        $("#encabezado_vacio")[0].style.display="none";
        $("#encabezado_muy_largo")[0].style.display="inline";
        
        $("#encabezado")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

function validarDescripcion(){
    let descripcion = $("#descripcion")[0].value;
    $("#descripcion_vacia")[0].style.display="none";
    $("#descripcion_muy_larga")[0].style.display="none";

    $("#descripcion")[0].classList.remove("is-invalid");
    $("#descripcion")[0].classList.add("is-valid");

    if (descripcion.trim().length == 0){
        $("#descripcion_vacia")[0].style.display="inline";
        $("#descripcion_muy_larga")[0].style.display="none";

        $("#descripcion")[0].classList.add("is-invalid");
        return false;
    }
    if(descripcion.length > 300){
        $("#descripcion_vacia")[0].style.display="none";
        $("#descripcion_muy_larga")[0].style.display="inline";

        $("#descripcion")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}


function validarNuevaZapatilla(){
    if(!validarNombre()) return;
    if(!validarMarca()) return;
    if(!validarCategoria()) return;
    if(!validarPrecio()) return;
    if(!validarEncabezado()) return;
    if(!validarDescripcion()) return;

    document.getElementById("nuevaZapatilla").submit();
}

function validarEditarZapatilla(){
    if(!validarNombre()) return;
    if(!validarMarca()) return;
    if(!validarCategoria()) return;
    if(!validarPrecio()) return;
    if(!validarEncabezado()) return;
    if(!validarDescripcion()) return;
    
    document.getElementById("editarZapatilla").submit();
}

