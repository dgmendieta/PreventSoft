//Transform to jQuery DataTable the objects list table
$(document).ready(function () {
    $('.list_table').DataTable({
        language: {
            "decimal": "",
            "emptyTable": "No hay información",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
            "infoEmpty": "Mostrando 0 a 0 de 0 Entradas",
            "infoFiltered": "(Filtrado de _MAX_ total entradas)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrar _MENU_ Entradas",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "Sin resultados encontrados",
            "paginate": {
                "first": "Primero",
                "last": "Último",
                "next": "Siguiente",
                "previous": "Anterior"
            }
        },
    });
});

//Controls password matching
function checkPass(input) {
                   if (input.value != document.getElementById('id_password').value) {
                           input.setCustomValidity('Las claves deben coincidir.');
                       } else {
                                 input.setCustomValidity('');
                              }
                       }
//Controls email matching
function checkEmail(input) {
                    if (input.value != document.getElementById('id_username').value) {
                            input.setCustomValidity('Los correos deben coincidir.');
                        } else {
                                  input.setCustomValidity('');
                               }
                        }   
//Shows password
$(document).ready( function(){
 
   $('#show').click(function(){
      if($(this).hasClass('fa-eye'))
      {
      $('#id_password').removeAttr('type');
      $('#show').addClass('fa-eye-slash').removeClass('fa-eye');
      }
 
      else
      {
      $('#id_password').attr('type','password');
      $('#show').addClass('fa-eye').removeClass('fa-eye-slash');
      }
       });
 
});
//Shows password
$(document).ready( function(){
 
   $('#show_2').click(function(){
      if($(this).hasClass('fa-eye'))
      {
      $('#id_password2').removeAttr('type');
      $('#show_2').addClass('fa-eye-slash').removeClass('fa-eye');
      }
 
      else
      {
      //Establecemos el atributo y valor
      $('#id_password2').attr('type','password');
      $('#show_2').addClass('fa-eye').removeClass('fa-eye-slash');
      }
       });
 
});
