const express = require('express');
const mysql = require('mysql2')
const app = express();
const port = 3000;
app.use(express.json());

const db = mysql.createConnection(
  {
    host: 'localhost',
    user: 'root',
    password: 'aswin2002',
    database: 'sample'
  }
)
db.connect()


app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.get('/admin', (req, res) => {
    res.send('Hello, Admin!');
  });

app.post('/user', (req, res) => {
    const { username, password } = req.body;
  
    // Perform a query to check if the username and password match
    const query = 'SELECT * FROM  users WHERE BINARY name = ? AND BINARY password = ?';
    db.query(query, [username, password], (error, results) => {
      if (error) {
        throw error;
      }
  
      if (results.length === 1) {
        res.send(`Hello, ${username}! Welcome to the dashboard!`);
      } else {
        res.status(401).send('Invalid username or password');
      }
    });
  });
  

app.listen(port, () => {
  console.log(`Server is listening at http://localhost:${port}`);
});
