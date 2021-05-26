const showcase = document.querySelector('.showcase');

menuToggle.addEventListener('click', () => {
   showcase.classList.toggle('active');
})

function verifyPassword() {
   let uname = document.getElementById("username").value;
   let pw = document.getElementById("password").value;
   //check empty password field
   
   if (uname == "") {
      return false;
   }
   
   if (uname.length < 4) {
      return false;
   }
   
   if (uname.length > 14) {
      return false;
   }
   
   if(pw == "") {
      return false;
   }
   
   //minimum password length validation
   if(pw.length < 6) {
      return false;
   }
   
   //maximum length of password validation
   if(pw.length > 63) {
      return false;
   }
}
