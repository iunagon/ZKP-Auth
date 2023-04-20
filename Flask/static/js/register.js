const registerForm=document.querySelector("#register");

function setMessage(message,type){
    const messageElement=registerForm.querySelector(".form-message");

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


registerForm.addEventListener("submit",e=>{
    if(!(pwdcheck&&cpwdcheck&&namecheck)){
        e.preventDefault();  
        setMessage("Fields not filled correctly! ","error"); // ${namecheck}, ${pwdcheck}, ${cpwdcheck}
    }
    else{
        setTimeout(()=>{
            registerForm.submit();
        },3000);

    }
    
})

let pwdcheck=false,cpwdcheck=false,namecheck=false;
let pwd="",cpwd="";
let username=registerForm.querySelector("#signupUsername").value;
let pwdElement=registerForm.querySelector("#signupPassword").value;
let cpwdElement=registerForm.querySelector("#confirmPassword").value;
if(username.length>=5){
    namecheck=true;
}
if(pwdElement.length>=4){
    pwdcheck=true;
    if(pwdElement==cpwdElement){
        cpwdcheck=true;
    }
}


//form validation 
document.querySelectorAll(".form-input").forEach(inputElement=>{
    inputElement.addEventListener("input",e=>{
        if(e.target.id=="signupUsername"){
            if(e.target.value.length<5){
                setInputError(inputElement,"Username must be atleast 5 characters in length");
                namecheck=false;
            }
            else{
                namecheck=true;
                clearInputError(inputElement);
            }
        }
        if(e.target.id=="signupPassword"){
            pwdElement=inputElement;
            pwd=e.target.value;
            if(e.target.value.length<4){
                setInputError(inputElement,"Password should be atleast 4 characters in length");
                setInputError(cpwdElement,"Passwords not matching");
                cpwdcheck=false;
                pwdcheck=false;
            }
            else{
                pwdcheck=true;
                clearInputError(inputElement);
                if(pwd==cpwd){
                    cpwdcheck=true;
                    clearInputError(cpwdElement)
                }
            }
        }
        if(e.target.id=="confirmPassword"){
            cpwdElement=inputElement;
            cpwd=e.target.value;
            if(e.target.value!==pwd){
                setInputError(inputElement,"Passwords not matching");
                cpwdcheck=false;
            }
            else{
                cpwdcheck=true;
                clearInputError(inputElement);
            }
        }
    })
})

if(valid!=0){
    if(valid==1){
        setMessage(msg,"success");
    }
    else{
        setMessage(msg,"error");
    }
}