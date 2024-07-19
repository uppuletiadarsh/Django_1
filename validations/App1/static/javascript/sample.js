function validateForm() {
  let x = document.forms["myForm"]["uname"].value;
  let y= document.forms["myForm"]["psw"].value;
  if (x == "venkat")&&(y =="Sathya"){
    alert("Login Sucesss");
    return p.innerHTML='"Login Sucesss"'
  }
  else{
    alert("Login failed");

  }
}






}
