import Swal from "sweetalert2";

export function toastMessage(icono='error', titulo='Failed'){
    const Toast = Swal.mixin({
        toast: true,
        position: 'top',
        showConfirmButton: false,
        timer: 2000,
        timerProgressBar: true,
        didOpen: (toast) => {
          toast.addEventListener('mouseenter', Swal.stopTimer)
          toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
      })
      
      Toast.fire({
        icon: icono,
        title: titulo,
        customClass: {
            popup: 'swal-toast',
            container: 'swal-toast-container'
          }
      })
}