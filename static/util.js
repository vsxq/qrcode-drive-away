var error_msg = document.createElement("div")
error_msg.className="weui-toptips weui-toptips_warn js_tooltips"
document.querySelector("body").appendChild(error_msg)
function show_info(c,text){

    document.querySelector(".js_tooltips").innerText=text
     document.querySelector(".js_tooltips").style.display='block';
         c.value=""
         c.focus()
         setTimeout(function () {
             document.querySelector(".js_tooltips").style.display='none';

     }, 2000);
     try {
        document.querySelector(".table_show").style.display="none"
     } catch (error) {
         
     }
     
     
 }