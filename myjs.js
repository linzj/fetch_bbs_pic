(function () {
    var ctx = { count: 0 };
    function getrequest() {
        if (this.readyState >=2) {
            if (this.status != 200) {
                console.error('cancled href: ' + this._href + '; status code: ' + this.status);
                return;
            }
        } 
        if (this.readyState != 4) {
            return;
        }
        console.log('download ' + this._href + ' okay.');
        var href = 'http://127.0.0.1:8787/';
        var lastSlash = this._href.lastIndexOf("/");
        if (lastSlash == -1) {
            href += "" + (ctx.count++);
        } else {
            href += this._href.substring(lastSlash + 1);
        }
        console.log('posting href: ' + href);
        var request = new XMLHttpRequest();
        request.open('post', href);
        request.responseType = 'text';
        request._href = href;
        request.send(this.response);
        request.onreadystatechange = postreq;
    };
    function postreq() {
        if (this.readyState >=2) {
            if (this.status != 200) {
                console.error('cancled href: ' + this._href + '; status code: ' + this.status);
                return;
            }
        } 
        if (this.readyState != 4) {
            return;
        }
        console.log('post ' + this._href + ' okay.');
    };
    var node = document.querySelector('p>img');
    if (node != null) {
        var request = new XMLHttpRequest();
        console.log('send one request: ', node.src);
        request.open('get', node.src);
        request.responseType = 'blob';
        request._href = node.src;
        request.onreadystatechange = getrequest;
        request.send();
    }
})()
