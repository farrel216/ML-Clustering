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
    var sleeping = document.getElementById('sleeping-hours').value;
    var heart = document.getElementById('avg-hr').value;
    //set url and inner
    var url = "/hasil";
    //alert (url);
    var inner = "prediction_result";
    //open request
    var params = "name="+ name + "&sleeping-hours=" + sleeping + "&avg-hr=" + heart;
    xmlhttp.open('POST' , url, true);
    xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlhttp.onreadystatechange = function(){
        if ((xmlhttp.readyState == 4) && (xmlhttp.status == 200)){
            document.getElementById(inner).innerHTML = xmlhttp.responseText;
        }
        return false;
    }
    xmlhttp.send(params);
  }