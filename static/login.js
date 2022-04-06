const inputusername=document.querySelector('#inputname')
const inputpassword=document.querySelector('#inputPassword')
const loginbutton=document.querySelector('#loginbutton')

loginbutton.onclick = () => {
    const data={
      username:inputusername.value,
      password:inputpassword.value
    }
    axios
      .post("http://127.0.0.1:8000/api/loginapi/",data)
      .then((res) => {
        console.log(res);
        console.log(data)
      })
      .catch((err) => {
        console.log(err);
        console.log(data)
      })
    }