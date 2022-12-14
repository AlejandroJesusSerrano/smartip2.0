import swal from 'sweetalert';

let Swal = swal;

const deleteModelBtn = document.getElementById('deleteModelBtn')

function deleteModel(id){
     Swal.fire({
          "title": "¿estas seguro?",
          "text": "vas a eliminar el modelo de la Base de Datos, esta acción no se puede deshacer",
          "icon": "warning",
          "showCancelButton": true,
          "cancelButtonText": "No, Cancelar",
          "cancelButtonColor": "#13a168",
          "confirmButtonColor": "#dc3545",
          "confirmButtonText": "Si, Eliminar", 
          "reverseButtons":true,
     })
     .then(function(result) {
          if(result.isConfirmed) {
               window.location.href = "/dev_model_delete/"+id+"/"
          }
     })
}

deleteModelBtn.addEventListener('click', ()=>
{
     deleteModel(id)
})