const http = require('http')


const server = http.createServer(function(req,res) {

switch(req.url){

    case '/' :   res.end('this is home page')
    break;
 
    case '/about' : res.end('this is about page')
    break;
}

})

server.listen(8000,() => {
    console.log('server started')
})