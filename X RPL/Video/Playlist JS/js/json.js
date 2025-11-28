document.querySelector("#klik").addEventListener("click",tampil);

function tampil(paramas) {
    // console.log("tes")
    // let url = "https://jsonplaceholder.typicode.com/todos/1"
    let url = "js/tblmenu.json"
    fetch(url)
    // .then(response => response.json())
    .then(function (res) {
        return res.json();
    })
    // .then(json => console.log(json))
    .then(function (data) {
        // console.log(data);
        let output = <h1>DATA MENU</h1> 
        data.forEach(element => {
            output += `<tr>
                <td>${element.menu}</td>
                <td>${element.harga}</td>
                <td>${element.warna[0]}</td>
            </tr>`;
        });
        output += "</table>";document.querySelector("#isi").innerHTML= "<h1>DATA MENU</h1>";
    })
}


// let tblmenu = [ 
// {

//     "idmenu" : 1,
//     "idkategori" : 1,
//     "menu" : "Apel manalagi",
//     "harga" : 3000,
//     "warna" : ["merah", "kuning", "hijau"],
//     "stok" : true,
//     "keterangan" : null

// },
// {

//     "idmenu" : 2,
//     "idkategori" : 1,
//     "menu" : "Pisang",
//     "harga" : 2000,
//     "warna" : ["merah", "kuning"],
//     "stok" : false,
//     "keterangan" : null

// },

// ]

// console.log(tblmenu[0].menu);