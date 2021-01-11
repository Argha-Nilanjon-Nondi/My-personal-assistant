  
  function money_lister(row){
  
  let table_name=row[row.length-1][2]

  let link=document.getElementById("money-latest-table")
  
  let tr1=document.getElementById("total");
  
   link.setAttribute("href",`/money/single/${row[row.length-1][1]}/`)

   tr1.innerHTML=`Last created table : ${table_name}`;
  
  }
  
  
    
  
  async function getData(url){
  
  let params={method:"post"};
  
  const domain=await fetch(url,params);
  
  let data = await domain.json();
  
  return data.data;
  
  }
  
  getData("/money/tables/data/").then((data)=>{
  
   money_lister(data);
  
  })/*.catch(()=>{
  
  alert("There is a problem in your network");
  
  });*/