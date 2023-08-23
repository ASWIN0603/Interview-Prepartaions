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


  app.get('/user', (req, res) => {
    
  
    // Perform a query to check if the username and password match
    const query = 'SELECT * FROM  users ';
    db.query(query,  (error, results) => {
      if (error) {
        throw error;
      }
  
      if (results.length > 0) {
        res.send(results);
      } else {
        res.status(401).send('no data found');
      }
    });
  });
app.post('/login', (req, res) => {
    const { username, password } = req.body;
  
    // Perform a query to check if the username and password match
    const query = `SELECT * FROM  users WHERE BINARY name = '${username}' AND BINARY password = '${password}'`;
    db.query(query, (error, results) => {
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
  

app.post ('/user', (req,res) =>{
const {username, password} = req.body;

const query = `INSERT INTO users(name,password) VALUES('${username}', '${password}')` ;
db.query(query, (error,results) =>{
  if (error) {
    throw error;
}

if (results.affectedRows === 1) {
    res.send(`${username} was added`);
}  else {
    res.status(500).send(`Error adding ${username}`);
}
});

});

  app.patch('/user', (req, res) => {
    const { username, newusername } = req.body;

    // Perform a query to update the username
    const query = `UPDATE users SET name = '${newusername}' WHERE name = '${username}'`;
    db.query(query, (error, results) => {
        if (error) {
            throw error;
        }

        if (results.affectedRows === 1) {
            res.send(`${username} was changed to ${newusername}`);
        } else if (results.affectedRows === 0) {
            res.status(404).send(`${username} not found, update was unsuccessful`);
        } else {
            res.status(500).send('Error updating username');
        }
    });

  });


  app.delete('/user', (req, res) => {
    const { username } = req.body;
  
    // Perform a query to check if the username and password match
    const query = `DELETE FROM users WHERE name ='${username}'`;
    db.query(query,  (error, results) => {
      if (error) {
        throw error;
      }
  
      if (results.affectedRows === 1) {
        res.send(`${username} deleted successfully`);
      } else {
        res.status(401).send('delete unsuccessfull');
      }
    });
  });

app.listen(port, () => {
  console.log(`Server is listening at http://localhost:${port}`);
});
