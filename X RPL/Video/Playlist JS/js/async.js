document.querySelector("#klik").addEventListener("click", tampil);

async function tampil() {
    const url = "http://jsonplaceholder.typicode.com/users";

    const res = await fetch(url);

    const data = await res.json();

    let out = "<ul>";
    data.forEach(element => {
        console.log(element.name);
        out += `<li>${element.name}</li>`;
    });

    out += "</ul>";
    document.querySelector("#isi").innerHTML = out;
}