const express = require('express')
const Article = require('./../models/article')
const router = express.Router()


router.get('/new', (req, res) =>{
    res.render('articles/new', {article : new Article() })
})

//// [GET-new -> show]
router.get('/:id', async (req, res)=>{
    const article = await Article.findById(req.params.id)
    if (article == null) res.redirect('/')
    res.render('articles/show', { article : article})
})

//// [GET-edit]
router.get('/edit/:id', async (req, res) => {
    const article = await Article.findById(req.params.id)
    res.render('articles/edit', {article : article })
})

////[Delete]
router.delete('/:id', async (req, res) => {
    let article = await Article.findById(req.params.id)
    if (article.password == req.body.password){
        await Article.findByIdAndDelete(req.params.id)
        res.redirect('/')
    }else{
        window.location.reload()
    }
})


//// [Post]
router.post('/', async (req,res) => {
    let article = new Article({
        title : req.body.title,
        author : req.body.author,
        password : req.body.password,
        description : req.body.description,
    })
    try{
        article = await article.save()    //article에 새로 저장
        res.redirect(`/articles/${article.id}`)
    } catch(e){
        console.log(e)
        res.render('articles/new', {article : article})
    }
})

//// [PUT]
router.put('/:id', async (req, res) => {
    let article = await Article.findById(req.params.id)

    if (article.password == req.body.password){
        article.title = req.body.title
        article.author = req.body.author
        article.password = req.body.password
        article.description = req.body.description
    }else{
        window.location.reload()
    }
    
    try{
        article = article.save()   
        res.redirect(`/`)
    } catch(e){ 
        res.render('articles/edit', {article : article})
    }
})



/*
///[Post]
router.post('/', async (req, res, next) => {
    req.article = new Article()
    next()
  }, saveArticleAndRedirect('new'))

///[Put]
router.put('/:id', async (req, res, next) => {
    req.article = await Article.findById(req.params.id)
    next()
  }, saveArticleAndRedirect('edit'))
  
  function saveArticleAndRedirect(path) {
    return async (req, res) => {
      let article = req.article
      article.title = req.body.title
      article.author = req.body.author
      article.password = req.body.password
      article.description = req.body.description
      article.markdown = req.body.markdown
      try {
        article = await article.save()
        res.redirect(`/articles/${article.id}`)
      } catch (e) {
        res.render(`articles/${path}`, { article: article })
      }
    }
  }
*/

module.exports = router
