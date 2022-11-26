function getXMLHttpRequest() {
    if (window.XMLHttpRequest) {
        //code for modern browser
        return new XMLHttpRequest();
    } else {
        //code for old IE browser
        return new ActiveXObject("Microsoft.XMLHTTP");
    }
}
function showResult(){
    var xmlhttp = getXMLHttpRequest();
    //get input value
    var name = document.getElementById("name").value;
    var sunshine = document.getElementById('sunshine-hour').value;
    var work = document.getElementById('work-hour').value;
    if(name != "" && sunshine != "" && work != ""){
    //set url and inner
    var url = "/hasil";
    //alert (url);
    var inner = "prediction_result";
    //open request
    var params = "name="+ name + "&sunshine-hour=" + sunshine + "&work-hour=" + work;
    xmlhttp.open('POST' , url, true);
    xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlhttp.onreadystatechange = function(){
        document.getElementById(inner).innerHTML = '<img src="static/img/ajax_loader.png"/>';
        if ((xmlhttp.readyState == 4) && (xmlhttp.status == 200)){
            document.getElementById(inner).innerHTML = xmlhttp.responseText;
        }
        return false;
    }
    
    xmlhttp.send(params);
  }
  else{
    alert("Isi seluruh data");
  }
}