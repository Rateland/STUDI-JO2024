fetch('URL_PROTEGEE', {
    method: 'GET', // Ou 'POST', etc.
    headers: {
        'Authorization': 'JWT ' + localStorage.getItem('jwtToken'),
        'Content-Type': 'application/json'
    }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
