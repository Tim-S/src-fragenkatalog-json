# SRC Fragenkatalog als JSON exportieren (z.B. für eine Quiz-App)

Dieses Skript nutzt 
[Camelot](https://camelot-py.readthedocs.io/en/master/index.html) um Daten aus dem SRC-Fragenkatalog von ELWIS ([Fragenkatalog-SRC-2018.pdf](https://www.elwis.de/DE/Schifffahrtsrecht/Sprechfunkzeugnisse/Fragenkatalog-SRC-2018.pdf?__blob=publicationFile&v=4))
zu lesen und in ein JSON-Format zu überführen, welche man dann z.B. für eine kleine Quiz-App verwenden könnte.

## PreRequisites
[Camelot](https://camelot-py.readthedocs.io/en/master/index.html) setzt voraus, dass Ghostscript und Tkinter installiert sind. Genaueres findet this auf der Projektseite 
[Camelot Abhänigkeiten installieren](https://camelot-py.readthedocs.io/en/master/user/install-deps.html#install-deps)

Sind die Abhängigkeiten installiert, machen wir mit der [Installation von camelot-py](https://camelot-py.readthedocs.io/en/master/user/install.html#using-pip) weiter.

```bash
pip install camelot-py[cv]
```

## Benutzung

```
python ./extract_questions_from_pdf.py --url "https://www.elwis.de/DE/Schifffahrtsrecht/Sprechfunkzeugnisse/Fragenkatalog-SRC-2018.pdf?__blob=publicationFile&v=4" 
--pdf "Fragenkatalog-SRC-2018.pdf"
--json "questions.json"
```

Oder Kurz

```
python ./extract_questions_from_pdf.py --url "https://www.elwis.de/DE/Schifffahrtsrecht/Sprechfunkzeugnisse/Fragenkatalog-SRC-2018.pdf?__blob=publicationFile&v=4"
```

Nachdem das Skript beendet ist, sollte ein entsprechenden *.json file (Standardmäßg questions.json) erzeugt worden sein