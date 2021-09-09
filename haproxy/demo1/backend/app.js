var http = require('http');

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    var url = req.url;
    console.log(url);
    if (url === '/secret') {
        console.log("hit secret")
        res.end("secret\n");
    } else {
        res.end("public\n");
    }
}).listen(8000, function () {
    console.log("server start at port 8000");
});