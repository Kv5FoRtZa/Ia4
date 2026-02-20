# Ia4
	Proiect Informatica Aplicata 4
		Bahaciu Raisa-Georgiana, Morus Alexandru, Zamfir Irina-Maria
	
	Scurta descriere:
		Aplicatia este un joc, unde jucatorul trebuie sa navigheze pe niste harti si sa omoare niste inamici.
	El contine 4 nivele si un nivel final unde se va lupta cu un BOSS.Pentru a face acestea, jucatorul poate
	sa mearga in cele 4 puncte cardinale si sa impuste, in timp ce inamicii trag inapoi. Jocul are ca scop
	eliminarea tuturor inamicilor, si se progreseaza la urmatorul nivel atunci cand sunt toti eliminati.
	La nivelul final, boss-ul trebuie eliminat impreuna cu inamicii normali.

	Link github:
		https://github.com/Kv5FoRtZa/Ia4
	Limbaje folosite/tehnologii folosite:
		Python/Pygame
	Instructiuni rulare:
		Pentru rulare se intra in folderul App si se ruleaza main.py.
		Odata pornita aplicatia, se da click pe butoanele care apar.
	Ce a contribuit fiecare:
		Bahaciu Raisa-Georgiana:
			Am configurat fereastra de joc, sistemul de cadre pe secundă (FPS) și variabilele globale necesare pentru funcționarea motorului grafic.
			Am implementat o logică de încărcare a „sprite sheets” care permite personajului să aibă animații diferite pentru starea de repaus (idle) și alergare (run).
			Am creat un sistem de tiles pentru fundal și obiecte fizice precum blocuri (ziduri) și capcane (tepi).
			Am integrat bare de viață dinamice pentru jucător  care se actualizează în timp real. Am creat level3.
			Am programat mișcarea personajului pe axele X și Y, incluzând schimbarea direcției sprite-ului prin funcția flip.
			Am creat funcția principală draw care gestionează ordinea straturilor: fundalul, obiectele hărții, și jucătorul.
			Am scris funcții pentru încărcarea automată a imaginilor din directoare specifice (assets), asigurând scalarea și transparența acestora (convert_alpha).
			Am implementat coliziuni bazate pe măști (pygame.mask) pentru a detecta exact momentul în care jucătorul atinge zidurile sau capcanele.
			Am facut ecranul de play si butonul de Click to Play.
		Morus Alexandru:
			Am implementat totul legat de inamici(miscarea lor, modul in care trag)
			Am implementat gloantele jucatorului / ale inamicilor, si interactiunea intre acestea si tintele lovite(folosind la player sistemul de hp)
			Am implementat boss-ul si tot ce tine de acesta(din nou mers, tras, dar si divizunea gloantelor/ trasul catre directia jucatorului)
			Am ajutat la crearea hartilor(hartile 1, 4 si 5 sunt facute de mine)
			Am intregrat elementele create de mine in functia de draw.
			Am creat un mod de a disipa gloantele si de a elimina inamicii de pe harta odata ce au fost invinsi.
			Am facut un sistem de coliziune separat pentru inamici, pentru a asigura ca acestia nu se lovesc de ziduri.
			Am ajutat la crearea textului ajutator de pe primele pagini.
		Zamfir Irina-Maria:
			Am scris clasele: gameMapClass, levelClass;
			Am facut fisierele: level_menu, gameLogicFunc (unde am scris si mutat metodele necesare logicii jocului – am scris : create_levels(), winning_message(), losing_message(), unlock_next_level() ).
			Am organizat fisierele sub forma unei ierarhii profesionale, pentru a face mai usoara citirea codului si colaborarea intre membrii echipei.
			Am modificat draw() din backgroundFunc (pentru a include toate elementele prezente in gameMapClass).
			Am modificat main: am scris logica care permite jucarea a mai multe nivele. Am adaugat elemente vizuale la ecranul principal (in functia main_menu()) si am mutat logica de joc a unui nivelului (functia play_game()).
			Am facut harta 2.
	Dificultati intampinate:
		Gloantele se stergeau cand loveau un perete sau un inamic, si daca inamicul era fix langa perete rar se stergea de 2 ori si dadea crash.
		Coliziunile cu peretele(inamicii nu aveau loc sa treaca in anumite locuri, si ramaneau bloati + jucatorul se putea bloca in perete)
		Sincronizarea mișcării cu pereții: A fost necesară separarea verificării coliziunilor pe axa X și axa Y pentru a permite jucătorului să se miște fluid pe lângă obstacole fără să rămână blocat.
		Controlul animației: Reglarea vitezei de schimbare a cadrelor folosind animation_count și ANIMATION_DELAY pentru a preveni o animație prea rapidă sau prea lentă.
		Manipularea sprite-urilor: Gestionarea automată a denumirilor de fișiere pentru a crea dicționare de animații orientate spre stânga și spre dreapta, trecera din imagine in sprite pentru a crea o animatie
		Am avut dificultati in integrarea elementelor de frontend (in special in implementarea meniului nivelului), intrucat expertiza mea se concentreaza pe zona de backend. Am reusit sa inving acest obstacol studiind documentatia Pygame privind gestionarea evenimentelor. 
		Am intampinat dificultati in legarea meniurilor intre ele, insa am reusit sa rezolv prin implementarea unor apeluri recursive controlate.
