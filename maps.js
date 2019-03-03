//Get number of results
//Get price
//Get address

for(int r=0; r < loc.Count; r++)
{
    var btn = document.createElement("BUTTON");
    btn.setAttribute("id", "result"+ r.toString());
    btn.setAttribute("onclick", "openMarker()");
    var price = document.createTextNode(Price);
    btn.appendChild(t);

    document.getElementById("column1").appendChild(btn);
}
function openMarker() {
    document.getElementById("demo").innerHTML = "Hello World";
  }