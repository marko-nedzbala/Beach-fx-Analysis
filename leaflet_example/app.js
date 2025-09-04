// var map = L.map('map').setView([51.505, -0.09], 13);
// 40.3615° N, -73.9740

let map = L.map('map').setView([40.361, -73.974], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);









