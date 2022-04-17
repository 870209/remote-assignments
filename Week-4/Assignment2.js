function ajax(src, callback){
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var data = this.response;
            callback(data);
        }
    };
    req.open("get", src, true);
    req.responseType = 'json';
    req.send();
}
function render(data){
    var newDiv = document.createElement("div");
    newDiv.innerHTML = data;
    document.body.appendChild(newDiv);

// document.createElement() and appendChild() methods are preferred.
}
ajax("https://appworks-school.github.io/Remote-Aassigiment-Data/products",
function(response){
render(response);
});
 // you should get product information in JSON format and render data in the page