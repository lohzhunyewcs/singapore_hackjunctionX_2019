let a = {};
document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelector('#choice').onchange = () =>{
        // Initialize new Ajax request
        const request = new XMLHttpRequest();
        request.open('POST', 'http://127.0.0.1:8000/api/makechoice/');

        request.onload = () =>{
            const data = JSON.parse(JSON.parse(request.responseText));
            a = data;
            console.log(`data: ${data}`)
            console.log(`typeof data: ${typeof(data)}`)
            document.querySelector('#category').value = data['category'];
            document.querySelector('#price').value = data['price'];
        }

        // const data = new FormData();
        // data.append('choice', document.querySelector('#choice'));
        let data = JSON.stringify({'choice': document.querySelector('#choice').value})
        request.send(data); 
    };
});