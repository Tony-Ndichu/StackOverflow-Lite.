var overlay = document.getElementById('overlay');
let modalOpener = document.getElementById('open-modal')
let modalCloser = document.getElementById('close-modal')



function openModal(){
	modalOpener.onclick = function () {
         overlay.classList.remove("is-hidden");
     }
}


function closeModal(){
	modalCloser.onclick = function () {

   overlay.classList.add("is-hidden");
}
}

window.onload = () =>{
	this.openModal()
	this.closeModal()
}
