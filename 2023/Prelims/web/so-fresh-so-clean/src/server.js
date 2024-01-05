const express = require('express');
const path = require('node:path');
const bodyParser = require('body-parser');
const { readFile } = require('fs/promises');
const parseString = require('xml2js').parseString;

const app = express()
const port = 5000

app.use(express.static('static'))
app.use(bodyParser.text({ type: 'text/xml' }))

function invalidItem(item) {
    return JSON.stringify(item).includes('flag');
}

app.get('/', (req, res) => {
    res.sendFile('index.html', { root: path.join(__dirname, 'templates')});
})

app.get('/cart', async (req, res) => {
    let cartTemplate = await readFile('templates/cart.html', 'utf8');
    let html = cartTemplate.replaceAll('{{ item }}', 'Your cart is empty');
    res.setHeader('Content-Type', 'text/html');
    res.send(html);
})

app.post('/cart', async (req, res) => {
    let html = null;
    let cartTemplate = await readFile('templates/cart.html', 'utf8');
    try {
        parseString(req.body, function (err, cart) {
            if (invalidItem(cart)) {
                res.statusCode = 400;
                return res.send('Invalid item!');
            }
            if (cart.item.includes('flag')) {
                html = cartTemplate.replaceAll('{{ item }}', process.env.FLAG || 'gg{not_a_flag}');
            } else {
                html = cartTemplate.replaceAll('{{ item }}', cart.item)
            }
            res.setHeader('Content-Type', 'text/html');
            res.send(html);
        });
    } catch(e) {
        res.statusCode = 500;
        return res.send(e.message);
    }
})  

app.listen(port, () => {
    console.log(`listening on port ${port}`);
})
