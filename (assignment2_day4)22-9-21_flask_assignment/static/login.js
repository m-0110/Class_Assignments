function validateForm() {
  let x = document.forms["myForm"]["name"].value;
  if (x == "") {
    alert("Name must be filled out");
    return;
  }
  let x1 = document.getElementById("email").value
  if (x1=="")
  {
    alert("Email must be filled out");
    return;
  }
  let x2 = document.getElementById("pswd1").value
  let x3 = document.getElementById("pswd2").value
  if (x2=="" || x3=="")
  {
    alert("password is necessary");
    return;
  }

  if (x2!=x3)
  {
    alert("passwords not matched");
    return;
  }
  else
  {
    alert("user registered");
    return ;

  }




}
