function footerposition(){
	document.getElementById("footer").style.top = (266 + document.getElementById("section").offsetHeight) + "px";
}
function opensidebar(){
    document.getElementById('sidebar').style.display='block';    
    document.getElementById('container').style.pointerEvents='none';
    document.getElementById('container').style.opacity=0.4;



  }
  function closesidebar(){
    document.getElementById('sidebar').style.display='none';
    document.getElementById('container').style.pointerEvents='All';
    document.getElementById('container').style.opacity=100;
  }