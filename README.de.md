[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![de](https://img.shields.io/badge/lang-de-green.svg)](README.de.md)
[![ru](https://img.shields.io/badge/lang-ru-yellow.svg)](README.ru.md)

# CYCLE - Ein Kalender für Frauen

**DD.MM.YYYY Version 0.3.3**  
2002-2005 (c) Oleg Gints (altgo@users.sourceforge.net)  
2002-2005 (c) "CONERO lab", http://conero.lrn.ru  
2022 (c) Konstantin L. Metlov (metlov@donfti.ru , metlov@fti.dn.ua)  

### PROGRAMMFEATURES

*   Berechnung der Menstruationstage basierend auf der Länge des Zyklus oder der letzten Perioden
*   Berechnung der Tage des "sicheren" Sex, erhöhter Fruchtbarkeit und Eisprungs
*   Voraussage des Tages der Empfängnis eines Kindes
*   Notizfunktion
*   Hilft bei der Einnahme von hormonellen Empfängnispillen

### WIE ES FUNKTIONIERT

Das Programm verwendet die _Kalendermethode_ für die Berechnung der fruchtbaren Tage. Dafür ist es notwendig, die Dauer von mindestens sechs vergangenen Perioden zu kennen. Für die Berechnung wird folgender Algorithmus verwendet:

*   Erster Tag: Dauer des kürzesten Zyklus minus 18
*   Letzter Tag: Dauer des längsten Zyklus minus 11
*   Eisprung: Wird in der Mitte der fruchtbaren Tage vermutet (Mit der Kalendermethode ist die exakte Berechnung nicht möglich)

Mehr Informationen über die Kalendermethode sind unter [http://www.mama.ru/gynecolog/STA/st18.htm](http://www.mama.ru/gynecolog/STA/st18.htm) (in russisch) verfügbar.

Der Tag der Empfängnis (Geburt) eines Kindes wird vom Beginn der letzten Menstruation gezählt. Dieses Datum wird mit der Dauer eines Zyklus korrigiert (Es wird die Anzahl der Tage addiert/subtrahiert, die die Zyklusdauer von 28 Tagen abweicht). Es ist möglich, das Ergebnis unter folgender Adresse zu überprüfen: [http://cir.msk.ru/sroki.shtml](http://cir.msk.ru/sroki.shtml) (in russisch)

### PROGRAMMNUTZUNG

Es ist notwendig, den Beginn der letzten Menstruationen per Hand zu markieren. Dies geschieht durch einen Klick mit der rechten Maustaste auf einen Tag im Kalender und der Auswahl von "Zyklusbeginn". Auf dieselbe Art kann die Markierung entfernt werden. Mit Hilfe der Dauer der letzten sechs Zyklen wird das Programm folgendes berechnen:

*   Fruchtbare Tage - grüne Zellen
*   Eisprung (Mitte der fruchtbaren Tage) - hellgrüne Zelle
*   Beginn der nächsten Menstruation - pinke Zelle

Die Zyklusdauer kann in den Einstellungen festgelegt werden oder über den Durchschnitt der Dauer der letzten 6 Zyklen berechnet werden.

Um den voraussichtlichen Tag der Geburt des Kindes zu berechnen ist es nötig, den ersten Tag des letzten Zyklus zusätzlich als "Schwanger" zu markieren.

Abhängig von Ihren Absichten können sowohl Tage des "sicheren" Sex als auch nur fruchtbare Tage angezeigt werden. Informationen über interessante Tage können mit einem Linksklick auf den entsprechenden Tag aufgerufen werden.

Es ist möglich, Notizen zu einem Tag hinzuzufügen. Tage mit Notiz werden unterstrichen dargestellt.

_Hinweis:_ Die Fehlerrate der Kalendermethod liegt bei ca. 10 Prozent. Sie ist nur für Frauen mit einer regelmäßigen Periode zu empfehlen.

Wenn Ihnen Ihr Arzt die Pille verschrieben hat, wird Ihnen das Programm bei der Einhaltung der regelmäßigen Einnahme helfen. Machen Sie sich aber trotzdem mit den Hinweisen auf der Packungsbeilage vertraut! Eine Packung kann 21 Tabletten (Der Zyklus dauert 21 Tage, danach 7 Tage Pause) oder 28 Tabletten enthalten - diese werden dann jeden Tag eingenommen. Im Programm wird nur der Tag markiert, an dem die erste Tablette eingenommen werden muss.

### VERTEILUNGSBESTIMMUNGEN

Das Programm "Cycle" wird unter der **GNU General Public License** verteilt in der Hoffnung, dass es nützlich sein wird. Es gibt aber keine Garantie, dass es korrekt oder überhaupt funktioniert. (Siehe Datei "COPYRIGHT")

Übersetzung: Christian Weiske (cweiske@users.sourceforge.net)
