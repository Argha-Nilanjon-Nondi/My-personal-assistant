  
  function money_lister(row){
  
  let total=0;
  
  let tr1=document.getElementById("total");
  
  row.forEach((element)=>{
 
  let status=element[3];
  let amount=element[4];
  var str_status="";
  
  if(status=="0"){
  total+=Number(amount);
  str_status="Increase"
  }
  
  if(status=="1"){
  total-=Number(amount);
  str_status="Decrease"
  }
  
   tr1.innerHTML=`Total : ${total}  -/TK`;
    
  });
  
  }
  
  
    
  
  async function getData(url){
  
  let params={method:"post"};
  
  const domain=await fetch(url,params);
  
  let data = await domain.json();
  
  return data.data;
  
  }
  
  getData("/money/data/").then((data)=>{
  
   money_lister(data);
  
  }).catch(()=>{
  
  alert("There is a problem in your network");
  
  });