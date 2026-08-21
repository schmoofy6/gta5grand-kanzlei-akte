# Kanzlei-Akte

Mandanten- und Fallverwaltung für Rechtsanwälte im Rollenspiel auf **GTA5Grand** (Server #3 | DE).

Eine einzige HTML-Datei. Kein Server, kein Build, keine Abhängigkeiten, kein Konto — herunterladen, im
Browser öffnen, loslegen. Alle Daten bleiben auf dem eigenen Rechner.

---

## Was das Tool kann

**Mandanten und Fälle**
Mandantenkartei mit Reisepassnummer und Telefonnummer, Fallakten mit Fallnummer, Vorwürfen,
festnehmenden Beamten, Staatsanwalt und Behörde. Volltextsuche und Filter über alles.

**Strafmaß nach dem Regelwerk**
Der komplette Bußgeldkatalog (85 Delikte, Stand 14.04.2026) ist eingebaut. Wählt man die Vorwürfe an,
rechnet das Tool das zulässige Höchstmaß aus — nach **§ 3 VII StPO** zählt der schwerwiegendste
Einzeltatbestand, es wird *nicht* addiert. Die geforderte Strafe füllt sich automatisch, Kaution,
Ersatzfreiheitsstrafe und Entschädigung werden mitgerechnet. Liegt das tatsächlich verhängte Strafmaß
darüber, meldet das Tool den Abhandlungsfehler nach § 35 StPO. Ausschlussparagraphen und
Qualifikationsdelikte ohne Grundtat werden ebenfalls erkannt.

**Schriftstücke**
Zwölf Vorlagen, alle frei bearbeitbar, mit PDF-Export:

| | |
|---|---|
| Revisionsantrag | inklusive Feststellung, Aufhebung, Löschung und Erstattung nach § 23 V StPO |
| Antrag auf Akteneinsicht | § 36 I StPO |
| Begnadigungsgesuch | Art. 9 SVerfG |
| Antrag auf Löschung der Strafakte | § 19 IV StPO |
| Antrag auf Entschädigung | § 23 StPO |
| Antrag auf einstweilige Anordnung | § 17 StPO |
| Dienstaufsichtsbeschwerde | |
| Strafanzeige und Strafantrag | § 16 StPO |
| Antrag auf eine Familienlizenz | § 7 RAVO |
| Anmeldung eines Unternehmens | §§ 11, 12 BGB, auch als Dachgesellschaft mit Töchtern |
| Vertretungsvollmacht | § 8 BGB |
| Rechnung / Honorarnote | RAVO §§ 3, 4 |

Platzhalter wie `{mandant}`, `{reisepass}` oder `{tabelle:posten}` werden beim Erzeugen ersetzt.
Vorlagen lassen sich dauerhaft ändern, einzelne Schriftstücke zusätzlich im Wortlaut anpassen, ohne die
Vorlage anzufassen. Aktenzeichen nach dem Muster `A-RA-NN-YYYY-XX` (§ 41 II StPO) erzeugt das Tool selbst.

**Honorar nach RAVO**
Jede Leistung wird mit Datum, Art und Betrag erfasst und gegen die Höchstsätze des § 4 II RAVO geprüft.
Die Gebühren der Schriftstücke zählen automatisch zum jeweiligen Verfahren — nichts wird doppelt
eingetragen. Der Nachweis der letzten 14 Tage nach § 3 VI RAVO wird als fertiges PDF im Briefkopf der Kanzlei
ausgegeben, wahlweise als Tabelle.

**Fristen und Auswertung**
Die 72-Stunden-Frist der Revision (§ 41 I StPO) und die Verjährung nach 14 Tagen (§ 19 StPO) laufen
sichtbar mit. Die Übersicht fasst Ergebnisse und Statistik auf einer Seite zusammen: Erfolgsquote,
gesparte Hafteinheiten und Geldstrafen, die Fälle je Ausgang sowie Ranglisten der Staatsanwälte und
der festnehmenden Beamten.

**Gesetzestexte**
229 Paragraphen aus neun Gesetzbüchern im Wortlaut — StGB, StPO, BGB, WaffG, BtMG, StVO, BDG, SVerfG,
RAVO — sortiert nach Gesetzbuch und Paragraph, damit Strg + F funktioniert.

---

## Benutzen

**Am einfachsten:** [`index.html`](index.html) herunterladen und doppelklicken. Fertig.

**Als Webseite:** In den Repository-Einstellungen unter *Pages* den Branch `main` und den Ordner `/`
auswählen. Das Tool läuft dann unter `https://<benutzername>.github.io/<repository>/`.

Gespeichert wird automatisch nach jeder Änderung im `localStorage` des Browsers, zusätzlich unter einem
Sicherungsschlüssel. **Es gibt keinen Server, kein Konto und keine Anmeldung** — die Daten verlassen den
Rechner nicht. Unter **Daten** lässt sich alles als JSON sichern und wieder einspielen; das ist der Weg,
um die Akte auf ein anderes Gerät, in einen anderen Browser oder zu einem Kollegen zu bringen.

---

## Entwicklung

```
index.html        das gesamte Tool
gesetze/*.txt     die Gesetzestexte als Quelle, ein Paragraph je Zeile: §Nummer|Titel|Volltext
build-online.py   erzeugt online.html (dieselbe Datei ohne <html>/<head>/<body>) zum Einbetten
```

Kein Build-Schritt, kein Paketmanager. `index.html` bearbeiten und im Browser neu laden. Die Datei
enthält alles: Stildefinitionen, Daten und Logik, in Abschnitte gegliedert und kommentiert.

---

## Rechtliches

Dies ist ein Hilfsmittel für das Rollenspiel auf einem GTA-Server. Es ist **keine Rechtsberatung** und
hat mit dem Recht der Bundesrepublik Deutschland nichts zu tun. Die abgebildeten Gesetzbücher, der
Bußgeldkatalog und die Rechtsanwaltsverordnung stammen vom Server GTA5Grand und liegen dort im
[Forum](https://gta5grand.com/forum/forums/242/) öffentlich aus; sie sind hier zum Nachschlagen
eingebunden und gehören ihren Urhebern. Ändert der Server sein Regelwerk, gilt das Regelwerk, nicht
dieses Tool.

Der Programmcode steht unter der MIT-Lizenz, siehe [LICENSE](LICENSE).
