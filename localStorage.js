function login(username, password) {
    fetch('/api-token-auth/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({username: username, password: password})
    })
    .then(response => response.json())
    .then(data => {
        if (data.token) {
            localStorage.setItem('jwtToken', data.token);
        } else {
            console.error('Token not received');
        }
    })
    .catch(error => console.error('Error:', error));
}
