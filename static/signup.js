const inputusername=document.querySelector('#inputname')
const inputpassword=document.querySelector('#inputPassword')
const inputEmail=document.querySelector('#inputEmail')
const loginbutton=document.querySelector('#loginbutton')

loginbutton.onclick = () => {
    const data={
      name:inputusername.value,
      email:inputEmail.value,
      password:inputpassword.value
    }
    axios
      .post("http://127.0.0.1:8000/api/signupapi/",data)
      .then((res) => {
        console.log(res);
        console.log(data)
      })
      .catch((err) => {
        console.log(err);
        console.log(data)
      })
    }