const initTransitions = () => {
    document.querySelector(".transition").addEventListener("click" , event => {
        event.preventDefault();
        fetch(event.currentTarget.href)
        .then(response => {
            if (response.ok) return response.json()
        })
        .then(data => {
            swal({
                title: 'Success!',
                text: data.message,
                timer: 1000,
                type: 'success',
                padding: '2em'
            }).then(result => {
                window.location.reload();
            });
            
        })
    });
}

document.addEventListener("DOMContentLoaded", () => {
    initTransitions();
});