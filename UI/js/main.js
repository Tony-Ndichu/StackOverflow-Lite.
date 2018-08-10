
//THIS THE MENU JS CODE

let theMenuButton = document.getElementById('menu');

let theCloseButton = document.getElementById('closer');


function showMenu() {
	theMenuButton.onclick = function () {
	toggleMenuBody()
	toggleCloseButton()

	
}
}

function hideMenu() {
	theCloseButton.onclick = function () {
	toggleMenuBody()
	toggleCloseButton()
	

}
}

function toggleMenuBody(){ 

	var menuid = document.getElementById("bodyMenu")

if ( menuid.classList.contains('not-visible') ){

menuid.classList.remove('not-visible');
menuid.classList.add('visible');
 
}else{
	menuid.classList.remove('visible');
menuid.classList.add('not-visible');
}
}


function toggleMenuButton(){
	
	var menu_button = document.getElementById("menu")

if ( menu_button.classList.contains('show') ){

menu_button.classList.remove('show');
menu_button.classList.add('hide');
 
}else{
	menu_button.classList.remove('hide');
	menu_button.classList.add('show');
}
}


function toggleCloseButton(){
	
	var close_button = document.getElementById("closer")

if ( close_button.classList.contains('show') ){

close_button.classList.remove('show');
close_button.classList.add('hide');
 
}else{
	close_button.classList.remove('hide');
	close_button.classList.add('show');
}
}

//THIS IS THE MODAL JS CODE


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

//TO ENSURE THESE JS FILES ONLY RUN WHEN DOM ELEMENTS HAVE LOADED

window.onload = () =>{
	this.showMenu()
	this.hideMenu()
	this.openModal()
	this.closeModal()
}