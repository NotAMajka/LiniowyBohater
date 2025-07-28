import os, ctypes, sys
import random
import time

hp = 15
mana = 30
shield = 10
gold = 1000
moj_damage = 5
moj_magiczny_dmg = 0
obecna_lokacja = "lonka"
wrog = None
wybor = None
### wrogowie
przeciwnik_huj = None
pusty_pokoj = False
obecny_item = "brak"
ile_lochow_przeszedles = 0
poziom_trudnosci = 0
moj_magiczny_dmg = 0

dodatek_dmg_kowal = 0
dodatek_shield_kowal = 0
dodatek_mag_dmg_kowal = 0

os.system('cls')

itemy = {
	"kijek               ": {"nr": "1", "dmg": 2, "shield": 1, "magiczne_obrazenia": 1, "cena_buy": 12},
	"akumulator_na_kablu ": {"nr": "2", "dmg": 100, "shield": 10, "magiczne_obrazenia": 1, "cena_buy": 1000},
	"mala_tarca          ": {"nr": "3", "dmg": 1, "shield": 2, "magiczne_obrazenia": 1, "cena_buy": 20},
	"duza_tarca          ": {"nr": "4", "dmg": 2, "shield": 4, "magiczne_obrazenia": 2, "cena_buy": 2},
	"bardzo_duza_tarcza  ": {"nr": "5", "dmg": 3, "shield": 6, "magiczne_obrazenia": 3, "cena_buy": 50},
	"maly_napiersnik     ": {"nr": "6", "dmg": 0, "shield": 4, "magiczne_obrazenia": 2, "cena_buy": 29},
	"sredni_napiersnik   ": {"nr": "7", "dmg": 0, "shield": 6, "magiczne_obrazenia": 3, "cena_buy": 37},
	"duzy_napiersnik     ": {"nr": "8", "dmg": 0, "shield": 9, "magiczne_obrazenia": 4, "cena_buy": 47},
	"maly_miecz          ": {"nr": "9", "dmg": 2, "shield": 1, "magiczne_obrazenia": 1, "cena_buy": 15},
	"sredni_miecz       ": {"nr": "10", "dmg": 4, "shield": 2, "magiczne_obrazenia": 2, "cena_buy": 24},
	"duzy_miecz         ": {"nr": "11", "dmg": 7, "shield": 3, "magiczne_obrazenia": 4, "cena_buy": 47},
	"rozdzka            ": {"nr": "12", "dmg": 0, "shield": 1,"magiczne_obrazenia": 4, "cena_buy": 20},
	"kostur             ": {"nr": "13", "dmg": 1, "shield": 1,"magiczne_obrazenia": 8, "cena_buy": 30},
	"czarny kostur      ": {"nr": "14", "dmg": 1, "shield": 3,"magiczne_obrazenia": 12, "cena_buy": 42},
	"cipek              ": {"nr": "15", "dmg": 999, "shield": 999, "magiczne_obrazenia": 1, "cena_buy": 1},
	"brak               ": {"nr": "16", "dmg": 0, "shield": 0, "magiczne_obrazenia": 1, "cena_buy": 0}
}

def przeciwnik(hp, dmg):
	global przeciwnik_huj
	przeciwnik_huj = {"hp_przeciwnik": hp, "obrazenia_przeciwnik": dmg}

def wyswietl_wybory(lokalizacja1, lokalizacja2, lokalizacja3, lokalizacja4):
   print("")
   print(f"1. {lokalizacja1}")
   print(f"2. {lokalizacja2}")
   print(f"3. {lokalizacja3}")
   print(f"4. {lokalizacja4}")
   nazwa = 0
   nazwa = input("wybierz opcje (1,2,3,4): ")
   return nazwa



def wyswietl_staty():
		global hp, mana, shield, moj_damage, gold, obecna_lokacja, poziom_trudnosci
		ctypes.windll.kernel32.SetConsoleTitleW(f"|  hp {round(hp)}  |  mana: {round(mana)}  |  shield: {round(shield)} (+{round(dodatek_shield_kowal)})  |  damage: {round(moj_damage)} (+{round(dodatek_dmg_kowal)})  |  mag_damage: {round(moj_magiczny_dmg)} (+{round(dodatek_mag_dmg_kowal)})  |  gold: {round(gold)}  |  lokalizacja: {obecna_lokacja}  |  item: {obecny_item}  |  trudnosc: {round(poziom_trudnosci)}")

def wygeneruj_wroga():
	global wrog
	rodzaj_wroga = random.randint(1, 6)
	if rodzaj_wroga == 1:
			wrog = "szkielet"
	elif rodzaj_wroga == 2:
	    	wrog = "andrzej"
	elif rodzaj_wroga == 3:
	    	wrog = "antek"
	elif rodzaj_wroga == 4:
			wrog == "kurvinox"
	elif rodzaj_wroga == 5:
			wrog = "ognisko"
	elif rodzaj_wroga == 6:
			wrog = "skrzynia"
	if rodzaj_wroga == 5:
		print('pokoj jest pusty')
	elif rodzaj_wroga == 6:
		print("w pokoju jest skrzynia")
	elif rodzaj_wroga == 1 or rodzaj_wroga == 2 or rodzaj_wroga == 3 or rodzaj_wroga == 4:
		print(f"twoj wrog to {wrog}")
		print('on zaczyna')

def lootowanie():
	global gold, obecny_item, shield, hp, moj_damage, itemy, obecny_item
	numerek = random.randint(1, 100)

	if numerek == 1:
		ile_golda_kill = random.randint(18, 22)
		gold = gold + ile_golda_kill
		print(f"dostajesz {ile_golda_kill} golda fartowna kurwo (1%)")
		wyswietl_staty()
		time.sleep(5)

	elif numerek == 2 or numerek == 3:
		ile_golda_kill = random.randint(12, 15)
		gold = gold + ile_golda_kill
		print(f"dostajesz {ile_golda_kill} golda, ladnie (2%)")
		wyswietl_staty()
		time.sleep(5)

	elif numerek == 4 or numerek == 5 or numerek == 6 or numerek == 7 or numerek == 8:
		ile_golda_kill = random.randint(5, 7)
		gold = gold + ile_golda_kill
		print(f"dostajesz {ile_golda_kill} golda! (5%)")
		wyswietl_staty()
		time.sleep(4)

	elif numerek == 9 or numerek == 10 or numerek == 11 or numerek == 12 or numerek == 13:
		if obecny_item == "brak":
			print("masz farta kurwo ze nie masz nic przy sobie (5%)")
			time.sleep(4)
		else:
			shield = shield - itemy[obecny_item]['shield']
			moj_damage = moj_damage - itemy[obecny_item]['dmg']
			print('rozpierdalasz swoj item, lipa (5%)')
			obecny_item = "brak"
			wyswietl_staty()
			time.sleep(4)

	elif numerek == 14 or numerek == 15 or numerek == 16 or numerek == 17 or numerek == 18 or numerek == 19 or numerek == 20 or numerek == 21 or numerek == 22 or numerek == 23:
			ile_damage_kill = random.randint(1, 3)
			print("nakluwasz sie na fiuta potwora (10%)")
			print(f"dostajesz {ile_damage_kill} damage")
			hp = hp - ile_damage_kill
			wyswietl_staty()
			time.sleep(4)

	elif numerek > 23:
		ile_golda_kill = random.randint(1, 4)
		gold = gold + ile_golda_kill
		print(f"dostajesz {ile_golda_kill} golda! (77%)")
		wyswietl_staty()
		time.sleep(2)

def pokoj(wygeneruj_wroga, przeciwnik):
	      global hp, moj_damage, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal
	      nowe_dmg_przeciwnika = 0
	      while True:
	       if dlugosc_lochow >= 0:
	        os.system('cls')
	        wygeneruj_wroga()
	        print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
	        obecna_lokacja = "lochy"
	        wyswietl_staty()
	        if wrog == "szkielet":
	        	if poziom_trudnosci == 0:
	        		przeciwnik(random.randint(8, 12), random.randint(8, 15))
	        	elif poziom_trudnosci == 1:
	        		przeciwnik(random.randint(10, 16), random.randint(10, 17))
	        	elif poziom_trudnosci == 2:
	        		przeciwnik(random.randint(12, 18), random.randint(12, 19))
	        	elif poziom_trudnosci == 3:
	        		przeciwnik(random.randint(14, 20), random.randint(14, 21))
	        	elif poziom_trudnosci == 4:
	        		przeciwnik(random.randint(16, 22), random.randint(16, 23))

	        elif wrog == "antek":
	        	if poziom_trudnosci == 0:
	        		przeciwnik(random.randint(4, 6), random.randint(10, 16))
	        	elif poziom_trudnosci == 1:
	        		przeciwnik(random.randint(6, 8), random.randint(12, 19))
	        	elif poziom_trudnosci == 2:
	        		przeciwnik(random.randint(8, 10), random.randint(14, 21))
	        	elif poziom_trudnosci == 3:
	        		przeciwnik(random.randint(10, 12), random.randint(16, 23))
	        	elif poziom_trudnosci == 4:
	        		przeciwnik(random.randint(12, 14), random.randint(18, 25))

	        elif wrog == "andrzej":
	        	if poziom_trudnosci == 0:
	        		przeciwnik(random.randint(11, 15), random.randint(6, 8))
	        	elif poziom_trudnosci == 1:
	        		przeciwnik(random.randint(13, 17), random.randint(8, 10))
	        	elif poziom_trudnosci == 2:
	        		przeciwnik(random.randint(15, 19), random.randint(10, 12))
	        	elif poziom_trudnosci == 3:
	        		przeciwnik(random.randint(17, 21), random.randint(12, 14))
	        	elif poziom_trudnosci == 4:
	        		przeciwnik(random.randint(19, 23), random.randint(14, 16))

	        elif wrog == "kurvinox":
	        	if poziom_trudnosci == 0:
	        		przeciwnik(random.randint(5, 11), random.randint(6, 12))
	        	elif poziom_trudnosci == 1:
	        		przeciwnik(random.randint(8, 14), random.randint(9, 16))
	        	elif poziom_trudnosci == 2:
	        		przeciwnik(random.randint(11, 17), random.randint(12, 19))
	        	elif poziom_trudnosci == 3:
	        		przeciwnik(random.randint(14, 20), random.randint(15, 22))
	        	elif poziom_trudnosci == 4:
	        		przeciwnik(random.randint(17, 23), random.randint(18, 25))

	        elif wrog == "ognisko":
	        	  przeciwnik(0, 0)
	        	  odpoczynek = False
	        elif wrog == "skrzynia":
	        	przeciwnik(0,0)
	        	skrzynia_otworzona = False
	        while True: # pętla
	        	if wrog == "szkielet" or wrog == "andrzej" or wrog == "antek":
	        		wybor_walka = wyswietl_wybory("walka wrecz", 'magia', "obrona", "brak")
	        		if wybor_walka == "1":
	        			print("")
	        			nowe_dmg_przeciwnika = przeciwnik_huj['obrazenia_przeciwnik'] - shield
	        			if nowe_dmg_przeciwnika <= 0:
	        				nowe_dmg_przeciwnika = 0
	        			hp = hp - nowe_dmg_przeciwnika
	        			if hp <= 0:
	        				print("umarles, lamus lol")
	        				time.sleep(4)
	        				sys.exit()
	        			print(f"dostales wpierdol o {przeciwnik_huj['obrazenia_przeciwnik']} hp, zostalo ci {hp}")
	        			wyswietl_staty()
	        			przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - moj_damage - dodatek_dmg_kowal
	        			print(f"lamusowi zostalo {przeciwnik_huj['hp_przeciwnik']}")
	        			time.sleep(2)
	        			os.system('cls')
	        			print(f"twoj wrog to {wrog}")
	        			print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
	        			if przeciwnik_huj['hp_przeciwnik'] <= 0:
	        				obecna_lokacja = "martwy przeciwnik"
	        				wyswietl_staty()
	        				wyswietl_wybory("lootuj", 'idz dalej', "brak", "brak")
	        				if wybor == "1":
	        					lootowanie()
	        					dlugosc_lochow = dlugosc_lochow - 1
	        					break
	        				if wybor == "2":
	        					dlugosc_lochow = dlugosc_lochow - 1
	        					break
	        				else:
	        					print("pojebalo cie?")
	        		if wybor_walka == "2":
	        			os.system('cls')
	        			wybor_magia = wyswietl_wybory("kula ognia", 'hazard', "leczenie + obrona", "medytacja")
	        			if wybor_magia == "1":
	        				nowe_dmg_przeciwnika = przeciwnik_huj['obrazenia_przeciwnik'] - shield
	        				if nowe_dmg_przeciwnika <= 0:
	        					nowe_dmg_przeciwnika = 0
	        				hp = hp - nowe_dmg_przeciwnika
	        				if hp <= 0:
	        					print("umarles, lamus lol")
	        					time.sleep(4)
	        					sys.exit()
	        				print(f"dostales wpierdol o {przeciwnik_huj['obrazenia_przeciwnik']} hp, zostalo ci {hp}")
	        				time.sleep(2)
	        				wyswietl_staty()
	        				mana = mana - 15
	        				if mana <= 0:
	        					hp = hp + mana
	        					if hp <= 0:
	        						print("umarles, lamus lol")
	        						time.sleep(4)
	        						sys.exit()
	        					print("nie masz many pało niemyta lol")
	        					przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - 7.5 - dodatek_mag_dmg_kowal - moj_magiczny_dmg
	        					print(f"lamusowi zostalo {round(przeciwnik_huj['hp_przeciwnik'])}")
	        					mana = 0
	        					wyswietl_staty()
	        					time.sleep(2)
	        					os.system("cls")
	        					print(f"twoj wrog to {wrog}")
	        					print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
	        				else:
	        					przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - 7.5 - dodatek_mag_dmg_kowal - moj_magiczny_dmg
	        					print(f"lamusowi zostalo {przeciwnik_huj['hp_przeciwnik']}")
	        					wyswietl_staty()
	        				if przeciwnik_huj['hp_przeciwnik'] <= 0:
	        					obecna_lokacja = "martwy przeciwnik"
	        					wyswietl_staty()
	        					wyswietl_wybory("lootuj", 'idz dalej', "brak", "brak")
	        					if wybor == "1":
	        						dlugosc_lochow = dlugosc_lochow - 1
	        						lootowanie()
	        						break
	        					if wybor == "2":
	        						dlugosc_lochow = dlugosc_lochow - 1
	        						break
	        					else:
	        						print("pojebalo cie?")
	        			elif wybor_magia == "2":
	        				print("")
	        				mana = mana - 20
	        				damage_automatu = random.randint(5, 12)
	        				print(f"twoj damage to {damage_automatu}!!")
	        				nowe_dmg_przeciwnika = przeciwnik_huj['obrazenia_przeciwnik'] - shield
	        				if nowe_dmg_przeciwnika <= 0:
	        					nowe_dmg_przeciwnika = 0
	        				hp = hp - nowe_dmg_przeciwnika
	        				print(f"dostales wpierdol o -{przeciwnik_huj['obrazenia_przeciwnik']}, zostaje ci {hp} hp")
	        				if hp <= 0:
	        					print("umarles, lamus lol")
	        					time.sleep(4)
	        					sys.exit()
	        				wyswietl_staty()
	        				if mana <= 0:
	        					hp = hp + mana
	        					wyswietl_staty()
	        					print(f"nie masz many, dostajesz {mana} hp!")
	        					if hp <= 0:
	        						print("umarles, lamus lol")
	        						time.sleep(4)
	        						sys.exit()
	        					przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - damage_automatu - dodatek_mag_dmg_kowal - moj_magiczny_dmg
	        					print(f"lamusowi zostalo {przeciwnik_huj['hp_przeciwnik']}")
	        					mana = 0
	        					wyswietl_staty()
	        					time.sleep(2)
	        				else:
	        					przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - damage_automatu - dodatek_mag_dmg_kowal - moj_magiczny_dmg
	        					print(f"lamusowi zostalo {przeciwnik_huj['hp_przeciwnik']}")
	        					wyswietl_staty()
	        					time.sleep(2)
	        				os.system('cls')
	        				print(f"twoj wrog to {wrog}")
	        				print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
	        				if przeciwnik_huj['hp_przeciwnik'] <= 0:
	        					obecna_lokacja = "martwy przeciwnik"
	        					wyswietl_staty()
	        					wyswietl_wybory("lootuj", 'idz dalej', "brak", "brak")
	        					if wybor == "1":
	        						dlugosc_lochow = dlugosc_lochow - 1
	        						lootowanie()
	        						break
	        					if wybor == "2":
	        						dlugosc_lochow = dlugosc_lochow - 1
	        						break
	        					else:
	        						print("pojebalo cie?")
	        			elif wybor_magia == "3":
	        				if mana >= 10:
	        					mana = mana - 10
	        					hp = hp + 3
	        					os.system('cls')
	        					print(f"twoj wrog to {wrog}")
	        					print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
	        					wyswietl_staty()
	        					print("dostajesz 3 hp za 10 many i blokujesz obrazenia!")
	        					time.sleep(3)
	        				else:
	        					print("nie masz tyle many lamusie")
	        			elif wybor_magia == "4":
	        				nowe_dmg_przeciwnika = przeciwnik_huj['obrazenia_przeciwnik'] - shield
	        				if nowe_dmg_przeciwnika <= 0:
	        					nowe_dmg_przeciwnika = 0
	        				hp = hp - nowe_dmg_przeciwnika
	        				if hp <= 0:
	        					print("umarles, lamus lol")
	        					time.sleep(4)
	        					sys.exit()
	        				print(f"dostales wpierdol o {przeciwnik_huj['obrazenia_przeciwnik']} hp, zostalo ci {hp}")
	        				print("")
	        				dodawanie_many = random.randint(8, 12)
	        				print(f"medytujesz i dostajesz {dodawanie_many} many!")
	        				mana = mana + dodawanie_many
	        				wyswietl_staty()
	        				time.sleep(3)
	        				os.system('cls')
	        				print(f"twoj wrog to {wrog}")
	        				print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
	        		if wybor_walka == "3":
	        			print("")
	        			obrona_przeciwnik_dmg = przeciwnik_huj['obrazenia_przeciwnik'] * 0.8
	        			nowe_dmg_przeciwnika = obrona_przeciwnik_dmg - shield
	        			if nowe_dmg_przeciwnika <= 0:
	        				nowe_dmg_przeciwnika = 0
	        			hp = hp - nowe_dmg_przeciwnika
	        			print(f"dostales wpierdol o {nowe_dmg_przeciwnika} hp, zostalo ci {hp}")
	        			wyswietl_staty()
	        			if hp <= 0:
	        				print("umarles, lamus lol")
	        				time.sleep(4)
	        				sys.exit()
	        			moj_damage_obrona = moj_damage / 2
	        			przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - moj_damage_obrona - dodatek_dmg_kowal
	        			print(f"lamusowi zostalo {przeciwnik_huj['hp_przeciwnik']}")
	        			time.sleep(2)
	        			os.system('cls')
	        			print(f"twoj wrog to {wrog}")
	        			print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
	        			if przeciwnik_huj['hp_przeciwnik'] <= 0:
	        				obecna_lokacja = "martwy przeciwnik"
	        				wyswietl_staty()
	        				wyswietl_wybory("lootuj", 'idz dalej', "brak", "brak")
	        				if wybor == "1":
	        					dlugosc_lochow = dlugosc_lochow - 1
	        					lootowanie()
	        					break
	        				if wybor == "2":
	        					dlugosc_lochow = dlugosc_lochow - 1
	        					break
	        				else:
	        					print("pojebalo cie?")
	        	elif wrog == "ognisko":
	        		wyswietl_wybory("odpocznij", 'idz dalej', "brak", "brak")
	        		if wybor == "1":
	        			if odpoczynek == False:
	        				odpoczynek = True
	        				ilosc_hp = random.randint(2, 4)
	        				ilosc_many = random.randint(2, 4)
	        				hp = hp + ilosc_hp
	        				mana = mana + ilosc_many
	        				print("odpoczywasz..")
	        				time.sleep(2)
	        				wyswietl_staty()
	        				print(f"odzystkujesz {ilosc_hp} hp i {ilosc_many} many!")
	        				time.sleep(2)
	        			else:
	        				print("juz odpoczales, idz dalej lamusie")
	        		elif wybor == "2":
	        			dlugosc_lochow = dlugosc_lochow - 1
	        			break
	        	elif wrog == "skrzynia":
	        		wyswietl_wybory("otworz", 'idz dalej', "brak", "brak")
	        		if wybor == "1":
	        		 if skrzynia_otworzona == False:
	        		 	skrzynia_otworzona = True
	        		 	real_czy_fake = random.randint(1,2)
	        		 	print('otwierasz skrzynie...')
	        		 	time.sleep(1)
	        		 	if real_czy_fake == 1:
	        		 		ile_gold_skrzynia = random.randint(3, 8)
	        		 		print(f"znajdujesz {ile_gold_skrzynia} golda!")
	        		 		gold = gold + ile_gold_skrzynia
	        		 		wyswietl_staty()
	        		 		time.sleep(2)
	        		 	elif real_czy_fake == 2:
	        		 		ile_hp_skrzynia = random.randint(1,4)
	        		 		print(f"skrzynia to jednak wrog i dostajesz strzala na morde o {ile_hp_skrzynia} hp!")
	        		 		hp = hp - ile_hp_skrzynia
	        		 		wyswietl_staty()
	        		 		time.sleep(2)
	        		 else:
	        		 	print("juz otworzyles skrzynie, idz dalej lamusie")
	        		elif wybor == "2":
	        			dlugosc_lochow = dlugosc_lochow - 1
	        			break
	       else:
	        	print("skonczyles lochy")
	        	print("wiesniacy i ten skurwysyn z mlotem zorganizowali uczte na twoja czesc!!")
	        	time.sleep(3)
	        	ile_lochow_przeszedles = ile_lochow_przeszedles + 1
	        	hp = hp + 3
	        	mana = mana + random.randint(2, 4)
	        	wyswietl_staty()
	        	break


# POCZATEK
while True:
  os.system('cls')
  obecna_lokacja = "lonka"
  wyswietl_staty()
  print("u wiedzmy dodajesz staty do postaci (nie stracisz ich)")
  print("u kowala dodajesz staty do broni (mozesz je stracic)")
  print("jesli chcesz sie cofnac w jakims wyborze, kliknij enter bez wpisywania liczby")
  wybor_lonka = wyswietl_wybory("lochy (wejscie 5 golda)", 'sklep', "wiedzma", "kowal")
  if wybor_lonka == "1" or wybor_lonka == "2" or wybor_lonka == "3" or wybor_lonka == "4":
  	if wybor_lonka == "1":
  	  if obecna_lokacja == "lonka":
  	  	obecna_lokacja = "lochy"
  	  	if ile_lochow_przeszedles >= 2:
  	  		poziom_trudnosci = 1
  	  	elif ile_lochow_przeszedles >= 4:
  	  		poziom_trudnosci = 2
  	  	elif ile_lochow_przeszedles >= 7:
  	  		poziom_trudnosci = 3
  	  	elif ile_lochow_przeszedles >= 10:
  	  		poziom_trudnosci = 4
  	  	gold = gold - 5
  	  	os.system('cls')
  	  	wyswietl_staty()
  	  	wybor_lochy = wyswietl_wybory("idz przed siebie", 'zawroc', "brak", "brak")
  	  	losowanie_dlugosc_lochow = random.randint(6, 8)

  	  	dlugosc_lochow = losowanie_dlugosc_lochow + (poziom_trudnosci * 2)
  	  	if wybor_lochy == "1":
  	  		os.system('cls')
  	  		obecna_lokacja = "walka"
  	  		wyswietl_staty()
  	  		pokoj(wygeneruj_wroga, przeciwnik)
  	  	if wybor_lochy == "2":
  	  	  if obecna_lokacja == "lochy":
  	  	  	print("spierdalasz i tracisz golda lol")
  	if wybor_lonka == "2":
  	  	if obecna_lokacja == "lonka":
  	  		obecna_lokacja = "sklep"
  	  		wyswietl_staty()
  	  		numer_itemu = 0
  	  		print("")
  	  		for item in itemy:
  	  			print(f"{itemy[item]['nr']}. {item}  |  {itemy[item]['dmg']} DMG  |  {itemy[item]['shield']} SHIELD  |  {itemy[item]['magiczne_obrazenia']}  MAG_DMG  |  {itemy[item]['cena_buy']} GOLDA  |")
  	  		wybrany_item = input("wybierz item (numer): ")
  	  		for item in itemy:
  	  			for staty in itemy[item]:
  	  				if staty == "nr":
  	  					if itemy[item]['nr'] == wybrany_item:
  	  						print(f"wybrales {item}!")
  	  						tak_nie_kupno = input(f"czy chcesz go kupic za {itemy[item]['cena_buy']}? Zostanie ci {gold - itemy[item]['cena_buy']} (t/n): ")
  	  						if tak_nie_kupno == "t":
  	  							if gold >= itemy[item]['cena_buy']:
  	  								dodatek_dmg_kowal = 0
  	  								dodatek_shield_kowal = 0
  	  								dodatek_mag_dmg_kowal = 0
  	  								if obecny_item == "brak":
  	  									obecny_item = item
  	  									gold = gold - itemy[item]['cena_buy']
  	  									shield = shield + itemy[item]['shield']
  	  									moj_damage = moj_damage + itemy[item]['dmg']
  	  									wyswietl_staty()
  	  									print(f"dodano {itemy[item]['shield']} SH i {itemy[item]['dmg']} DMG")
  	  									print("")
  	  									input("kliknij cokolwiek aby kontynuowac")
  	  								else:
  	  									shield = shield - itemy[obecny_item]['shield']
  	  									moj_damage = moj_damage - itemy[obecny_item]['dmg']

  	  									obecny_item = item

  	  									gold = gold - itemy[item]['cena_buy']
  	  									shield = shield + itemy[item]['shield']
  	  									moj_damage = moj_damage + itemy[item]['dmg']
  	  							else:
  	  								print("idz zarob kutasie krzywy")
  	  								print("")
  	  								input("kliknij cokolwiek aby kontynuowac")
  	  						elif tak_nie_kupno == "n":
  	  							print("zdecyduj sie maly kurwiu")
  	  							print("")
  	  							input("kliknij cokolwiek aby kontynuowac")
  	if wybor_lonka == "3":
  	  if obecna_lokacja == "lonka":
  	  	os.system('cls')
  	  	obecna_lokacja = "wiedzma"
  	  	print("")
  	  	print(f"dodanie 1 dmg kosztuje {5 + round(float(poziom_trudnosci))} golda")
  	  	print(f"dodanie 1 shielda kosztuje {6 + round(float(poziom_trudnosci))} golda")
  	  	print(f"dodanie 1 many kosztuje {2 + round(float(poziom_trudnosci))} golda")
  	  	print(f"dodanie 1 hp kosztuje {4 + round(float(poziom_trudnosci))} golda ")
  	  	print("")
  	  	wyswietl_wybory("wiekszy dmg", "wiekszy shield", "dodanie many", "dodanie hp")
  	  	if wybor == "1":
  	  		kup_dmg_ilosc = input("Ile chcesz dodatkowego dmg?: ")
  	  		mnoznik = 5 + float(poziom_trudnosci)
  	  		cena_dmg_kup = abs(float(kup_dmg_ilosc)) * mnoznik
  	  		tak_czy_nie_dmg = input(f"czy chcesz kupic {abs(round(float(kup_dmg_ilosc)))} dmg za {abs(round(float(cena_dmg_kup)))} golda? (t/n): ")
  	  		if gold >= cena_dmg_kup:
  	  			if tak_czy_nie_dmg == "t":
  	  				gold = abs(round(gold)) - abs(round(cena_dmg_kup))
  	  				moj_damage = abs(round(float(moj_damage))) + abs(round(float(kup_dmg_ilosc)))
  	  				wyswietl_staty()
  	  				print(f"masz teraz {moj_damage} dmg")
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  			elif tak_czy_nie_dmg == "n":
  	  				print('namyśl sie kurwa')
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  		else:
  	  			print("nie stac cie palo niemyta")
  	  			print("")
  	  			input("kliknij cokolwiek aby kontynuowac")
  	  	if wybor == "2":
  	  		kup_shield_ilosc = input("Ile chcesz dodatkowego shielda?: ")
  	  		mnoznik = 6 + float(poziom_trudnosci)
  	  		cena_shield_kup = abs(float(kup_shield_ilosc)) * mnoznik
  	  		tak_czy_nie_shield = input(f"czy chcesz kupic {abs(round(float(kup_shield_ilosc)))} shield za {abs(round(float(cena_shield_kup)))} golda? (t/n): ")
  	  		if gold >= cena_shield_kup:
  	  			if tak_czy_nie_shield == "t":
  	  				gold = abs(round(gold)) - abs(round(cena_shield_kup))
  	  				shield = abs(round(float(shield))) + abs(round(float(kup_shield_ilosc)))
  	  				wyswietl_staty()
  	  				print(f"masz teraz {shield} shielda")
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  			elif tak_czy_nie_shield == "n":
  	  				print('namyśl sie kurwa')
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  		else:
  	  			print("nie stac cie palo niemyta")
  	  			print("")
  	  			input("kliknij cokolwiek aby kontynuowac")
  	  	if wybor == "3":
  	  		kup_mana_ilosc = input("Ile chcesz dodatkowej many?: ")
  	  		mnoznik = 2 + float(poziom_trudnosci)
  	  		cena_mana_kup = abs(float(kup_mana_ilosc)) * mnoznik
  	  		tak_czy_nie_mana = input(f"czy chcesz kupic {abs(round(float(kup_mana_ilosc)))} many za {abs(round(float(cena_mana_kup)))} golda? (t/n): ")
  	  		if gold >= cena_mana_kup:
  	  			if tak_czy_nie_mana == "t":
  	  				gold = abs(round(gold)) - abs(round(cena_mana_kup))
  	  				mana = abs(round(float(mana))) + abs(round(float(kup_mana_ilosc)))
  	  				wyswietl_staty()
  	  				print(f"masz teraz {mana} many")
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  			elif tak_czy_nie_mana == "n":
  	  				print('namyśl sie kurwa')
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  		else:
  	  			print("nie stac cie palo niemyta")
  	  			print("")
  	  			input("kliknij cokolwiek aby kontynuowac")
  	  	if wybor == "4":
  	  		kup_hp_ilosc = input("Ile chcesz dodatkowego hp?: ")
  	  		mnoznik = 4 + float(poziom_trudnosci)
  	  		cena_hp_kup = abs(float(kup_hp_ilosc)) * mnoznik
  	  		tak_czy_nie_hp = input(f"czy chcesz kupic {abs(round(float(kup_hp_ilosc)))} hp za {abs(round(float(cena_hp_kup)))} golda? (t/n): ")
  	  		if gold >= cena_hp_kup:
  	  			if tak_czy_nie_hp == "t":
  	  				gold = abs(round(gold)) - abs(round(cena_hp_kup))
  	  				hp = abs(round(float(hp))) + abs(round(float(kup_hp_ilosc)))
  	  				wyswietl_staty()
  	  				print(f"masz teraz {hp} hp")
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  			elif tak_czy_nie_hp == "n":
  	  				print('namyśl sie kurwa')
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  		else:
  	  			print("nie stac cie palo niemyta")
  	  			print("")
  	  			input("kliknij cokolwiek aby kontynuowac")
  	if wybor_lonka == "4":
  	  if obecna_lokacja == "lonka":
  	  	os.system('cls')
  	  	obecna_lokacja = "skurwysyn z mlotem"
  	  	print("")
  	  	print(f"dodanie 1 dmg kosztuje {3 + round(float(poziom_trudnosci))} golda")
  	  	print(f"dodanie 1 shielda kosztuje {4 + round(float(poziom_trudnosci))} golda")
  	  	print(f"dodanie 1 magicznego dmg kosztuje {3 + round(float(poziom_trudnosci))} golda")
  	  	print("")
  	  	wyswietl_wybory("wiekszy dmg", "wiekszy shield", "wiekszy magiczny dmg", "wyjscie")
  	  	if wybor == "1":
  	  		kup_dmg_ilosc = input("Ile chcesz dodatkowego dmg?: ")
  	  		mnoznik = 3 + float(poziom_trudnosci)
  	  		cena_dmg_kup = abs(float(kup_dmg_ilosc)) * mnoznik
  	  		tak_czy_nie_dmg = input(f"czy chcesz dodac {abs(round(float(kup_dmg_ilosc)))} dmg do broni za {abs(round(float(cena_dmg_kup)))} golda? (t/n): ")
  	  		if gold >= cena_dmg_kup:
  	  			if tak_czy_nie_dmg == "t":
  	  				gold = abs(round(gold)) - abs(round(cena_dmg_kup))
  	  				dodatek_dmg_kowal = abs(round(float(dodatek_dmg_kowal))) + abs(round(float(kup_dmg_ilosc)))
  	  				wyswietl_staty()
  	  				print(f"masz teraz {dodatek_dmg_kowal} dodatkowego dmg w broni")
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  			elif tak_czy_nie_dmg == "n":
  	  				print('namyśl sie kurwa')
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  		else:
  	  			print("nie stac cie palo niemyta")
  	  			print("")
  	  			input("kliknij cokolwiek aby kontynuowac")
  	  	if wybor == "2":
  	  		kup_shield_ilosc = input("Ile chcesz dodatkowego shielda?: ")
  	  		mnoznik = 4 + float(poziom_trudnosci)
  	  		cena_shield_kup = abs(float(kup_shield_ilosc)) * mnoznik
  	  		tak_czy_nie_shield = input(f"czy chcesz kupic {abs(round(float(kup_shield_ilosc)))} za {abs(round(float(cena_shield_kup)))} golda? (t/n): ")
  	  		if gold >= cena_shield_kup:
  	  			if tak_czy_nie_shield == "t":
  	  				gold = abs(round(gold)) - abs(round(cena_shield_kup))
  	  				dodatek_shield_kowal = abs(round(float(dodatek_shield_kowal))) + abs(round(float(kup_shield_ilosc)))
  	  				wyswietl_staty()
  	  				print(f"masz teraz {dodatek_shield_kowal} dodatkowego shielda do broni!")
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  			elif tak_czy_nie_shield == "n":
  	  				print('namyśl sie kurwa')
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  		else:
  	  			print("nie stac cie palo niemyta")
  	  			print("")
  	  			input("kliknij cokolwiek aby kontynuowac")
  	  	if wybor == "3":
  	  		kup_magicznydmg_ilosc = input("Ile chcesz dodatkowego magicznego dmg?: ")
  	  		mnoznik = 4 + float(poziom_trudnosci)
  	  		cena_mag_dmg_kup = abs(float(kup_magicznydmg_ilosc)) * mnoznik
  	  		tak_czy_nie_shield = input(f"czy chcesz kupic {abs(round(float(kup_magicznydmg_ilosc)))} magicznego dmg za {abs(round(float(cena_mag_dmg_kup)))} golda? (t/n): ")
  	  		if gold >= cena_mag_dmg_kup:
  	  			if tak_czy_nie_shield == "t":
  	  				gold = abs(round(gold)) - abs(round(cena_mag_dmg_kup))
  	  				dodatek_mag_dmg_kowal = abs(round(float(dodatek_mag_dmg_kowal))) + abs(round(float(kup_magicznydmg_ilosc)))
  	  				wyswietl_staty()
  	  				print(f"masz teraz {dodatek_mag_dmg_kowal} dodatkowego magicznego damage do broni!")
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  			elif tak_czy_nie_shield == "n":
  	  				print('namyśl sie kurwa')
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  		else:
  	  			print("nie stac cie palo niemyta")
  	  			print("")
  	  			input("kliknij cokolwiek aby kontynuowac")
  else:
  	print("jestes niedogrzany?")



