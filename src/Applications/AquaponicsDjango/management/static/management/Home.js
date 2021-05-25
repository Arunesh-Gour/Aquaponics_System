const showcase = document.querySelector('.showcase');

menuToggle.addEventListener('click', () => {
  showcase.classList.toggle('active');
})

function verifyPassword() {  
  var pw = document.getElementById("password").value;  
  //check empty password field  
  if(pw == "") {  
     document.getElementById("message").innerHTML = "**Fill the password please!";  
     return false;  
  }  
   
  if(pw == "12345"){
    return true;
  }

 //minimum password length validation  
  if(pw.length < 4) {  
     document.getElementById("message").innerHTML = "**Password length must be atleast 4 characters";  
     return false;  
  }  
  
//maximum length of password validation  
  if(pw.length > 15) {  
     document.getElementById("message").innerHTML = "**Password length must not exceed 15 characters";  
     return false;  
  }
}  