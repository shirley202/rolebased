document.addEventListener('DOMContentLoaded', function() {
    var materiaField = document.getElementById('id_materia');
    var unidadesField = document.getElementById('id_unidades');
    var contenidosField = document.getElementById('id_contenidos');

    // Cuando se selecciona una materia
    materiaField.addEventListener('change', function() {
        var materiaId = materiaField.value;

        // Realizar una solicitud AJAX para obtener las unidades y contenidos asociados a la materia seleccionada
        fetch('/obtener_unidades_y_contenidos/?materia_id=' + materiaId)
            .then(response => response.json())
            .then(data => {
                // Limpiar las opciones actuales
                unidadesField.innerHTML = '';
                contenidosField.innerHTML = '';

                // Agregar las nuevas opciones
                data.unidades.forEach(unidad => {
                    var option = document.createElement('option');
                    option.text = unidad.nombre;
                    option.value = unidad.id;
                    unidadesField.add(option);
                });

                data.contenidos.forEach(contenido => {
                    var option = document.createElement('option');
                    option.text = contenido.nombre;
                    option.value = contenido.id;
                    contenidosField.add(option);
                });
            });
    });
});
