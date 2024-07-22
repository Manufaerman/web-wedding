
const navLink = document.getElementsByClassName('nav-link')
console.log(navLink[2])
for(var i = 0; i <= navLink.length; i++){
    console.log(i)
    navLink[i].addEventListener('click', activarDesactivar, false);
}

function activarDesactivar(){
    if(navLink.classList.contains('activo')){
        navLink.classList.remove('activo')
        }
    navLink.classList.add('activo')
    console.log(navLink.classList);

}