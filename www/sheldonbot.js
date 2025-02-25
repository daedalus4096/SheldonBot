var API_ENDPOINT = 'https://34r916h6k8.execute-api.us-west-1.amazonaws.com/prod/random';

var errorDiv = document.getElementById('error-message')
var successDiv = document.getElementById('success-message')
var resultsDiv = document.getElementById('results-message')
var imageDiv = document.getElementById('image-container')

function clearNotifications() {
    errorDiv.textContent = '';
    resultsDiv.textContent = '';
    successDiv.textContent = '';
    imageDiv.textContent = '';
}

// When buttons are clicked, this is run passing values to API Gateway call
document.getElementById('requestButton').addEventListener('click', function(e) { sendData(e, 'sheldon'); });

function sendData (e, pref) {
    e.preventDefault()
    clearNotifications()
    fetch(API_ENDPOINT + '?' + new URLSearchParams({ tag: pref }), {
        headers:{
            "Content-type": "application/json"
        },
        method: 'GET',
        mode: 'cors'
    })
    .then((resp) => resp.json())
    .then(function(data) {
        console.log(data)
        const body = JSON.parse(data.body);
        const img = document.createElement('img');
        img.src = body.Image;
        img.alt = pref;
        imageDiv.innerHTML = '';
        imageDiv.appendChild(img);
    })
    .catch(function(err) {
        errorDiv.textContent = 'Oops! Error Error:\n' + err.toString();
        console.log(err)
    });
};
