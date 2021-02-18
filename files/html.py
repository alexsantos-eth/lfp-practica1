import webbrowser
import os


def generate_html(content):
    html = '<!DOCTYPE html><html lang="es"> <head> <meta charset="UTF-8"/> <meta name="viewport" content="width=device-width, initial-scale=1.0"/> <link rel="preconnect" href="https://fonts.gstatic.com"/> <link href="https://fonts.googleapis.com/css2?family=Cabin&display=swap" rel="stylesheet"/> <title>Practica 01</title> <style>@keyframes entry {from {opacity: 0;  transform: scale(0.8);}to {opacity: 1;transform: scale(1);}}*{margin: 0; padding: 0; box-sizing: border-box; font-family: "Cabin", sans-serif;}body{background: #f5f5f5; display: flex; align-items: center; justify-content: center; padding: 30px; height: 100vh;}#container{background-color: #ffffff; width: 100%; max-width: 620px; border-radius: 10px; overflow: hidden; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.3);opacity:0;transform:scale(0.8);animation: entry 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) 1 0.5s normal forwards;}a{color: #fff; font-weight: bold;}#header{padding: 40px; background: #2196f3; color: #fff;}#card{background: #555; padding: 40px;}#card > p{font-family: monospace; font-size: 1.2em; color: #fff; font-weight: bold;}</style> </head> <body> <div id="container"> <div id="header"> <h1>Resultados de archivos</h1> <p id="description"></p></div><div id="card"> <p>' + \
        content + \
        '</p></div></div><script>const p=document.getElementById("description"); p.innerHTML=`Estos son los datos generados el ${new Date().toLocaleDateString( "en-GB" )} a las ${new Date().toLocaleTimeString( "en-US" )} por los archivos .lfp en la aplicación. ver app en <a target="_blank" href="https://github.com/alexsan-dev/lfp-practica1">https://github.com/alexsan-dev/lfp-practica1</a>`; </script> </body></html>'
    file = open('./index.html', "w")
    file.write(html.replace('\n', '<br/>'))
    file.close()
    webbrowser.open('file://' + os.path.realpath('./index.html'))
