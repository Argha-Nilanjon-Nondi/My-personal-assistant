     let other_msg=document.getElementById("chat-users");
    
    function creatShowcage(data){
       let html_code=``;
       data.forEach((ele)=>{
          let msg=ele[1];
          let mark=ele[2];
          let css1=``;
          let css2=``;
          
          if(mark=="U"){
             css1+=`class="d-flex align-items-end flex-column" `;
             css2+=`style="width:18rem;border:4px solid green;"`
          }
          
          if(mark=="O"){
              css1+=`class="d-flex flex-column"`;
             css2+=`style="width:18rem;border:4px solid orange;"`
          }          
          
          html_code+=`
<div ${css1}>
<div class="p-2">
     <div class="card" ${css2} >
        <div class="card-body">
          <p class="card-text">${msg}</p>
        </div>
      </div>
  </div>
</div>                  
          
          `;
            
          
       });
   other_msg.innerHTML=html_code;    
       
    }

  
  async function getData(url){
  
  let params={method:"post"};
  
  const domain=await fetch(url,params);
  
  let data = await domain.json();
  
  return data.data;
  
  }
      
   let owner_dbid="";
   
   let full_url;
   
   let enter_url;
   
    getData("/dbid/").then((data)=>{
    
    /*making the url start*/
  
   owner_dbid+=data;
     let other_dbid=other_msg.getAttribute("dbid");
  
     full_url=`/chat_me/talk/${owner_dbid}/${other_dbid}/`;
     
     enter_url=`/chat_me/enter/${owner_dbid}/${other_dbid}/`;
     
     /*making the url end*/
     
     /*creat the msg box start*/
  
  setInterval(()=>{
  getData(full_url).then((data)=>{
  
      /*alert(data);*/
      
      creatShowcage(data);
  
  }).catch((e)=>{
  
  alert(e);
  
  });
  
   } ,3000);
  
  /*creat the msg box end*/
  
  }).catch((e)=>{
  
  alert(e);
  
  });   


    /*form of msg enter start*/
       let msg=document.getElementById("about");
       
       document.getElementById("action-send").addEventListener("click",(e)=>{
       
        e.preventDefault();
        
       en_u2=enter_url+msg.value+`/`;

  getData(en_u2).then((data)=>{
 
  
  }).catch((e)=>{
  
  alert(e);
  
  });
       
       });
        /*form of msg enter end*/