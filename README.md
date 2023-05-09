###VAŽNO
dodati api key u config/config.py
------------
### Pregled značajki:


- Prikaz trenutne prognoze za odabrani grad

- Prikaz trodnevne prognoze za odabrani grad

- Prikaz sedmodnevne prognoze za odabrani grad

- Grafički prikaz minimalne i maksimalne temperature za prikazane prognoze

![](https://i.ibb.co/JzF1gK1/Snimka-zaslona-2023-05-09-181308.png)

------------
### Pokretanje aplikacije
Da biste kreirali i aktivirali virtualno okruženje (venv) te instalirali pakete iz requirements.txt datoteke, morate slijediti sljedeće korake:

###### Kreirajte virtualno okruženje:
Otvorite terminal ili naredbeni redak. Navigirajte do glavnog direktorija projekta.
Pokrenite naredbu specifičnu za svoj operativni sustav:

Na Windowsu:

`python -m venv venv`

Na macOS-u i Linuxu: 

`python3 -m venv venv`

###### Aktivirajte virtualno okruženje:
Na Windowsu:
Ako se već ne nalazite u korijenskom direktoriju projekta, navigirajte do njega.
Pokrenite naredbu: 
`venv\Scripts\activate.bat`

Na macOS-u i Linuxu:
Ako se već ne nalazite u direktoriju projekta, navigirajte do njega.
Pokrenite naredbu: 

`source venv/bin/activate`

Nakon aktiviranja virtualnog okruženja, naredbe koje izvršavate će koristiti instalirane pakete 
unutar tog okruženja.

###### Instalirajte pakete iz requirements.txt datoteke:
Nakon što ste aktivirali virtualno okruženje, izvršite sljedeću naredbu:

`pip install -r requirements.txt`

Ova naredba će instalirati sve pakete navedene u requirements.txt datoteci u vaše virtualno okruženje.
