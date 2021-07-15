const initNotifications = () => {
    const toast = swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000,
        padding: '2em'
    });
    
    document.querySelectorAll(".notification").forEach(notification => {
        toast({
            type: notification.dataset.tags,
            title: notification.dataset.message,
            padding: '2em',
        })
    });
}

document.addEventListener("DOMContentLoaded", () => {
    initNotifications();
});