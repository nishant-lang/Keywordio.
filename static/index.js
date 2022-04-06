const addbookbutton=document.querySelector('#Addbookid')
const booklist=document.querySelector('#booklist')


addbookbutton.onclick = () => {
  axios
    .get("http://127.0.0.1:8000/addbook/")
    .then((res) => {
      console.log(res);
      let outputbooklist=res.data;
      console.log(booklist)
      for(let i=0;i<outputbooklist.length;i++){
        const node = document.createElement("li"); 
        const textnode = document.createTextNode(outputbooklist[i].book_name);
        console.log(outputbooklist[i])
        node.appendChild(textnode);
        booklist.appendChild(node)
     
      }
   
    })
    .catch((err) => console.log(err));
};







