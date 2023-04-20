const loginForm=document.querySelector("#login");
function setMessage(message,type){
    const messageElement=loginForm.querySelector(".form-message");

    messageElement.classList.remove("form-message-error");
    messageElement.classList.remove("form-message-success");
    messageElement.textContent=message;
    messageElement.classList.add(`form-message-${type}`);
}

function setInputError(inputElement,message){
    inputElement.classList.add("form-input-error");
    inputElement.parentElement.querySelector(".form-input-error-message").textContent=message;
}

function clearInputError(inputElement){
    inputElement.classList.remove("form-input-error");
    inputElement.parentElement.querySelector(".form-input-error-message").textContent="";
    
}

loginForm.addEventListener("submit",e=>{
    if(!(pwdcheck&&namecheck)){
        e.preventDefault();  
        
        setMessage("Fields not filled correctly! ","error"); // ${namecheck}, ${pwdcheck}, ${cpwdcheck}
    }
    else{
        loginForm.submit();

    }
    
})

let pwdcheck=false,namecheck=false;
let pwd="";

let username=loginForm.querySelector("#loginUsername").value;
let pwdElement=loginForm.querySelector("#loginPassword").value;
if(username.length>=5){
    namecheck=true;
}
if(pwdElement.length>=4){
    pwdcheck=true;
}
//form validation 
document.querySelectorAll(".form-input").forEach(inputElement=>{
    inputElement.addEventListener("input",e=>{
        if(e.target.id=="loginUsername"){
            if(e.target.value.length<5){
                setInputError(inputElement,"Username must be atleast 5 characters in length");
                namecheck=false;
            }
            else{
                namecheck=true;
                clearInputError(inputElement);
            }
        }
        if(e.target.id=="loginPassword"){
            pwdElement=inputElement;
            pwd=e.target.value;
            if(e.target.value.length<4){
                setInputError(inputElement,"Password should be atleast 4 characters in length");
                pwdcheck=false;
            }
            else{
                pwdcheck=true;
                clearInputError(inputElement);
    
            }
        }
    })
})

if(msg){            
    setMessage(msg,"error");
}

