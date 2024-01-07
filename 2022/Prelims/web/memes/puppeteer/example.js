const puppeteer = require('puppeteer');

const admin_pass = process.env.ADMIN_PASSWORD || 'asdf';
const host = process.env.PUBLIC_HOST || 'localhost:5000';

// Referesh session every N loops
const REFRESH_SESSION = 20;

(async () => {
    const browser = await puppeteer.launch({
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();

    page.on('dialog', async dialog => {
        console.info(`DIALOG: ${dialog.message()}`);
        await dialog.dismiss();
    });

    page.on('pageerror', msg => {
        console.info(`PAGE ERROR: ${msg}`);
    });

    page.on('error', msg => {
        console.info(`ERROR: ${msg}`);
    });

    page.on('console', msg => {
        for (let i = 0; i < msg.args().length; ++i)
            console.info(`${i}: ${msg.args()[i]}`);
    });

    let ctr = 0;

    while (true) {
        console.log('Navigating to site');
        try {
            // Make sure we are logged out!
            if (ctr == 0) {
                console.info('Logging out');
                await page.goto(`http://${host}/logout`, {waitUntil: 'domcontentloaded'});
                console.log('Logging in');
                await page.goto(`http://${host}/login`, {waitUntil: 'domcontentloaded'});
                await page.type('#username', 'admin');
                await page.type('#password', admin_pass);
                await Promise.all([
                    page.click('input[type=submit]'),
                    page.waitForNavigation({'waitUntil': 'networkidle0'}),
                ]);
            } else {
                console.info('Loading front page');
                await page.goto(`http://${host}`, {waitUntil: 'domcontentloaded'});
            }

            ctr = (ctr + 1) % REFRESH_SESSION;

            try {
                await page.$eval('a[class=meme-url]', (el) =>
                    console.log('Meme link found', el.href)
                )
            } catch (e) {
                console.log('Ticket page is empty, nothing to do');
                await new Promise(r => setTimeout(r, 60000));
                continue;
            }

            // click meme link
            console.log('Clicking link')
            try {
                await Promise.all([
                    page.click('a[class=meme-url]'),
                    page.waitForNavigation({'timeout': 5000}),
                ]);
            } catch (e) {
                console.error(e)
            }
            console.log('Visiting URL: ', page.url())
            await new Promise(r => setTimeout(r, 5000));
        } catch(err) {
            console.error(err);
            await new Promise(r => setTimeout(r, 60000));
        }
    }

    await browser.close();
})();
