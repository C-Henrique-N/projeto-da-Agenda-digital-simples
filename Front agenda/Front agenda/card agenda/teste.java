const titulo = document.getElementById("titulo");
const data = document.getElementById("data");
const hora = document.getElementById("hora");
const cor = document.getElementById("cor");

const botao = document.getElementById("adicionar");
const lista = document.getElementById("lista");

botao.addEventListener("click", function(){

    const card = document.createElement("div");
    card.className = "card";

    const lado = document.createElement("div");
    lado.className = "lado";

    const conteudo = document.createElement("div");
    conteudo.className = "conteudo";

    if(cor.value == "vermelho"){
        lado.style.background = "#ff4d4d";
        card.style.background = "#ffd6d6";
    }

    if(cor.value == "verde"){
        lado.style.background = "#4CAF50";
        card.style.background = "#d9f5db";
    }

    if(cor.value == "azul"){
        lado.style.background = "#2196F3";
        card.style.background = "#d9ecff";
    }

    if(cor.value == "amarelo"){
        lado.style.background = "#FFD54F";
        card.style.background = "#fff8d6";
    }

    lado.innerHTML = `
        <p>${data.value}</p>
        <p>${hora.value}</p>
    `;

    conteudo.innerHTML = `
        <h2>${titulo.value}</h2>
    `;

    card.appendChild(lado);
    card.appendChild(conteudo);

    lista.appendChild(card);

    titulo.value = "";
    data.value = "";
    hora.value = "";
});