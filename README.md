# Python-script-2-1
Script languages 2/1. assignment

Vegyünk egy olyan programozási nyelvet, amelyben a szekvenciát "utasitas ;utasitas" szerkezet (a pontosvessző előtt lehet space, de utána nem), az elágazást "ELAGAZAS feltetel [[utasitasok ]]" szerkezet, míg a ciklust "CIKLUS feltetel [[utasitasok ]]" szerkezet jelöli (a szerkezetekben az utasítások helyes python utasítások). A feladat egy olyan program elkészítése, amely megkeresi az aktuális könyvtárban (ahol futtatjuk) a ".prog" kiterjesztésű, fenti szintaxisnak megfelelő fájlokat és minden ilyen fájlból egy ugyanolyan nevű, de ".py" kiterjesztésű fájlt készít, amely a leírásnak megfelelő helyes python programot tartalmaz. A python program "for", illetve "if" szerkezeteket használjon (a kezdő sorban a ":" előtt mindig pontosan egy space legyen) és a belső blokkokat mindig 4 db space-el beljebb kezdje. Feltehető, hogy a ciklusokon/elágazásokon belül nincs újabb ciklus/elágazás. Minta .prog fájl, illetve .py fájl.

A megoldást tartalmazó python fájl forráskódját kell feltölteni (UTF-8 kódolásnak megfelelően).

utasitas ;utasitas ;
ELAGAZAS feltetel [[utasitasok]]
CIKLUS feltetel [[utasitasok]]

ELAGAZAS feltetel [[utasitas ;utasitas ; utasitas]]
CIKLUS feltetel [[utasitas ;utasitas ; utasitas]]