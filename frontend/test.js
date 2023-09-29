import axios from 'axios';

axios.get('https://jsonplaceholder.typicode.com/todos')
.then(response=>{
    console.log(response.data);
})

fetch('https://jsonplaceholder.typicode.com/todos')
.then(response=>response.json())
.then(data=>{
    console.log(data);
})