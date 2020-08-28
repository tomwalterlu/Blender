Thema: 

Addon für die 3D Software Blender. In diesem Addon soll dem Nutzer die Interaktion mit der 3-dimensionalen Version des „Perlin Noise“ einfach gemacht werden. Der Nutzer hat die Freiheit, auf einer quadratischen Fläche, deren Detail und Größe er wählt, sogenannte „Perlin-Berge“ zu erzeugen. Der Nutzer wählt die Größe der Berge und zeichnet einen Bereich auf die Fläche, auf dem die Berge erzeugt werden. Mit der Größe der Berge ist hier eine Skalierung gemeint. Die Berge werden ihren anfänglichen Proportionen gerecht vergrößert.

Bedienung des Programms:

C:\Program Files\Blender Foundation\Blender\2.80\scripts\addons
Im addons Verzeichnis den Ordner mit __init__.py und anderen Dateien einfügen.
Danach in Blender Edit -> Preferences -> Add-ons -> Perlin Berge (suchen) -> mit Haken freischalten. Fertig.
Voraussetzung:
Der Nutzer befindet sich im 3D Viewport von Blender (Version >=2.80) mit Objekt Sicht, dies sollte die Standard Sicht in Blender sein, wenn ein neues Projekt erstellt wird. Ansonsten unter ‚File‘ oder ‚Datei‘ den Editor Type und den Modus entsprechend zu 3D Viewport und Objekt Mode wechseln.
Das Addon ist in Form eines Panels (bpy.types.Panel), wird also sichtbar im rechten Rand vom 3D Viewport, sobald man die Taste ‚n‘ drückt. 
Es ist empfehlenswert, alles was sich im Viewport befindet, vorerst zu löschen. Sofern man sich im Objekt Modus befindet geschieht dies über die Tastenkombination „A + X“ und dann ENTER. Danach hat man eine freie Sicht. Alternativ kann man auch „A + H“ benutzen, um temporär andere Objekte zu verstecken.
Ist n gedrückt, so sollte neben Item, Tool und View „Perlin Berge“ erscheinen. Um es zu öffnen: Einmal mit linker Maustaste auf „Perlin Berge“  klicken.
Nun sollte ein aufklappbarer Dialog erscheinen mit Titel „Perlin Berge“. Klappt man diesen auf, erscheinen 4 Optionen in Form von Buttons.
Diese sollen in der angezeigten Reihenfolge betätigt werden.
Wählt man „Fläche erzeugen“, wird ein Pop Up Dialog angezeigt. Hier kann man die Startfläche konfigurieren. Der einzugebende Text stellt den Namen des neu erzeugten Flächenobjektes dar, also nicht das Mesh sondern das gesamte Objekt in dem sich das Mesh befindet.
Zusätzlich kann man die Flächenhöhe und Flächenweite der Fläche bestimmen (in Meter), und die Anzahl der Zellen in beide Richtungen wählen. Diese Zahl gibt an wie oft die Fläche, über die X- und die Y-Achsen geteilt wird. Somit entsteht ein Gittermuster auf der Fläche. Drückt man OK ist die Konfiguration abgeschlossen und die Fläche erscheint zentriert im Viewport.
Warnung: Es werden später keine Berge entstehen, falls die Flächenhöhe/weite restlos durch die Zellenanzahl teilbar ist und der Skalierungsfaktor gerade oder kleiner 2 gewählt ist. Dies ist kein Fehler in der Implementierung, sondern die Perlin Funktion liefert auf ganzzahlige X und Y Werte immer den Wert 0.
Nun kann der Nutzer die erzeugte Fläche auswählen (Linksklick auf Objekt, Ränder sollen orange farbig sein). Dann kann der Nutzer „Gebirgeareal zeichnen“ wählen. Das selektierte Objekt wird anschließend in den „Weight Paint Modus“ wechseln. Jetzt kann der Nutzer den Bereich auf die Fläche zeichnen, wo die Berge später erscheinen werden. Mit der Taste F und Bewegung der Maus nach innen oder außen kann man die Breite der Zeichnung wählen und mit einem Linksklick abschließen. Grüne, blaue, gelbe oder rote Farbtöne werden in dieser Anwendung gleichbehandelt.
Hat man nun den gewünschten Bereich ausgewählt, kann man „Hügel anpassen und erzeugen“ auswählen, um die Größe der Berge auszuwählen, und den Prozess abschließen. Abhängig davon wie detailliert das Terrain ist, und vor allem, wie groß der selektierte Bereich ist, kann der Prozess einige Millisekunden bis mehrere Sekunden dauern.
Bei höherem Detail werden die abgeschnittenen Ränder sichtbar. Bei dieser Problematik empfiehlt sich der Gebrauch der Smooth-Funktion im Sculpt Mode um die Ränder zu glätten, sollte man dieses Addon für die Erzeugung von Landschaften benutzen.
