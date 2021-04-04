const express = require('express')
const app = express()
const bcrypt = require('bcrypt')
const passport = require('passport')

const initializePassport = require('./passport-config')
initializePassport(passport)

const users = []

app.use(express.urlencoded({ extended : false}))

//// [ejs]
app.set('view-engine', 'ejs')

//// [get - main]
app.get('/', (req, res) => {
    res.render('index.ejs')
})

//// [get - Login]
app.get('/login', (req, res) => {
    res.render('login.ejs')
})

//// [get - Register]
app.get('/register', (req, res) => {
    res.render('register.ejs')
})

//// [post - Register]
app.post('/register', async (req, res) => {
    try {
      const hashedPassword = await bcrypt.hash(req.body.password, 10)
      users.push({
        id: Date.now().toString(),
        name: req.body.name,
        email: req.body.email,
        password: hashedPassword
      })
      res.redirect('/login')
    } catch {
      res.redirect('/register')
    }
    console.log(users)
  })

//// [post - :ogin]
app.post('/login', (req, res) => {

})


app.listen(3000)