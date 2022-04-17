#!/usr/bin/env python3
import cgi
import os
import arrow
import sys
import codecs
from random import randint
from pathlib import Path

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
form = cgi.FieldStorage()
url = form.getfirst("url", "")
r1 = randint(0, 10)
r2 = randint(0, 10)
r3 = randint(0, 10)
r4 = randint(0, 10)
r5 = randint(0, 10)
r6 = randint(0, 10)
r7 = randint(0, 10)
r8 = randint(0, 10)

short_url = f"{r1}{r2}{r3}{r4}{r5}{r6}{r7}{r8}.html"

link_file = open(short_url, "w")
link_file.write(f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Сервис ИдиНа</title>
    <meta http-equiv="refresh" content="1;URL={url}" />
</head>
<body>
    <center><h1>ИдиНа</h1></center><br>
    <center><a href="{url}">Если не сработала переадресация, нажмите сюда</a></center>
</body>
</html>
""")
link_file.close()
os.replace('/usr/share/nginx/html' + short_url, '/usr/share/nginx/html/l' + short_url)

filesPath = r"/usr/share/nginx/html/l"
criticalTime = arrow.now().shift(hours=+1).shift(days=-1)
for item in Path(filesPath).glob('*'):
    if item.is_file():
        f = str(item.absolute())
        itemTime = arrow.get(item.stat().st_mtime)
        if itemTime < criticalTime:
            os.remove(f)

print("Content-type: text/html\n")
print("""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Сервис ИдиНа</title>
    <style>
        body {
    background: url('https://github.com/ars-lang/idina/raw/main/background39.png');
     }
.floating-button {
  text-decoration: none;
  display: inline-block;
  width: 140px;
  height: 45px;
  line-height: 45px;
  border-radius: 45px;
  margin: 10px 20px;
  font-family: 'Montserrat', sans-serif;
  font-size: 11px;
  text-transform: uppercase;
  text-align: center;
  letter-spacing: 3px;
  font-weight: 600;
  color: #524f4e;
  background: white;
  box-shadow: 0 8px 15px rgba(0, 0, 0, .1);
  transition: .3s;
}
.floating-button:hover {
  background: #2EE59D;
  box-shadow: 0 15px 20px rgba(46, 229, 157, .4);
  color: white;
  transform: translateY(-7px);
}    
    </style>
</head>
<body>
    <center><form action="http://идина.рф/cgi-bin/link.py">
        <h1>ИдиНа</h1>
        <br>
        <label for="url">Введите ссылку: </label><br>
        <br>
        <input type="url" name="url" id="url"
            placeholder="https://example.com"
            pattern="https://.*" size="30"
            required><br>
        <br>
        <hr>
        <br>
        <button type="submit" class="floating-button">Сократить!</button><br>
        <br>
        <hr>
    </form></center>
    <br>
""")
print(f"""
    <center><p>Ваша ссылка: идина.рф/l/{short_url}</p></center><br>
</body>
</html>
""")
