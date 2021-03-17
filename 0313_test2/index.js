


const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);


function DarkMode(){
    const checkbox=$("input[name=darkModeSwitch]");
    const header = $("#header");
    const container = $(".container");
    const footer = $("#footer");
    
    
    const faqBtn = $("#faqBtn");
    const main=$("#main");
    const mainLogo=$("#mainLogo");
    
    console.log("체크박스 쿼리",checkbox);
    console.log("체크박스상황",checkbox.checked);

    if(checkbox.checked){
        header.style.backgroundColor = "#000000";
        container.style.backgroundColor = "#000000";
        footer.style.backgroundColor = "#000000";
        footer.style.color="#ffffff"
    
    
        faqBtn.style.backgroundColor = "#000000";
        faqBtn.style.color="#ffffff";
        main.style.color="#ffffff";
    
        mainLogo.src="./img/Night.png";
    }
    
    else{

        header.style.backgroundColor = "#ffffff";
        container.style.backgroundColor = "#ffffff";
        footer.style.backgroundColor = "#ffffff";
        footer.style.color="#000000"
    
    
        faqBtn.style.backgroundColor = "#ffffff";
        faqBtn.style.color="#000000";
        main.style.color="#000000";
    
        mainLogo.src="./img/Day.png";
    }
    
}   
