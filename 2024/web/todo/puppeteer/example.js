const puppeteer = require('puppeteer');

const admin_user = process.env.ADMIN_USER || 'admin@ggc.tf';
const admin_pass = process.env.ADMIN_PASSWORD || '92$uFby%%Ke!5E';
const host = process.env.PUBLIC_HOST || 'main.d2rmp2202r4l9h.amplifyapp.com';


(async () => {
  while (true) {

    console.log('Starting browser');
    const browser = await puppeteer.launch({
      //headless: false,
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


    console.log('Navigating to site');
    try {
      await page.goto(`http://${host}/?admin`, {waitUntil: 'domcontentloaded'});
      await new Promise(r => setTimeout(r, 5000));

      try {
        await page.$eval('h1', (el) => el)
        console.log('Logged in')
      } catch (e) {
        console.log('Not logged in')
        console.log('Logging in');
        await page.type('input[name="username"]', admin_user);
        console.log('Username input');
        await page.type('input[name="password"]', admin_pass);
        console.log('Password input');
        await page.click('button[fullwidth="true"]'),
        console.log('Sign in clicked')
        await new Promise(r => setTimeout(r, 5000));
      }

      while (true) {
        try {
          const payload = await page.$eval('li', (el) => el.innerHTML)
          console.log(`TODO found! Payload: ${payload}`)
          console.log('Giving it 10 seconds to execute')
          await new Promise(r => setTimeout(r, 10000));
          console.log('Deleting latest TODO')
          await page.goto(`http://${host}/?admin&delete`, {waitUntil: 'domcontentloaded'});
          await new Promise(r => setTimeout(r, 5000));
          await page.goto(`http://${host}/?admin`, {waitUntil: 'domcontentloaded'});
          await new Promise(r => setTimeout(r, 5000));
      await new Promise(r => setTimeout(r, 5000));
        } catch (e) {
          console.log('No TODO found on page. Sleeping for 60 seconds.')
          console.log('Closing browser')
          await browser.close();
          await new Promise(r => setTimeout(r, 60000));
          break
        }
      }
    } catch(err) {
      console.log('FATAL ERROR')
      console.log(err);
      await new Promise(r => setTimeout(r, 60000));
    }

  }

})();
