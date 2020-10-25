
   
      function pdf_viewer(url, myCanvas){
  
    pdfjsLib.getDocument(url).then(( doc )=> {
     
     doc.getPage(1).then( (page)=>{
      
      var context=myCanvas.getContext("2d");
      var viewport=page.getViewport(2);
      
      myCanvas.height=viewport.height;
       myCanvas.width=viewport.width;
       
       obj={
         canvasContext:context,
         viewport:viewport
       };
       
       page.render(obj);
     
     } );
    
    });
    
  }
    
        
function maker(data,dbid){
    
    let certificate=document.getElementById("certificate");
    
    pdf_viewer(`/static/users/${dbid}/certificate/${data[0][1]}`,certificate);
    
    }
    
   let dbid="";
    
   
  
  async function getData(url){
  
  let params={method:"post"};
  
  const domain=await fetch(url,params);
  
  let data = await domain.json();
  
  return data.data;
  
  }
  
    getData("/dbid/").then((d)=>{
  
   dbid+=d;
  
  }).catch(()=>{
  
  alert("There is a problem in your network");
  
  });   
  
  getData("/certificate/data/").then((data)=>{
  
   maker(data,dbid);
  
  }).catch(()=>{
  
  alert("There is a problem in your network");
  
  }); 
  