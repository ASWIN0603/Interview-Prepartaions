const fs = require('fs')
const http = require('http')

const server = http.createServer(function(req,res) {

  fs.appendFileSync(`log.txt`, `user logged in on ${Date.now()} \n `)

  return res.end(`This is Login Page`)

})
server.listen(8000, () =>{
    console.log('Server started in port 8000')
})


// if we use writeFile method we need to concatinate before writing into the file