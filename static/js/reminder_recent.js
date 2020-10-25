function remind_make(data){
    
    let reminder=document.getElementById("reminder");
    
 reminder.innerText=data[0][0];
   
    
    }   
    
    
async function getData(url){
  
  let params={method:"post"};
  
  const domain=await fetch(url,params);
  
  let data = await domain.json();
  
  return data.data;
  
  }
  
  getData("/reminder/data/").then((data)=>{
  
  remind_make(data);
  
  }).catch(()=>{
  
 
  });
  