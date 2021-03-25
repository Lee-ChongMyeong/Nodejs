const express = require('express')
const mongoose = require('mongoose')
const app = express()
const Article = require('./models/article')
const methodOverride = require('method-override')

app.use(express.urlencoded({ extended : false}))

//// [method-override]
app.use(methodOverride('_method'))

//// [MongoDB]
mongoose.connect('mongodb://localhost:27017/admin', {
      useNewUrlParser: true,
      useUnifiedTopology: true,
      useCreateIndex: true,
      ignoreUndefined: true,
    // user: "test",
    // pass: "test"
})

//// [Router] 
const articleRouter = require('./routes/articles')


//// [Routes]
app.use('/articles', articleRouter)

//// [EJS]
app.set('view engine', 'ejs')


//// [Get, Main page 정보 받아옴]
app.get('/', async (req, res) => {
    const articles = await Article.find().sort({ createdAt : 'desc'})
    res.render('articles/index', { articles : articles})
})


//// [Port]
app.listen(3000)