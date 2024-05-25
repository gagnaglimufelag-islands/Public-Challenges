import express, { Express, Request, Response} from "express";
import session from 'express-session';
import dotenv from "dotenv";
import { randomBytes } from 'crypto';
import { readFileSync } from "fs";
import router from "./routes/api.route";
import path from "path";
import fs from 'fs'


dotenv.config();

const app: Express = express();
const port = process.env.PORT || 3000;

app.use("/api/v1",router)
app.set('view engine', 'ejs');


const storage_file = path.join(__dirname, 'storage.json');
const data = fs.readFileSync(storage_file, 'utf-8');
const vhs_storage = JSON.parse(data);

app.get('/', (req, res) => {
  res.render('index', { vhs_storage:{...vhs_storage} });
});

app.listen(port, () => {
  console.log(`[server]: Server is running at http://localhost:${port}`);
});
