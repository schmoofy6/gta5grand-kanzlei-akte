# Erzeugt aus der lokalen index.html die Online-Fassung fuer die claude.ai-Seite.
# Unterschied: Die Online-Seite bringt ihr HTML-Geruest selbst mit, deshalb fliegen
# DOCTYPE, <html>, <head> und <body> raus - Inhalt und Funktion bleiben identisch.
# Aufruf:  python build-online.py
import io, re, os

HIER = os.path.dirname(os.path.abspath(__file__))
QUELLE = os.path.join(HIER, "index.html")
ZIEL   = os.path.join(HIER, "online.html")

s = io.open(QUELLE, encoding="utf-8").read()

kopf_ende = s.index("</head>")
kopf = s[:kopf_ende]
rest = s[kopf_ende + len("</head>"):]

titel = re.search(r"<title>(.*?)</title>", kopf, re.S)
stile = re.findall(r"<style>.*?</style>", kopf, re.S)

rest = re.sub(r"^\s*<body[^>]*>", "", rest.strip(), flags=re.I)
rest = re.sub(r"</body>\s*</html>\s*$", "", rest.strip(), flags=re.I)

teile = []
if titel:
    teile.append("<title>%s</title>" % titel.group(1))
teile.extend(stile)
teile.append(rest.strip())

io.open(ZIEL, "w", encoding="utf-8").write("\n".join(teile) + "\n")
print("online.html geschrieben:", len(open(ZIEL, encoding="utf-8").read()), "Zeichen")
