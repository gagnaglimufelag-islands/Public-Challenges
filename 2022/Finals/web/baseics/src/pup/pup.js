const result_id = process.argv[2]
const flag = process.argv[3]

const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--no-setuid-sandbox']});
  console.log('Starting browser')
  const page = await browser.newPage();
  await page.setCookie({"name": "flag", "value": flag, "domain": "localhost"})
  console.log('Fetching website')
  await page.goto(`http://localhost:5000/results/${result_id}`, {
    waitUntil: 'networkidle2',
  });
  await page.waitForTimeout(3000);
  await browser.close();
  console.log('Done')
})();
