## WERSJA Z DNIA 05.01.2025
## AUTOR discord: nadi_nadi_nadi

import os, ctypes, sys, json
import random
import time
from colorama import Fore, Back, Style

## SAVE
with open('zapis.json', 'r') as x:
	data = json.load(x)


## OGOLNE
hp = data['hp_jak_cos_edytujesz_to_jestes_pizda']
mana = data['mana']
max_mana = data['max_mana']
shield = data['shield']
gold = data['gold']
moj_damage = data['moj_damage']
moj_magiczny_dmg = data['moj_magiczny_dmg']
obecna_lokacja = "lonka"
ile_razy_zwaliles = data['ile_razy_zwaliles']
ilosc_minionow = 0
zabezpieczenia = data['zabezpieczenia']
pokonani_wrogowie = data['pokonani_wrogowie']
wrog = None
wybor = None
### wrogowie
przeciwnik_huj = None
pusty_pokoj = False
dur_rece = data['dur_rece']
dur_klata = data['dur_klata']
dur_kule = data["dur_klata"]
dur_glowa = data['dur_glowa']

## krol
odebrane_1 = data['odebrane_1']
odebrane_2 = data['odebrane_2']
odebrane_3 = data['odebrane_3']
odebrane_4 = data['odebrane_4']

## POTKI
potka_hp = data['potka_hp']
potka_mana = data['potka_mana']
potka_granat = data['potka_granat']
potka_oslabienie = data['potka_oslabienie']


## ITEMY + TRUDNOSC
obecny_item_rece = data['obecny_item_rece']
obecny_item_klata = data['obecny_item_rece']
obecny_item_kule = data['obecny_item_kule']
obecny_item_glowa = data['obecny_item_glowa']
ile_lochow_przeszedles = data['ile_lochow_przeszedles']
poziom_trudnosci = data['poziom_trudnosci']
klasa = data['klasa']

## KOWAL
dodatek_dmg_kowal = data['dodatek_dmg_kowal']
dodatek_shield_kowal = data['dodatek_shield_kowal']
dodatek_mag_dmg_kowal = data['dodatek_mag_dmg_kowal']

os.system('cls')

### ITEMY
itemy = {
"brak": {"nr": "1", "dmg": 0, "shield": 0, "magiczne_obrazenia": 0, "cena_buy": 0, "slot": "rece"},
"kijek": {"nr": "2", "dmg": 2, "shield": 1, "magiczne_obrazenia": 1, "cena_buy": 12, "slot": "rece"},
"akumulator_na_kablu": {"nr": "3", "dmg": 100, "shield": 10, "magiczne_obrazenia": 1, "cena_buy": 1000, "slot": "rece"},
"mala_tarca": {"nr": "4", "dmg": 1, "shield": 3, "magiczne_obrazenia": 1, "cena_buy": 20, "slot": "rece"},
"duza_tarca": {"nr": "5", "dmg": 2, "shield": 5, "magiczne_obrazenia": 2, "cena_buy": 34, "slot": "rece"},
"bardzo_duza_tarcza": {"nr": "6", "dmg": 3, "shield": 6, "magiczne_obrazenia": 3, "cena_buy": 50, "slot": "rece"},
"maly_miecz": {"nr": "7", "dmg": 3, "shield": 1, "magiczne_obrazenia": 1, "cena_buy": 17, "slot": "rece"},
"sredni_miecz": {"nr": "8", "dmg": 4, "shield": 2, "magiczne_obrazenia": 2, "cena_buy": 24, "slot": "rece"},
"duzy_miecz": {"nr": "9", "dmg": 7, "shield": 3, "magiczne_obrazenia": 4, "cena_buy": 47, "slot": "rece"},
"rozdzka": {"nr": "10", "dmg": 0, "shield": 1,"magiczne_obrazenia": 4, "cena_buy": 20, "slot": "rece"},
"kostur": {"nr": "11", "dmg": 1, "shield": 1,"magiczne_obrazenia": 8, "cena_buy": 30, "slot": "rece"},
"czarny_kostur": {"nr": "12", "dmg": 1, "shield": 3,"magiczne_obrazenia": 12, "cena_buy": 42, "slot": "rece"},
"maly_napiersnik": {"nr": "13", "dmg": 0, "shield": 4, "magiczne_obrazenia": 2, "cena_buy": 40, "slot": "klata"},
"sredni_napiersnik": {"nr": "14", "dmg": 0, "shield": 6, "magiczne_obrazenia": 3, "cena_buy": 60, "slot": "klata"},
"duzy_napiersnik": {"nr": "15", "dmg": 0, "shield": 9, "magiczne_obrazenia": 4, "cena_buy": 80, "slot": "klata"},
"lekki_pancerz": {"nr": "16", "dmg": 0, "shield": 3, "magiczne_obrazenia": 1, "cena_buy": 30, "slot": "klata"},
"magiczny_pancerz": {"nr": "17", "dmg": 0, "shield": 5, "magiczne_obrazenia": 5, "cena_buy": 55, "slot": "klata"},
"ciezki_pancerz": {"nr": "18", "dmg": 0, "shield": 10, "magiczne_obrazenia": 3, "cena_buy": 90, "slot": "klata"},
"zloty_hełm": {"nr": "19", "dmg": 0, "shield": 5, "magiczne_obrazenia": 2, "cena_buy": 35, "slot": "glowa"},
"stalowy_hełm": {"nr": "20", "dmg": 0, "shield": 7, "magiczne_obrazenia": 3, "cena_buy": 50, "slot": "glowa"},
"cipek": {"nr": "21", "dmg": 999, "shield": 999, "magiczne_obrazenia": 1, "cena_buy": 1, "slot": "kule"},
"amulet_mocy": {"nr": "22", "dmg": 1, "shield": 1, "magiczne_obrazenia": 5, "cena_buy": 30, "slot": "kule"},
"kamień_mocy": {"nr": "23", "dmg": 0, "shield": 0, "magiczne_obrazenia": 12, "cena_buy": 45, "slot": "kule"},
"amulet_z_diamantem": {"nr": "24", "dmg": 1, "shield": 5, "magiczne_obrazenia": 2, "cena_buy": 50, "slot": "kule"},
"kulochron": {"nr": "25", "dmg": 1, "shield": 8, "magiczne_obrazenia": 2, "cena_buy": 50, "slot": "kule"},
"złoty_pierścień": {"nr": "26", "dmg": 0, "shield": 0, "magiczne_obrazenia": 7, "cena_buy": 30, "slot": "kule"},
"pierscionek_slubny": {"nr": "27", "dmg": 4, "shield": 4, "magiczne_obrazenia": 10, "cena_buy": 200, "slot": "rece"},
"SYF ITEMY PONIZEJ": {"nr": "28", "dmg": 0, "shield": 0, "magiczne_obrazenia": 0, "cena_buy": 9999, "slot": "X"},
"kolba": {"nr": "29", "dmg": 1, "shield": 0, "magiczne_obrazenia": 1, "cena_buy": 12, "slot": "rece"},
"fiut": {"nr": "30", "dmg": 1, "shield": 0, "magiczne_obrazenia": 1, "cena_buy": 12, "slot": "rece"},
"patyk": {"nr": "31", "dmg": 1, "shield": 0, "magiczne_obrazenia": 0, "cena_buy": 12, "slot": "rece"},
"galaz": {"nr": "32", "dmg": 1, "shield": 1, "magiczne_obrazenia": 0, "cena_buy": 12, "slot": "rece"},
"kamien": {"nr": "33", "dmg": 1, "shield": 1, "magiczne_obrazenia": 0, "cena_buy": 12, "slot": "rece"},
"glaz": {"nr": "34", "dmg": 2, "shield": 0, "magiczne_obrazenia": 0, "cena_buy": 12, "slot": "rece"},
"mokry jacek": {"nr": "35", "dmg": 2, "shield": 0, "magiczne_obrazenia": 1, "cena_buy": 12, "slot": "rece"},
"talerz": {"nr": "36", "dmg": 2, "shield": 0, "magiczne_obrazenia": 0, "cena_buy": 12, "slot": "rece"},
"gowno na patyku": {"nr": "37", "dmg": 1, "shield": 1, "magiczne_obrazenia": 1, "cena_buy": 12, "slot": "rece"},
}



potki = {
	"potka_hp": {"nr": "1", "hp": 5, "mana": "-", "cena_buy": 12},
	"potka_mana": {"nr": "2", "hp": "-", "mana": 10, "cena_buy": 12},
	"potka_granat": {"nr": "3", "hp": 10, "mana": "-", "cena_buy": 12},
	"potka_oslabienie": {"nr": "4", "hp": "/2", "mana": "-", "cena_buy": 12}
}


def wyswietl_wybory(lokalizacja1, lokalizacja2, lokalizacja3, lokalizacja4):
   print("")
   print(f"1. {lokalizacja1}")
   print(f"2. {lokalizacja2}")
   print(f"3. {lokalizacja3}")
   print(f"4. {lokalizacja4}")
   nazwa = 0
   nazwa = input("wybierz opcje (1,2,3,4): ")
   return nazwa

## OGOLNE
def info_staty():
	global hp, mana, max_mana, klasa, shield, obecna_lokacja, gold, moj_damage, moj_magiczny_dmg, obecny_item_rece, obecny_item_klata, obecny_item_kule, obecny_item_glowa, poziom_trudnosci, dodatek_shield_kowal, dodatek_dmg_kowal, dodatek_mag_dmg_kowal, potka_hp, potka_mana, potka_granat, potka_oslabienie, odebrane_1, odebrane_2, odebrane_3, odebrane_4, zabezpieczenia, pokonani_wrogowie, ile_lochow_przeszedles, ile_razy_zwaliles, dur_rece, dur_kule, dur_glowa, dur_klata
	do_zapisu2 = {
  				"hp": hp,
  				"mana": mana,
  				"max_mana": max_mana,
  				"shield": shield,
  				"gold": gold,
  				"moj_damage": moj_damage,
  				"moj_magiczny_dmg": moj_magiczny_dmg,
  				"obecny_item_rece": obecny_item_rece,
  				"obecny_item_klata": obecny_item_klata,
  				"obecny_item_kule": obecny_item_kule,
  				"obecny_item_glowa": obecny_item_glowa,
  				"poziom_trudnosci": poziom_trudnosci,
  				"dodatek_dmg_kowal": dodatek_dmg_kowal,
  				"dodatek_shield_kowal": dodatek_shield_kowal,
  				"dodatek_mag_dmg_kowal": dodatek_mag_dmg_kowal,
  				"potka_hp":potka_hp,
  				"potka_mana":potka_mana,
  				"potka_granat":potka_granat,
  				"potka_oslabienie":potka_oslabienie,
  				"zabezpieczenia": zabezpieczenia,
  				"ile_lochow_przeszedles": ile_lochow_przeszedles,
  				"ile_razy_zwaliles": ile_razy_zwaliles,
  				"dur_rece": dur_rece,
  				"dur_kule": dur_kule,
  				"dur_klata": dur_klata,
  				"dur_glowa": dur_glowa,
  				"lokacja": obecna_lokacja,
  				"klasa": klasa
	}
	with open('obecne_staty.json', 'w') as plikk:
  		json.dump(do_zapisu2, plikk, indent=14)
	time.sleep(.15)
	with open('nie_usuwac.txt', 'w') as x:
		x.write('t')

def wyswietl_staty():
	with open('obecne_staty.json', 'r') as x:
		data = json.load(x)
	xx_hp = data['hp']#
	xx_mana = data['mana']#
	xx_max_mana = data['max_mana']
	xx_shield = data['shield']#
	xx_gold = data['gold']#
	xx_moj_damage = data['moj_damage']#
	xx_moj_magiczny_dmg = data['moj_magiczny_dmg']#
	xx_zabezpieczenia = data['zabezpieczenia']  # INNE
	xx_dur_rece = data['dur_rece'] #
	xx_dur_klata = data['dur_klata'] #
	xx_dur_kule = data["dur_klata"] #
	xx_dur_glowa = data['dur_glowa'] #
	xx_obecna_lokacja = data['lokacja'] # INNE
	xx_potka_hp = data['potka_hp']#
	xx_potka_mana = data['potka_mana']#
	xx_potka_granat = data['potka_granat']#
	xx_potka_oslabienie = data['potka_oslabienie']#
	xx_obecny_item_rece = data['obecny_item_rece'] #
	xx_obecny_item_klata = data['obecny_item_klata'] #
	xx_obecny_item_kule = data['obecny_item_kule'] #
	xx_obecny_item_glowa = data['obecny_item_glowa'] #
	xx_ile_lochow_przeszedles = data['ile_lochow_przeszedles']
	xx_poziom_trudnosci = data['poziom_trudnosci']
	xx_dodatek_dmg_kowal = data['dodatek_dmg_kowal']#
	xx_dodatek_shield_kowal = data['dodatek_shield_kowal']#
	xx_dodatek_mag_dmg_kowal = data['dodatek_mag_dmg_kowal']#
	xx_klasa = data['klasa']
	os.system('cls')
	with open('obecne_staty.json', 'r') as x:
		data = json.load(x)
	print(Fore.GREEN + "-_-_-_-_-_-_-_-_-_-_-  PODSTAWOWE  -_-_-_-_-_-_-_-_-_-_-")
	print(Style.RESET_ALL)
	print(f"HP: {xx_hp}   MANA: {xx_mana} ({xx_max_mana})  SHIELD: {xx_shield}   GOLD: {xx_gold}   DMG: {xx_moj_damage}   MAG_DMG: {xx_moj_magiczny_dmg}")
	print("")
	print(Fore.GREEN + "-_-_-_-_-_-_-_-_-_-_-  PRZEDMIOTY  -_-_-_-_-_-_-_-_-_-_-")
	print(Style.RESET_ALL)
	print(f"KULE: {xx_obecny_item_kule} ({xx_dur_kule})   RECE: {xx_obecny_item_rece} ({xx_dur_rece})   KLATA: {xx_obecny_item_klata} ({xx_dur_klata})   GLOWA: {xx_obecny_item_glowa} ({xx_dur_glowa})")
	print("")
	print(Fore.GREEN + "-_-_-_-_-_-_-_-_-_-_-  POTKI  -_-_-_-_-_-_-_-_-_-_-")
	print(Style.RESET_ALL)
	print(f"POTKA_HP: {xx_potka_hp}   POTKA_MANA: {xx_potka_mana}   POTKA_GRANAT: {xx_potka_granat}   POTKA_OSLABIENIE: {xx_potka_oslabienie}")
	print("")
	print(Fore.GREEN + "-_-_-_-_-_-_-_-_-_-_-  BOOSTY  -_-_-_-_-_-_-_-_-_-_-")
	print(Style.RESET_ALL)
	print(f"KULE:  +{itemy[xx_obecny_item_kule]['dmg']} DMG   +{itemy[xx_obecny_item_kule]['shield']} SH   +{itemy[xx_obecny_item_kule]['magiczne_obrazenia']} MAG_DMG")
	print(f"RECE:  +{itemy[xx_obecny_item_rece]['dmg']} DMG   +{itemy[xx_obecny_item_rece]['shield']} SH   +{itemy[xx_obecny_item_rece]['magiczne_obrazenia']} MAG_DMG   (KOWAL_DMG: {xx_dodatek_dmg_kowal}   KOWAL_SH: {xx_dodatek_shield_kowal}   KOWAL_MAG_DMG: {xx_dodatek_mag_dmg_kowal})")  
	print(f"KLATA: +{itemy[xx_obecny_item_klata]['dmg']} DMG   +{itemy[xx_obecny_item_klata]['shield']} SH   +{itemy[xx_obecny_item_klata]['magiczne_obrazenia']} MAG_DMG")
	print(f"GLOWA: +{itemy[xx_obecny_item_glowa]['dmg']} DMG   +{itemy[xx_obecny_item_glowa]['shield']} SH   +{itemy[xx_obecny_item_glowa]['magiczne_obrazenia']} MAG_DMG")
	print("")
	print(Fore.GREEN + "-_-_-_-_-_-_-_-_-_-_-  INNE  -_-_-_-_-_-_-_-_-_-_-")
	print(Style.RESET_ALL)
	print(f"TRUDNOSC: {xx_poziom_trudnosci}   ILE_LOCHOW_PRZESZEDLES: {xx_ile_lochow_przeszedles}   KLASA: {xx_klasa}")
	DAWAJ_TERAZ = False	

	
def przeciwnik(hp, dmg):
	global przeciwnik_huj
	przeciwnik_huj = {"hp_przeciwnik": hp, "obrazenia_przeciwnik": dmg}
#def wyswietl_staty():
#		global hp, mana, shield, moj_damage, gold, obecna_lokacja, poziom_trudnosci, dur_rece, dur_kule, dur_glowa, dur_klata
#		ctypes.windll.kernel32.SetConsoleTitleW(f"|  hp {round(hp)}  |  mana: {round(mana)}  |  shield: {round(shield)} (+{round(dodatek_shield_kowal)})  |  damage: {round(moj_damage)} (+{round(dodatek_dmg_kowal)})  |  mag_damage: {round(moj_magiczny_dmg)} (+{round(dodatek_mag_dmg_kowal)})  |  gold: {round(gold)}  |  lokalizacja: {obecna_lokacja}  |  itemy: {obecny_item_kule}({dur_kule})/{obecny_item_rece}({dur_rece})/{obecny_item_klata}({dur_klata})/{obecny_item_glowa}({dur_glowa})  |  trudnosc: {round(poziom_trudnosci)}")
def wygeneruj_wroga():
	global wrog
	rodzaj_wroga = random.randint(1, 8)
	if rodzaj_wroga == 1:
			wrog = "szkielet"
	elif rodzaj_wroga == 2:
	    	wrog = "andrzej"
	elif rodzaj_wroga == 3:
	    	wrog = "antek"
	elif rodzaj_wroga == 4:
			wrog = "kurvinox"
	elif rodzaj_wroga == 5:
			wrog = "ognisko"
	elif rodzaj_wroga == 6:
			wrog = "skrzynia"
	elif rodzaj_wroga == 7:
			wrog = "cipster"
	elif rodzaj_wroga == 8:
			wrog = "uczen 1 klasy technik informatyk"
	if rodzaj_wroga == 5:
		print('pokoj jest pusty')
	if rodzaj_wroga == 6:
		print("w pokoju jest skrzynia")
	if rodzaj_wroga == 1 or rodzaj_wroga == 2 or rodzaj_wroga == 3 or rodzaj_wroga == 4 or rodzaj_wroga == 7 or rodzaj_wroga == 8:
		print(f"twoj wrog to {wrog}")
		print('on zaczyna')
def lootowanie():
	global gold, obecny_item_rece, shield, hp, moj_damage, itemy, obecny_item_klata, obecny_item_kule, obecny_item_glowa, zabezpieczenia, potka_hp, potka_mana, potka_granat, potka_oslabienie, info_staty
	numerek = random.randint(1, 1000)
	if 1 <= numerek <= 5:
		ile_golda_kill = random.randint(14, 19) + (poziom_trudnosci * 2)
		gold = gold + ile_golda_kill
		print(f"dostajesz {ile_golda_kill} golda fartowna kurwo (0.5%)")
		info_staty()
		info_staty()
		time.sleep(5)
	elif 6 <= numerek <= 15:
		ile_golda_kill = random.randint(9, 14) + (poziom_trudnosci * 2)
		gold = gold + ile_golda_kill
		print(f"dostajesz {ile_golda_kill} golda, ladnie (1%)")
		info_staty()
		info_staty()
		time.sleep(5)
	elif 16 <= numerek <= 65:
		ile_golda_kill = random.randint(5, 7) + (poziom_trudnosci * 2)
		gold = gold + ile_golda_kill
		print(f"dostajesz {ile_golda_kill} golda! (5%)")
		info_staty()
		info_staty()
		time.sleep(4)
	elif 66 <= numerek <= 75:
		if obecny_item_rece == "brak":
			print("masz farta kurwo ze nie masz nic w rekach (1%)")
			time.sleep(4)
		else:
			if zabezpieczenia <= 0:
				shield = shield - itemy[obecny_item_rece]['shield']
				moj_damage = moj_damage - itemy[obecny_item_rece]['dmg']
				print('rozpierdalasz swoj item z reki, lipa (2%)')
				obecny_item_rece = "brak"
				info_staty()
				info_staty()
				time.sleep(4)
			else:
				zabezpieczenia = zabezpieczenia - 1
				print("blokujesz rozjebanie itema, gratulacje! (2%)")
				info_staty()
				info_staty()
				time.sleep(4)
	elif 76 <= numerek <= 85:
		if obecny_item_kule == "brak":
			print("masz farta kurwo ze nie masz nic na jajcach (1%)")
			time.sleep(4)
		else:
			if zabezpieczenia <= 0:
				shield = shield - itemy[obecny_item_kule]['shield']
				moj_damage = moj_damage - itemy[obecny_item_kule]['dmg']
				print('rozpierdalasz swoj item z jajec, lipa (1%)')
				obecny_item_kule = "brak"
				info_staty()
				info_staty()
				time.sleep(4)
			else:
				zabezpieczenia = zabezpieczenia - 1
				print("blokujesz rozjebanie itema, gratulacje! (1%)")
				info_staty()
				info_staty()
				time.sleep(4)
	elif 86 <= numerek <= 95:
		if obecny_item_klata == "brak":
			print("masz farta kurwo ze nie masz nic na klacie (1%)")
			time.sleep(4)
		else:
			if zabezpieczenia <= 0:
				shield = shield - itemy[obecny_item_klata]['shield']
				moj_damage = moj_damage - itemy[obecny_item_klata]['dmg']
				print('rozpierdalasz swoja klate, lipa (1%)')
				obecny_item_klata = "brak"
				info_staty()
				info_staty()
				time.sleep(4)
			else:
				zabezpieczenia = zabezpieczenia - 1
				print("blokujesz rozjebanie itema, gratulacje! (1%)")
				info_staty()
				info_staty()
				time.sleep(4)
	elif 96 <= numerek <= 105:
		if obecny_item_glowa == "brak":
			print("masz farta kurwo ze nie masz nic na glowie (1%)")
			time.sleep(4)
		else:
			if zabezpieczenia <= 0:
				shield = shield - itemy[obecny_item_glowa]['shield']
				moj_damage = moj_damage - itemy[obecny_item_glowa]['dmg']
				print('rozpierdalasz swoj helm, lipa (1%)')
				obecny_item_glowa = "brak"
				info_staty()
				info_staty()
				time.sleep(4)
			else:
				zabezpieczenia = zabezpieczenia - 1
				print("blokujesz rozjebanie itema, gratulacje! (1%)")
				info_staty()
				info_staty()
				time.sleep(4)
	elif 106 <= numerek <= 205:
			ile_damage_kill = random.randint(1, 2)
			print("nakluwasz sie na kolbe potwora (10%)")
			print(f"dostajesz {ile_damage_kill} damage")
			hp = hp - ile_damage_kill
			info_staty()
			info_staty()
			time.sleep(4)
	elif 206 <= numerek <= 245:
		potki_lista = ["potka_hp", "potka_mana", "potka_granat", 'potka_oslabienie']
		wylosowana = random.choice(potki_lista)
		print(f"dostajesz {wylosowana}! (1%)")
		if wylosowana == "potka_hp":
			potka_hp = potka_hp + 1
		if wylosowana == "potka_mana":
			potka_mana = potka_mana + 1
		if wylosowana == "potka_granat":
			potka_granat = potka_granat + 1
		if wylosowana == "potka_oslabienie":
			potka_oslabienie = potka_oslabienie + 1
		info_staty()
		info_staty()
		time.sleep(3)
	elif 246 <= numerek <= 1000:
		ile_golda_kill = random.randint(1, 3) + (poziom_trudnosci * 2)
		gold = gold + ile_golda_kill
		print(f"dostajesz {ile_golda_kill} golda! (75.5%)")
		info_staty()
		info_staty()
		time.sleep(2)

def losuj_syf(): # 29 - 37
	global shield, moj_damage, moj_magiczny_dmg, itemy, obecny_item_rece, info_staty, dur_rece
	losowy_nr = random.randint(29, 37)
	losowy_nr = str(losowy_nr)
	for item in itemy:
  	  	for staty in itemy[item]:
  	  		if staty == "nr":
  	  			if itemy[item]['nr'] == losowy_nr:
  	  				if obecny_item_rece != "brak":
  	  					tak_nie_zamiana = input(f"wylosowales {item}! chcesz go zamienic za swoj item w rece? (t/n): ")
  	  					if tak_nie_zamiana == "t":
  	  						dur_rece = 50
  	  						shield = shield - itemy[obecny_item_rece]['shield']
  	  						moj_damage = moj_damage - itemy[obecny_item_rece]['dmg']
  	  						moj_magiczny_dmg = moj_magiczny_dmg - itemy[obecny_item_rece]['magiczne_obrazenia']
  	  						info_staty()
  	  						info_staty()
  	  						obecny_item_rece = item
  	  						time.sleep(1)
  	  						shield = shield + itemy[item]['shield']
  	  						moj_damage = moj_damage + itemy[item]['dmg']
  	  						moj_magiczny_dmg = moj_magiczny_dmg + itemy[item]['magiczne_obrazenia']
  	  						info_staty()
  	  						info_staty()
  	  						time.sleep(2)
  	  					elif tak_nie_zamiana == "n":
  	  						print("ok")
  	  						time.sleep(1)
  	  				else:
  	  					dur_rece = 50
  	  					print(f"Dostajesz {item}!")
  	  					obecny_item_rece = item
  	  					shield = shield + itemy[item]['shield']
  	  					moj_damage = moj_damage + itemy[item]['dmg']
  	  					moj_magiczny_dmg = moj_magiczny_dmg + itemy[item]['magiczne_obrazenia']
  	  					info_staty()
  	  					info_staty()
  	  					time.sleep(3)

def obecne_staty():
	global info_staty, hp, mana, max_mana, klasa, shield, gold, moj_damage, obecna_lokacja, moj_magiczny_dmg, obecny_item_rece, obecny_item_klata, obecny_item_kule, obecny_item_glowa, poziom_trudnosci, dodatek_shield_kowal, dodatek_dmg_kowal, dodatek_mag_dmg_kowal, potka_hp, potka_mana, potka_granat, potka_oslabienie, odebrane_1, odebrane_2, odebrane_3, odebrane_4, zabezpieczenia, pokonani_wrogowie, ile_lochow_przeszedles, ile_razy_zwaliles, dur_rece, dur_kule, dur_glowa, dur_klata
	do_zapisu = {
  				"hp": hp,
  				"mana": mana,
  				"max_mana": max_mana,
  				"shield": shield,
  				"gold": gold,
  				"moj_damage": moj_damage,
  				"moj_magiczny_dmg": moj_magiczny_dmg,
  				"obecny_item_rece": obecny_item_rece,
  				"obecny_item_klata": obecny_item_klata,
  				"obecny_item_kule": obecny_item_kule,
  				"obecny_item_glowa": obecny_item_glowa,
  				"poziom_trudnosci": poziom_trudnosci,
  				"dodatek_dmg_kowal": dodatek_dmg_kowal,
  				"dodatek_shield_kowal": dodatek_shield_kowal,
  				"dodatek_mag_dmg_kowal": dodatek_mag_dmg_kowal,
  				"potka_hp":potka_hp,
  				"potka_mana":potka_mana,
  				"potka_granat":potka_granat,
  				"potka_oslabienie":potka_oslabienie,
  				"odebrane_1":odebrane_1,
  				"odebrane_2":odebrane_2,
  				"odebrane_3":odebrane_3,
  				"odebrane_4":odebrane_4,
  				"zabezpieczenia": zabezpieczenia,
  				"pokonani_wrogowie": pokonani_wrogowie,
  				"ile_lochow_przeszedles": ile_lochow_przeszedles,
  				"ile_razy_zwaliles": ile_razy_zwaliles,
  				"dur_rece": dur_rece,
  				"dur_kule": dur_kule,
  				"dur_klata": dur_klata,
  				"dur_glowa": dur_glowa,
  				"lokacja": obecna_lokacja,
  				"klasa": klasa
	}
	with open('obecne_staty.json', 'w') as plik:
  		json.dump(do_zapisu, plik, indent=14)

## WALKA LOCHY
def walka_wrecz():
	global info_staty, obecny_item_rece, obecny_item_kule, moj_magiczny_dmg, itemy, obecny_item_glowa, obecny_item_klata, hp, dur_rece, dur_kule, dur_glowa, dur_klata, moj_damage, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia
	print("")
	if obecny_item_rece != "brak":
		dur_rece = dur_rece - 1
		if dur_rece <= 0:
			print("rozwalasz swoj item!")
			shield = shield - itemy[obecny_item_rece]['shield']
			moj_damage = moj_damage - itemy[obecny_item_rece]['dmg']
			moj_magiczny_dmg = moj_magiczny_dmg - itemy[obecny_item_rece]['magiczne_obrazenia']
			obecny_item_rece = "brak"
	if obecny_item_kule != "brak":
		dur_kule = dur_kule - 1
		if dur_kule <= 0:
			print("rozwalasz swoj item!")
			shield = shield - itemy[obecny_item_kule]['shield']
			moj_damage = moj_damage - itemy[obecny_item_kule]['dmg']
			moj_magiczny_dmg = moj_magiczny_dmg - itemy[obecny_item_kule]['magiczne_obrazenia']
			obecny_item_kule = "brak"
	nowe_dmg_przeciwnika = przeciwnik_huj['obrazenia_przeciwnik'] - shield
	if nowe_dmg_przeciwnika <= 0:
		nowe_dmg_przeciwnika = 0
	hp = hp - nowe_dmg_przeciwnika
	if hp <= 0:
		print("umarles, lamus lol")
		#wyzeruj_staty()
		time.sleep(4)
		os._exit(1)
	print(f"dostales wpierdol o {nowe_dmg_przeciwnika} hp, zostalo ci {hp}")
	info_staty()
	info_staty()
	przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - moj_damage - dodatek_dmg_kowal
	print(f"lamusowi zostalo {przeciwnik_huj['hp_przeciwnik']}")
	if obecny_item_rece == "krwawe_ostrze":
		hp = hp + 1
		print("leczysz sie o 1 hp!")
		info_staty()
		info_staty()
		time.sleep(0.5)
	if obecny_item_kule == "pierscionek_slubny":
		los_mana = random.randint(2, 4)
		mana = mana + los_mana
		print(f"dostajesz dodatkowo {los_mana} many!")
		info_staty()
		info_staty()
		time.sleep(0.5)
	time.sleep(2)
	os.system('cls')
	print(f"twoj wrog to {wrog}")
	print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
def potiony():
	global info_staty, obecny_item_rece, obecny_item_kule, moj_magiczny_dmg, itemy, obecny_item_glowa, obecny_item_klata, hp, dur_rece, dur_kule, dur_glowa, dur_klata, hp, moj_damage, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia, potka_hp, potka_mana, potka_granat, potka_oslabienie
	print("")
	if obecny_item_rece != "brak":
		dur_rece = dur_rece - 1
		if dur_rece <= 0:
			print("rozwalasz swoj item!")
			shield = shield - itemy[obecny_item_rece]['shield']
			moj_damage = moj_damage - itemy[obecny_item_rece]['dmg']
			moj_magiczny_dmg = moj_magiczny_dmg - itemy[obecny_item_rece]['magiczne_obrazenia']
			obecny_item_rece = "brak"
	if obecny_item_kule != "brak":
		dur_kule = dur_kule - 1
		if dur_kule <= 0:
			print("rozwalasz swoj item!")
			shield = shield - itemy[obecny_item_kule]['shield']
			moj_damage = moj_damage - itemy[obecny_item_kule]['dmg']
			moj_magiczny_dmg = moj_magiczny_dmg - itemy[obecny_item_kule]['magiczne_obrazenia']
			obecny_item_kule = "brak"
	ktora_potka = wyswietl_wybory(f"potka_hp ({potka_hp})", f"potka_mana ({potka_mana})", f"potka_granat ({potka_granat})", f"potka_oslabienie ({potka_oslabienie})")
	if ktora_potka == "1":
		if potka_hp != 0:
			nowe_dmg_przeciwnika = przeciwnik_huj['obrazenia_przeciwnik'] - shield
			if nowe_dmg_przeciwnika <= 0:
				nowe_dmg_przeciwnika = 0
			hp = hp + 5
			potka_hp = potka_hp - 1
			hp = hp - nowe_dmg_przeciwnika
			if hp <= 0:
				print("umarles, lamus lol")
				#wyzeruj_staty()
				time.sleep(4)
				os._exit(1)
			print(f"dostales wpierdol o {nowe_dmg_przeciwnika} hp, zostalo ci {hp}")
			info_staty()
			info_staty()
			przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - moj_damage - dodatek_dmg_kowal
			print(f"lamusowi zostalo {przeciwnik_huj['hp_przeciwnik']}")
			if obecny_item_rece == "krwawe_ostrze":
				hp = hp + 1
				print("leczysz sie o 1 hp!")
				info_staty()
				info_staty()
				time.sleep(0.5)
			if obecny_item_kule == "pierscionek_slubny":
				los_mana = random.randint(2,4)
				mana = mana + los_mana
				print(f"dostajesz dodatkowo {los_mana} many!")
				info_staty()
				info_staty()
				time.sleep(0.5)
			time.sleep(5)
			os.system('cls')
			print(f"twoj wrog to {wrog}")
			print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
	if ktora_potka == "2":
		if potka_mana != 0:
			nowe_dmg_przeciwnika = przeciwnik_huj['obrazenia_przeciwnik'] - shield
			if nowe_dmg_przeciwnika <= 0:
				nowe_dmg_przeciwnika = 0
			mana = mana + 10
			potka_mana = potka_mana - 1
			hp = hp - nowe_dmg_przeciwnika
			if hp <= 0:
				print("umarles, lamus lol")
				#wyzeruj_staty()
				time.sleep(4)
				os._exit(1)
			print(f"dostales wpierdol o {nowe_dmg_przeciwnika} hp, zostalo ci {hp}")
			info_staty()
			info_staty()
			przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - moj_damage - dodatek_dmg_kowal
			print(f"lamusowi zostalo {przeciwnik_huj['hp_przeciwnik']}")
			if obecny_item_rece == "krwawe_ostrze":
				hp = hp + 1
				print("leczysz sie o 1 hp!")
				info_staty()
				info_staty()
				time.sleep(0.5)
			if obecny_item_kule == "pierscionek_slubny":
				los_mana = random.randint(2,4)
				mana = mana + los_mana
				print(f"dostajesz dodatkowo {los_mana} many!")
				info_staty()
				info_staty()
				time.sleep(0.5)
			time.sleep(5)
			os.system('cls')
			print(f"twoj wrog to {wrog}")
			print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
	if ktora_potka == "3":
		if potka_granat != 0:
			nowe_dmg_przeciwnika = przeciwnik_huj['obrazenia_przeciwnik'] - shield
			if nowe_dmg_przeciwnika <= 0:
				nowe_dmg_przeciwnika = 0
			potka_granat = potka_granat - 1
			czy_wybucha = random.randint(1, 100)
			if czy_wybucha == 100:
				print("wyjebalo ci w lapach xd (1%)")
				hp = hp - 5
				info_staty()
				info_staty()
			hp = hp - nowe_dmg_przeciwnika
			if hp <= 0:
				print("umarles, lamus lol")
				#wyzeruj_staty()
				time.sleep(4)
				os._exit(1)
			print(f"dostales wpierdol o {nowe_dmg_przeciwnika} hp, zostalo ci {hp}")
			info_staty()
			info_staty()
			przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - moj_damage - dodatek_dmg_kowal
			przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - 10
			print(f"lamusowi zostalo {przeciwnik_huj['hp_przeciwnik']}")
			if obecny_item_rece == "krwawe_ostrze":
				hp = hp + 1
				print("leczysz sie o 1 hp!")
				info_staty()
				info_staty()
				time.sleep(0.5)
			if obecny_item_kule == "pierscionek_slubny":
				los_mana = random.randint(2,4)
				mana = mana + los_mana
				print(f"dostajesz dodatkowo {los_mana} many!")
				info_staty()
				info_staty()
				time.sleep(0.5)
			time.sleep(5)
			os.system('cls')
			print(f"twoj wrog to {wrog}")
			print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
	if ktora_potka == "4":
		if potka_oslabienie != 0:
			nowe_dmg_przeciwnika = przeciwnik_huj['obrazenia_przeciwnik'] - shield
			oslabione_dmg = nowe_dmg_przeciwnika / 2
			if oslabione_dmg <= 0:
				oslabione_dmg = 0
			potka_oslabienie = potka_oslabienie - 1
			hp = hp - oslabione_dmg
			if hp <= 0:
				print("umarles, lamus lol")
				#wyzeruj_staty()
				time.sleep(4)
				os._exit(1)
			print(f"dostales wpierdol o {oslabione_dmg} hp, zostalo ci {hp}")
			info_staty()
			info_staty()
			przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - moj_damage - dodatek_dmg_kowal
			print(f"lamusowi zostalo {przeciwnik_huj['hp_przeciwnik']}")
			if obecny_item_rece == "krwawe_ostrze":
				hp = hp + 1
				print("leczysz sie o 1 hp!")
				info_staty()
				info_staty()
				time.sleep(0.5)
			if obecny_item_kule == "pierscionek_slubny":
				los_mana = random.randint(2,4)
				mana = mana + los_mana
				print(f"dostajesz dodatkowo {los_mana} many!")
				info_staty()
				info_staty()
				time.sleep(0.5)
			time.sleep(5)
			os.system('cls')
			print(f"twoj wrog to {wrog}")
			print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")




def kula_ognia():
	global info_staty, hp, moj_damage, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia, max_mana
	nowe_dmg_przeciwnika = przeciwnik_huj['obrazenia_przeciwnik'] - shield
	if nowe_dmg_przeciwnika <= 0:
		nowe_dmg_przeciwnika = 0
	hp = hp - nowe_dmg_przeciwnika
	if hp <= 0:
		print("umarles, lamus lol")
		#wyzeruj_staty()
		time.sleep(4)
		os._exit(1)
	print(f"dostales wpierdol o {nowe_dmg_przeciwnika} hp, zostalo ci {hp}")
	time.sleep(2)
	mana = mana - 20
	info_staty()
	info_staty()
	if mana <= 0:
		hp = hp + mana
		if hp <= 0:
			print("umarles, lamus lol")
			#wyzeruj_staty()
			time.sleep(4)
			os._exit(1)
		print("nie masz many pało niemyta lol")
		przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - 8 - dodatek_mag_dmg_kowal - moj_magiczny_dmg
		print(f"lamusowi zostalo {round(przeciwnik_huj['hp_przeciwnik'])}")
		mana = 0
		info_staty()
		info_staty()
		time.sleep(2)
		os.system("cls")
		print(f"twoj wrog to {wrog}")
		print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
	else:
		przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - 8 - dodatek_mag_dmg_kowal - moj_magiczny_dmg
		print(f"lamusowi zostalo {przeciwnik_huj['hp_przeciwnik']}")
		info_staty()
		info_staty()
def hazard():
	 global info_staty, max_mana, hp, moj_damage, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia
	 print("")
	 mana = mana - 20
	 damage_automatu = random.randint(6, 12) + moj_magiczny_dmg
	 print(f"twoj damage to {damage_automatu}!!")
	 nowe_dmg_przeciwnika = przeciwnik_huj['obrazenia_przeciwnik'] - shield
	 if nowe_dmg_przeciwnika <= 0:
	 	nowe_dmg_przeciwnika = 0
	 hp = hp - nowe_dmg_przeciwnika
	 print(f"dostales wpierdol o {nowe_dmg_przeciwnika}, zostaje ci {hp} hp")
	 if hp <= 0:
	 	print("umarles, lamus lol")
	 	#wyzeruj_staty()
	 	time.sleep(4)
	 	os._exit(1)
	 info_staty()
	 info_staty()
	 if mana <= 0:
	 	hp = hp + mana
	 	info_staty()
	 	info_staty()
	 	print(f"nie masz many, dostajesz {mana} hp!")
	 	if hp <= 0:
	 		print("umarles, lamus lol")
	 		#wyzeruj_staty()
	 		time.sleep(4)
	 		os._exit(1)
	 	przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - damage_automatu - dodatek_mag_dmg_kowal
	 	print(f"lamusowi zostalo {przeciwnik_huj['hp_przeciwnik']}")
	 	mana = 0
	 	info_staty()
	 	info_staty()
	 	time.sleep(2)
	 else:
	 	przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - damage_automatu - dodatek_mag_dmg_kowal
	 	print(f"lamusowi zostalo {przeciwnik_huj['hp_przeciwnik']}")
	 	info_staty()
	 	info_staty()
	 	time.sleep(2)
	 os.system('cls')
	 print(f"twoj wrog to {wrog}")
	 print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
def obrona():
	        			global info_staty, hp, moj_damage, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia
	        			print("")
	        			obrona_przeciwnik_dmg = przeciwnik_huj['obrazenia_przeciwnik'] * 0.8
	        			nowe_dmg_przeciwnika = obrona_przeciwnik_dmg - shield
	        			if nowe_dmg_przeciwnika <= 0:
	        				nowe_dmg_przeciwnika = 0
	        				hp = hp - 1
	        				print(f"dostales wpierdol o 1 hp, zostalo ci {hp}")
	        				info_staty()
	        				info_staty()
	        			else:
	        				hp = hp - nowe_dmg_przeciwnika
	        				print(f"dostales wpierdol o {nowe_dmg_przeciwnika} hp, zostalo ci {hp}")
	        				info_staty()
	        				info_staty()
	        			if hp <= 0:
	        				print("umarles, lamus lol")
	        				#wyzeruj_staty()
	        				time.sleep(4)
	        				os._exit(1)
	        			moj_damage_obrona = moj_damage / 2
	        			przeciwnik_huj['hp_przeciwnik'] = przeciwnik_huj['hp_przeciwnik'] - moj_damage_obrona - dodatek_dmg_kowal
	        			print(f"lamusowi zostalo {przeciwnik_huj['hp_przeciwnik']}")
	        			time.sleep(2)
	        			os.system('cls')
	        			print(f"twoj wrog to {wrog}")
	        			print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")


## BOSS WALKA
def losowanie_atak_boss():
	global ilosc_minionow, info_staty_boss, info_staty
	rodzaj_ataku = random.randint(1,3) # summon, bije, 
	if rodzaj_ataku == 1:
		losuj_miniony = random.randint(1,3)
		ilosc_minionow = ilosc_minionow + losuj_miniony
		print(f'boss respi {losuj_miniony} minionow!')
		info_staty_boss()
		return "miniony"
	if rodzaj_ataku == 2:
		return "bije"
	if rodzaj_ataku == 3:
		return "siada na morde"
ilosc_dmg_miniony = 0
def walka_wrecz_boss():
	global info_staty, hp, info_staty_boss, boss_hp, moj_damage, ilosc_minionow, ilosc_dmg_miniony, losowanie_atak_boss, ilosc_minionow, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia, obecny_item_rece, obecny_item_kule
	boss_hp = boss_hp - moj_damage - dodatek_dmg_kowal
	print("")
	print(f"walnales bossa o {moj_damage + dodatek_dmg_kowal}")
	if obecny_item_rece == "krwawe_ostrze":
		hp = hp + 1
		print("leczysz sie o 1 hp!")
		info_staty_boss()
		time.sleep(0.5)
	if obecny_item_kule == "pierscionek_slubny":
		los_mana = random.randint(2,4)
		mana = mana + los_mana
		print(f"dostajesz dodatkowo {los_mana} many!")
		info_staty_boss()
		time.sleep(0.5)
	rodzaj_ataku_boss = losowanie_atak_boss()
	if rodzaj_ataku_boss == "miniony":
		ilosc_dmg_miniony = (ilosc_minionow * 3) - shield
		if ilosc_dmg_miniony <= 0:
			ilosc_dmg_miniony = 0
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)

	if rodzaj_ataku_boss == "bije":
		dmg_bossa = random.randint(14, 19) - shield
		if dmg_bossa <= 0:
			dmg_bossa = 0
		hp = hp - dmg_bossa
		print(f'dostajesz wpierdol o {dmg_bossa}, zostaje ci {hp}')
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)

	if rodzaj_ataku_boss == "siada na morde":
		dmg_siad_na_morde = random.randint(2, 5)
		hp = hp - dmg_siad_na_morde
		print(f"boss siada ci na morde i dostajesz {dmg_siad_na_morde} hp, zostaje ci {hp} hp")
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)
def potiony_boss():
	global hp, ilosc_dmg_miniony, info_staty_boss, boss_hp, moj_damage, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia, potka_hp, potka_mana, potka_granat, potka_oslabienie, obecny_item_rece, obecny_item_kule
	print("")
	ktora_potka = wyswietl_wybory(f"potka_hp ({potka_hp})", f"potka_mana ({potka_mana})", f"potka_granat ({potka_granat})", f"potka_oslabienie ({potka_oslabienie})")
	if ktora_potka == "1":
		if potka_hp != 0:
			hp = hp + 5
			potka_hp = potka_hp - 1
			boss_hp = boss_hp - moj_damage - dodatek_dmg_kowal
			print(f"walnales go o {moj_damage + dodatek_dmg_kowal} i uleczyles sie o 5 hp!")
			if obecny_item_rece == "krwawe_ostrze":
				hp = hp + 1
				print("leczysz sie o 1 hp!")
				info_staty_boss()
				time.sleep(0.5)
			if obecny_item_kule == "pierscionek_slubny":
				los_mana = random.randint(2,4)
				mana = mana + los_mana
				print(f"dostajesz dodatkowo {los_mana} many!")
				info_staty_boss()
				time.sleep(0.5)
		else:
			print("nie masz potek, tracisz ture lamusie")
	if ktora_potka == "2":
		if potka_mana != 0:
			mana = mana + 10
			potka_mana = potka_mana - 1
			boss_hp = boss_hp - moj_damage - dodatek_dmg_kowal
			print(f"walnales go o {moj_damage + dodatek_dmg_kowal} i dodajesz se 10 many!")
			if obecny_item_rece == "krwawe_ostrze":
				hp = hp + 1
				print("leczysz sie o 1 hp!")
				info_staty_boss()
				time.sleep(0.5)
			if obecny_item_kule == "pierscionek_slubny":
				los_mana = random.randint(2,4)
				mana = mana + los_mana
				print(f"dostajesz dodatkowo {los_mana} many!")
				info_staty_boss()
				time.sleep(0.5)
		else:
			print("nie masz potek, tracisz ture lamusie")
	if ktora_potka == "3":
		if potka_granat != 0:
			potka_granat = potka_granat - 1
			czy_wybucha = random.randint(1, 100)
			if czy_wybucha == 100:
				print("wyjebalo ci w lapach xd (1%)")
				hp = hp - 5
				info_staty_boss()
			if hp <= 0:
				print("umarles, lamus lol")
				wyzeruj_staty_boss()
				time.sleep(4)
				os._exit(1)
			boss_hp = boss_hp - moj_damage - dodatek_dmg_kowal
			boss_hp = boss_hp - 10
			print(f"walnales go o {moj_damage + dodatek_dmg_kowal} i do tego zadales 10 hp z potki!")
			if obecny_item_rece == "krwawe_ostrze":
				hp = hp + 1
				print("leczysz sie o 1 hp!")
				info_staty_boss()
				time.sleep(0.5)
			if obecny_item_kule == "pierscionek_slubny":
				los_mana = random.randint(2,4)
				mana = mana + los_mana
				print(f"dostajesz dodatkowo {los_mana} many!")
				info_staty_boss()
				time.sleep(0.5)
		else:
			print("nie masz potek, tracisz ture lamusie")
	if ktora_potka == "4":
		if potka_oslabienie != 0:
			potka_oslabienie = potka_oslabienie - 1
			info_staty()
			boss_hp = boss_hp - moj_damage - dodatek_dmg_kowal
			print(f"walnales go o {moj_damage + dodatek_dmg_kowal} i oslabiles jego nastepny atak!")
			if obecny_item_rece == "krwawe_ostrze":
				hp = hp + 1
				print("leczysz sie o 1 hp!")
				info_staty_boss()
				time.sleep(0.5)
			if obecny_item_kule == "pierscionek_slubny":
				los_mana = random.randint(2,4)
				mana = mana + los_mana
				print(f"dostajesz dodatkowo {los_mana} many!")
				info_staty_boss()
				time.sleep(0.5)
		else:
			print("nie masz potek, tracisz ture lamusie")
	rodzaj_ataku_boss = losowanie_atak_boss()
	if rodzaj_ataku_boss == "miniony":
		ilosc_dmg_miniony = (ilosc_minionow * 3) - shield
		if ilosc_dmg_miniony <= 0:
			ilosc_dmg_miniony = 0
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)

	if rodzaj_ataku_boss == "bije":
		if ktora_potka == "4":
			dmg_bossa = random.randint(10, 15) - shield
			if dmg_bossa <= 0:
				dmg_bossa = 0
			hp = hp - dmg_bossa
			print(f'dostajesz wpierdol o {dmg_bossa}, zostaje ci {hp}')
			hp = hp - ilosc_dmg_miniony
			print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
			info_staty_boss()
			time.sleep(5)
		else:
			dmg_bossa = random.randint(20, 30) - shield
			if dmg_bossa <= 0:
				dmg_bossa = 0
			hp = hp - dmg_bossa
			print(f'dostajesz wpierdol o {dmg_bossa}, zostaje ci {hp}')
			hp = hp - ilosc_dmg_miniony
			print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
			info_staty_boss()
			time.sleep(5)

	if rodzaj_ataku_boss == "siada na morde":
		if ktora_potka == "4":
			dmg_siad_na_morde = random.randint(2, 3)
			hp = hp - dmg_siad_na_morde
			print(f"boss siada ci na morde i dostajesz {dmg_siad_na_morde} hp, zostaje ci {hp} hp")
			hp = hp - ilosc_dmg_miniony
			print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
			info_staty_boss()
			time.sleep(5)
		else:
			dmg_siad_na_morde = random.randint(3, 6)
			hp = hp - dmg_siad_na_morde
			print(f"boss siada ci na morde i dostajesz {dmg_siad_na_morde} hp, zostaje ci {hp} hp")
			hp = hp - ilosc_dmg_miniony
			print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
			info_staty_boss()
			time.sleep(5)
def kula_ognia_boss():
	global hp, info_staty_boss, boss_hp, moj_damage, ilosc_minionow, moj_magiczny_dmg, ilosc_dmg_miniony, losowanie_atak_boss, ilosc_minionow, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia

	mana = mana - 15
	print("")
	if mana <= 0:
		hp = hp + mana
		if hp <= 0:
			print("umarles, lamus lol")
			#wyzeruj_staty()
			time.sleep(4)
			os._exit(1)
		print("nie masz many pało niemyta lol")
		print(f"walnales bossa o {7.5 + dodatek_mag_dmg_kowal + moj_magiczny_dmg}")
		boss_hp = boss_hp - 7.5 - dodatek_mag_dmg_kowal - moj_magiczny_dmg
		mana = 0
		info_staty_boss()
	else:
		print(f"walnales bossa o {7.5 + dodatek_mag_dmg_kowal + moj_magiczny_dmg}")
		boss_hp = boss_hp - 7.5 - dodatek_mag_dmg_kowal - moj_magiczny_dmg
	rodzaj_ataku_boss = losowanie_atak_boss()
	if rodzaj_ataku_boss == "miniony":
		ilosc_dmg_miniony = (ilosc_minionow * 3) - shield
		if ilosc_dmg_miniony <= 0:
			ilosc_dmg_miniony = 0
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)

	if rodzaj_ataku_boss == "bije":
		dmg_bossa = random.randint(15, 20) - shield
		if dmg_bossa <= 0:
			dmg_bossa = 0
		hp = hp - dmg_bossa
		print(f'dostajesz wpierdol o {dmg_bossa}, zostaje ci {hp}')
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)

	if rodzaj_ataku_boss == "siada na morde":
		dmg_siad_na_morde = random.randint(2, 4)
		hp = hp - dmg_siad_na_morde
		print(f"boss siada ci na morde i dostajesz {dmg_siad_na_morde} hp, zostaje ci {hp} hp")
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)
def hazard_boss():
	 global hp, boss_hp, info_staty_boss, moj_damage, ilosc_minionow, ilosc_dmg_miniony, losowanie_atak_boss, ilosc_minionow, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia
	 print("")
	 mana = mana - 20
	 print("")
	 damage_automatu = random.randint(5, 12)
	 print(f"twoj damage to {damage_automatu}!!")
	 if mana <= 0:
	 	hp = hp + mana
	 	info_staty()
	 	print(f"nie masz many, dostajesz {mana} hp!")
	 	if hp <= 0:
	 		print("umarles, lamus lol")
	 		#wyzeruj_staty()
	 		time.sleep(4)
	 		os._exit(1)
	 	print(f"bijesz bossa o {damage_automatu + dodatek_mag_dmg_kowal + moj_magiczny_dmg}")
	 	boss_hp = boss_hp - damage_automatu - dodatek_mag_dmg_kowal - moj_magiczny_dmg
	 	mana = 0
	 	info_staty_boss()
	 else:
	 	print(f"bijesz bossa o {damage_automatu + dodatek_mag_dmg_kowal + moj_magiczny_dmg}")
	 	boss_hp = boss_hp - damage_automatu - dodatek_mag_dmg_kowal - moj_magiczny_dmg
	 	info_staty_boss()

	 rodzaj_ataku_boss = losowanie_atak_boss()
	 if rodzaj_ataku_boss == "miniony":
	 	ilosc_dmg_miniony = (ilosc_minionow * 3) - shield
	 	if ilosc_dmg_miniony <= 0:
	 		ilosc_dmg_miniony = 0
	 	hp = hp - ilosc_dmg_miniony
	 	print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
	 	info_staty_boss()
	 	time.sleep(5)

	 if rodzaj_ataku_boss == "bije":
	 	dmg_bossa = random.randint(15, 20) - shield
	 	if dmg_bossa <= 0:
	 		dmg_bossa = 0
	 	hp = hp - dmg_bossa
	 	print(f'dostajesz wpierdol o {dmg_bossa}, zostaje ci {hp}')
	 	hp = hp - ilosc_dmg_miniony
	 	print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
	 	info_staty_boss()
	 	time.sleep(5)

	 if rodzaj_ataku_boss == "siada na morde":
	 	dmg_siad_na_morde = random.randint(2, 4)
	 	hp = hp - dmg_siad_na_morde
	 	print(f"boss siada ci na morde i dostajesz {dmg_siad_na_morde} hp, zostaje ci {hp} hp")
	 	hp = hp - ilosc_dmg_miniony
	 	print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
	 	info_staty_boss()
	 	time.sleep(5)
def obrona_boss():
	global hp, boss_hp, info_staty_boss, moj_damage, ilosc_minionow, ilosc_dmg_miniony, losowanie_atak_boss, ilosc_minionow, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia
	print("")
	moj_damage_obrona = moj_damage / 2
	boss_hp = boss_hp - moj_damage_obrona - dodatek_dmg_kowal
	print(f"klepiesz go o {moj_damage_obrona + dodatek_dmg_kowal}!")

	rodzaj_ataku_boss = losowanie_atak_boss()
	if rodzaj_ataku_boss == "miniony":
		ilosc_dmg_miniony = (ilosc_minionow * 3) - shield
		if ilosc_dmg_miniony <= 0:
			ilosc_dmg_miniony = 0
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)

	if rodzaj_ataku_boss == "bije":
		dmg_bossa = random.randint(15, 20) - shield
		if dmg_bossa <= 0:
			dmg_bossa = 0
		hp = hp - dmg_bossa
		print(f'dostajesz wpierdol o {dmg_bossa}, zostaje ci {hp}')
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)

	if rodzaj_ataku_boss == "siada na morde":
		dmg_siad_na_morde = random.randint(2, 4)
		hp = hp - dmg_siad_na_morde
		print(f"boss siada ci na morde i dostajesz {dmg_siad_na_morde} hp, zostaje ci {hp} hp")
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)
def leczenie_boss():
	global hp, boss_hp, info_staty_boss, moj_damage, ilosc_minionow, ilosc_dmg_miniony, losowanie_atak_boss, ilosc_minionow, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia
	if mana >= 10:
		mana = mana - 10
		hp = hp + 3
		info_staty_boss()
		print("dostajesz 3 hp za 10 many!")
		time.sleep(3)
	else:
		print("nie masz tyle many lamusie")
		time.sleep(3)
def medytacja_boss():
	global hp, boss_hp, info_staty_boss, moj_damage, ilosc_minionow, ilosc_dmg_miniony, losowanie_atak_boss, ilosc_minionow, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia
	print("")
	dodawanie_many = random.randint(8, 12)
	print(f"medytujesz i dostajesz {dodawanie_many} many!")
	mana = mana + dodawanie_many
	rodzaj_ataku_boss = losowanie_atak_boss()
	if rodzaj_ataku_boss == "miniony":
		ilosc_dmg_miniony = (ilosc_minionow * 3) - shield
		if ilosc_dmg_miniony <= 0:
			ilosc_dmg_miniony = 0
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)

	if rodzaj_ataku_boss == "bije":
		nowy_shield = shield / 2
		dmg_bossa = random.randint(15, 20) - nowy_shield
		if dmg_bossa <= 0:
			dmg_bossa = 0
		hp = hp - dmg_bossa
		print(f'dostajesz wpierdol o {dmg_bossa}, zostaje ci {hp}')
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)

	if rodzaj_ataku_boss == "siada na morde":
		dmg_siad_na_morde = random.randint(2, 4)
		hp = hp - dmg_siad_na_morde
		print(f"boss siada ci na morde i dostajesz {dmg_siad_na_morde} hp, zostaje ci {hp} hp")
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)
def walka_wrecz_miniony():
	global hp, info_staty_boss, boss_hp, moj_damage, ilosc_minionow, ilosc_dmg_miniony, losowanie_atak_boss, ilosc_minionow, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia, obecny_item_rece, obecny_item_kule
	ilosc_minionow = round(ilosc_minionow) - round((moj_damage / 5))
	if ilosc_minionow <= 0:
		ilosc_minionow = 0
	if obecny_item_rece == "krwawe_ostrze":
		hp = hp + 1
		print("leczysz sie o 1 hp!")
		info_staty_boss()
		time.sleep(0.5)
	if obecny_item_kule == "pierscionek_slubny":
		los_mana = random.randint(2,4)
		mana = mana + los_mana
		print(f"dostajesz dodatkowo {los_mana} many!")
		info_staty_boss()
		time.sleep(0.5)
	rodzaj_ataku_boss = losowanie_atak_boss()
	if rodzaj_ataku_boss == "miniony":
		ilosc_dmg_miniony = (ilosc_minionow * 3) - shield
		if ilosc_dmg_miniony <= 0:
			ilosc_dmg_miniony = 0
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)

	if rodzaj_ataku_boss == "bije":
		dmg_bossa = random.randint(15, 20) - shield
		if dmg_bossa <= 0:
			dmg_bossa = 0
		hp = hp - dmg_bossa
		print(f'dostajesz wpierdol o {dmg_bossa}, zostaje ci {hp}')
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)

	if rodzaj_ataku_boss == "siada na morde":
		dmg_siad_na_morde = random.randint(2, 4)
		hp = hp - dmg_siad_na_morde
		print(f"boss siada ci na morde i dostajesz {dmg_siad_na_morde} hp, zostaje ci {hp} hp")
		hp = hp - ilosc_dmg_miniony
		print(f"dostajesz {ilosc_dmg_miniony} od minionow, zostaje ci {hp}")
		info_staty_boss()
		time.sleep(5)


## BOSS OGOLNE
def info_staty_boss():
		global hp, mana, shield, moj_damage, gold, obecna_lokacja, poziom_trudnosci, ilosc_minionow, potka_hp, potka_mana, potka_granat, potka_oslabienie
		ctypes.windll.kernel32.SetConsoleTitleW(f"|  hp {round(hp)}  |  mana: {round(mana)}  |  shield: {round(shield)} (+{round(dodatek_shield_kowal)})  |  damage: {round(moj_damage)} (+{round(dodatek_dmg_kowal)})  |  mag_damage: {round(moj_magiczny_dmg)} (+{round(dodatek_mag_dmg_kowal)})  |  potki: {potka_hp}/{potka_mana}/{potka_granat}/{potka_oslabienie}  |  ilosc_minionow: {round(ilosc_minionow)}  |")
def smierc_boss():
	print("zabiles bossa")
	time.sleep(5)
boss_hp = 250
def boss_fight():
	global info_staty, hp, moj_magiczny_dmg, zabezpieczenia, wyzeruj_staty, hp, smierc_boss, boss_hp, walka_wrecz_miniony, leczenie_boss, medytacja_boss, walka_wrecz_boss, kula_ognia_boss, hazard_boss, potiony_boss, obrona_boss, boss_fight, ile_razy_zwaliles, potki, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, moj_damage, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia, lootowanie, hazard, obrona, poziom_trudnosci, info_staty, wyswietl_wybory, obecny_item_rece, obecny_item_klata, obecny_item_kule, obecny_item_glowa, potka_hp, potka_mana, potka_granat, potka_oslabienie
	os.system('cls')
	time.sleep(2)
	print("wchodzisz do ciemnego pomieszczenia,")
	time.sleep(2)
	print("jedyne co widzisz, to monstrulanie wielka postac na srodku.")
	time.sleep(4)
	print('z gory splywa swiatlo,')
	time.sleep(3)
	print("wiesz, ze to twoj moment chwaly...")
	time.sleep(4)
	print("")
	while True:
		info_staty_boss()
		os.system("cls")
		walka_boss = wyswietl_wybory("atakuj bossa", "atakuj miniony", "brak", "spieradlaj (uzyj fujarke)")
		if walka_boss == "1":
			atakuj_bossa = wyswietl_wybory("walka wrecz", "magia", "obrona", "potiony")
			if atakuj_bossa == "1":
				walka_wrecz_boss()
			if atakuj_bossa == "2":
				magia_boss = wyswietl_wybory("kula ognia", "hazard", "leczenie", "medytacja")
				if magia_boss == "1":
					kula_ognia_boss()
				if magia_boss == "2":
					hazard_boss()
				if magia_boss == "3":
					leczenie_boss()
				if magia_boss == "4":
					medytacja_boss()
			if atakuj_bossa == "3":
				obrona_boss()
			if atakuj_bossa == "4":
				potiony_boss()
		if walka_boss == "2":
			walka_wrecz_miniony()
		if walka_boss == "4":
			tak_nie_spierdalanie_boss = input("spoko, na pewno? (t/n): ")
			if tak_nie_spierdalanie_boss == "t":
				print("Ok, narka")
				boss_hp = 250
				ilosc_minionow = 0
				time.sleep(2)
				break
			elif tak_nie_spierdalanie_boss == "n":
				print("ok, do boju skurwysynie")
				time.sleep(3)
		if boss_hp <= 0:
			os.system('cls')
			smierc_boss()
			break
		if hp <= 0:
			print("umarles, lamus lol")
			#wyzeruj_staty()
			time.sleep(4)
			os._exit(1)
def quick_save():
	global info_staty, hp, mana, max_mana, klasa, shield, gold, moj_damage, moj_magiczny_dmg, obecny_item_rece, obecny_item_klata, obecny_item_kule, obecny_item_glowa, poziom_trudnosci, dodatek_shield_kowal, dodatek_dmg_kowal, dodatek_mag_dmg_kowal, potka_hp, potka_mana, potka_granat, potka_oslabienie, odebrane_1, odebrane_2, odebrane_3, odebrane_4, zabezpieczenia, pokonani_wrogowie, ile_lochow_przeszedles, ile_razy_zwaliles, dur_rece, dur_kule, dur_glowa, dur_klata
	do_zapisu = {
  				"hp_jak_cos_edytujesz_to_jestes_pizda": hp,
  				"mana": mana,
  				"max_mana": max_mana,
  				"shield": shield,
  				"gold": gold,
  				"moj_damage": moj_damage,
  				"moj_magiczny_dmg": moj_magiczny_dmg,
  				"obecny_item_rece": obecny_item_rece,
  				"obecny_item_klata": obecny_item_klata,
  				"obecny_item_kule": obecny_item_kule,
  				"obecny_item_glowa": obecny_item_glowa,
  				"poziom_trudnosci": poziom_trudnosci,
  				"dodatek_dmg_kowal": dodatek_dmg_kowal,
  				"dodatek_shield_kowal": dodatek_shield_kowal,
  				"dodatek_mag_dmg_kowal": dodatek_mag_dmg_kowal,
  				"potka_hp":potka_hp,
  				"potka_mana":potka_mana,
  				"potka_granat":potka_granat,
  				"potka_oslabienie":potka_oslabienie,
  				"odebrane_1":odebrane_1,
  				"odebrane_2":odebrane_2,
  				"odebrane_3":odebrane_3,
  				"odebrane_4":odebrane_4,
  				"zabezpieczenia": zabezpieczenia,
  				"pokonani_wrogowie": pokonani_wrogowie,
  				"ile_lochow_przeszedles": ile_lochow_przeszedles,
  				"ile_razy_zwaliles": ile_razy_zwaliles,
  				"dur_rece": dur_rece,
  				"dur_kule": dur_kule,
  				"dur_klata": dur_klata,
  				"dur_glowa": dur_glowa,
  				"klasa": klasa
	}
	with open('zapis.json', 'w') as plik:
  		json.dump(do_zapisu, plik, indent=14)

## LOKACJE
def pokoj(wygeneruj_wroga, przeciwnik):
	      global info_staty, max_mana, dur_rece, dur_kule, dur_glowa, dur_klata, obecny_item_rece, obecny_item_kule, obecny_item_glowa, obecny_item_klata, hp, potiony, moj_damage, pokonani_wrogowie, losuj_syf, zabezpieczenia, wyzeruj_staty, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia, lootowanie, hazard, obrona
	      nowe_dmg_przeciwnika = 0
	      while True:
	       if dlugosc_lochow >= 0:
	        if obecny_item_rece == "brak":
	        	dodatek_dmg_kowal = 0
	        os.system('cls')
	        wygeneruj_wroga()
	        print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
	        obecna_lokacja = "lochy"
	        czy_uleczony = False
	        info_staty()
	        info_staty()
	        if wrog == "szkielet":
	        	przeciwnik(random.randint(8 + (poziom_trudnosci*2), (12 + (poziom_trudnosci*2))), random.randint(7 + (poziom_trudnosci*2), (12 + (poziom_trudnosci*2))))
	        elif wrog == "antek":
	        	przeciwnik(random.randint(4 + (poziom_trudnosci*2), (6 + (poziom_trudnosci*2))), random.randint(10 + (poziom_trudnosci*2), (16 + (poziom_trudnosci*2))))
	        elif wrog == "andrzej":
	        	przeciwnik(random.randint(11 + (poziom_trudnosci*2), (15 + (poziom_trudnosci*2))), random.randint(7 + (poziom_trudnosci*2), (10 + (poziom_trudnosci*2))))
	        elif wrog == "kurvinox":
	        	przeciwnik(random.randint(5 + (poziom_trudnosci*2), (11 + (poziom_trudnosci*2))), random.randint(6 + (poziom_trudnosci*2), (12 + (poziom_trudnosci*2))))
	        elif wrog == "cipster":
	        	przeciwnik(random.randint(5 + (poziom_trudnosci*2), (11 + (poziom_trudnosci*2))), random.randint(6 + (poziom_trudnosci*2), (12 + (poziom_trudnosci*2))))
	        elif wrog == "uczen 1 klasy technik informatyk":
	        	przeciwnik(random.randint(8 + (poziom_trudnosci*2), (13 + (poziom_trudnosci*2))), random.randint(5 + (poziom_trudnosci*2), (10 + (poziom_trudnosci*2))))
	        elif wrog == "ognisko":
	        	  przeciwnik(0, 0)
	        	  odpoczynek = False
	        elif wrog == "skrzynia":
	        	przeciwnik(0,0)
	        	skrzynia_otworzona = False



	        while True: # pętla
	        	if wrog == "szkielet" or wrog == "andrzej" or wrog == "antek" or wrog == "kurvinox" or wrog == "cipster" or wrog == "uczen 1 klasy technik informatyk":
	        		wybor_walka = wyswietl_wybory("walka wrecz", 'magia', "obrona", "potiony")
	        		if wybor_walka == "1":
	        			walka_wrecz()
	        		if wybor_walka == "2":
	        			os.system('cls')
	        			wybor_magia = wyswietl_wybory("kula ognia (-15 many)", 'magiczny drut (-20 many)', "leczenie (-20 many/+3 hp)", "medytacja (+10/15 many)")
	        			if wybor_magia == "1":
	        				kula_ognia()
	        			elif wybor_magia == "2":
	        				hazard()
	        			elif wybor_magia == "3":
	        				if czy_uleczony == False:
	        					if mana >= 20:
	        						mana = mana - 20
	        						hp = hp + 3
	        						os.system('cls')
	        						print(f"twoj wrog to {wrog}")
	        						print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
	        						info_staty()
	        						info_staty()
	        						print("dostajesz 3 hp za 20 many!")
	        						czy_uleczony = True
	        						time.sleep(3)
	        					else:
	        						print("nie masz tyle many lamusie")
	        				else:
	        					print("Juz sie uleczyles w tej walce")
	        					time.sleep(1)
	        			elif wybor_magia == "4":
	        				nowy_shield_medytacja = shield / 2
	        				nowe_dmg_przeciwnika = przeciwnik_huj['obrazenia_przeciwnik'] - nowy_shield_medytacja
	        				if nowe_dmg_przeciwnika <= 0:
	        					nowe_dmg_przeciwnika = 0
	        					hp = hp - 3
	        					print("")
	        					print("mimo ze lamus jest slaby, dostajesz lepa na morde.")
	        					print(f"dostales wpierdol o 3 hp, zostalo ci {hp}")
	        					info_staty()
	        					time.sleep(1)
	        				else:
	        					hp = hp - nowe_dmg_przeciwnika
	        					print(f"dostales wpierdol o {nowe_dmg_przeciwnika} (shield / 2) hp, zostalo ci {hp}")
	        				if hp <= 0:
	        					print("umarles, lamus lol")
	        					#wyzeruj_staty()
	        					time.sleep(4)
	        					os._exit(1)
	        				print("")
	        				dodawanie_many = random.randint(10, 15)
	        				print(f"medytujesz i dostajesz {dodawanie_many} many!")
	        				mana = mana + dodawanie_many
	        				info_staty()
	        				info_staty()
	        				time.sleep(3)
	        				os.system('cls')
	        				print(f"twoj wrog to {wrog}")
	        				print(f"pozostaly(o) {dlugosc_lochow} pokoje(i)")
	        		if wybor_walka == "3":
	        			obrona()
	        		if wybor_walka == "4":
	        			potiony()
	        		if przeciwnik_huj['hp_przeciwnik'] <= 0:
	        				obecna_lokacja = "martwy przeciwnik"
	        				pokonani_wrogowie = pokonani_wrogowie + 1
	        				info_staty()
	        				info_staty()
		        			if obecny_item_klata != "brak":
		        				dur_klata = dur_klata - 1
		        				if dur_klata <= 0:
		        					print("rozwalasz swoj item!")
		        					shield = shield - itemy[obecny_item_klata]['shield']
		        					moj_damage = moj_damage - itemy[obecny_item_klata]['dmg']
		        					moj_magiczny_dmg = moj_magiczny_dmg - itemy[obecny_item_klata]['magiczne_obrazenia']
		        					obecny_item_klata = "brak"	
		        			if obecny_item_glowa != "brak":
		        					dur_glowa = dur_glowa - 1
		        					if dur_glowa <= 0:
		        						print("rozwalasz swoj item!")
		        						shield = shield - itemy[obecny_item_glowa]['shield']
		        						moj_damage = moj_damage - itemy[obecny_item_glowa]['dmg']
		        						moj_magiczny_dmg = moj_magiczny_dmg - itemy[obecny_item_glowa]['magiczne_obrazenia']
		        						obecny_item_glowa = "brak"		
	        				lootowanie_zioma = wyswietl_wybory("lootuj", 'idz dalej', "losuj itemy", "pewny gold (1-3 + poziom_trudnosci)")
	        				if lootowanie_zioma == "1":
	        					lootowanie()
	        					dlugosc_lochow = dlugosc_lochow - 1
	        					mana = max_mana
	        					info_staty()
	        					break
	        				if lootowanie_zioma == "2":
	        					dlugosc_lochow = dlugosc_lochow - 1
	        					mana = max_mana
	        					info_staty()
	        					break
	        				if lootowanie_zioma == "3":
	        					losuj_syf()
	        					dlugosc_lochow = dlugosc_lochow - 1
	        					mana = max_mana
	        					info_staty()
	        					break
	        				if lootowanie_zioma == "4":
	        					ile_dodac = random.randint(1,3) + (poziom_trudnosci * 2)
	        					gold = gold + ile_dodac
	        					info_staty()
	        					print(f"dostajesz {ile_dodac} golda")
	        					time.sleep(2)
	        					dlugosc_lochow = dlugosc_lochow - 1
	        					mana = max_mana
	        					info_staty()
	        					break
	        				else:
	        					print("pojebalo cie? tracisz loot lol")
	        					dlugosc_lochow = dlugosc_lochow - 1
	        					mana = max_mana
	        					info_staty()
	        					time.sleep(3)
	        					break
	        	elif wrog == "ognisko":
	        		ognisko_wybor = wyswietl_wybory("odpocznij", 'idz dalej', "brak", "zabij sie")
	        		if ognisko_wybor == "1":
	        			if odpoczynek == False:
	        				odpoczynek = True
	        				ilosc_hp = random.randint(2, 4)
	        				hp = hp + ilosc_hp
	        				mana = max_mana
	        				print("odpoczywasz..")
	        				time.sleep(2)
	        				info_staty()
	        				info_staty()
	        				print(f"odzystkujesz {ilosc_hp} hp i masz full many!")
	        				time.sleep(2)
	        			else:
	        				print("juz odpoczales, idz dalej lamusie")
	        		elif ognisko_wybor == "2":
	        			dlugosc_lochow = dlugosc_lochow - 1
	        			break
	        		elif ognisko_wybor == "4":
	        			print("masz zawal")
	        			time.sleep(2)
	        			os._exit(1)

	        	elif wrog == "skrzynia":
	        		skrzynia_wybor = wyswietl_wybory("otworz", 'idz dalej', "brak", "brak")
	        		if skrzynia_wybor == "1":
	        		 if skrzynia_otworzona == False:
	        		 	skrzynia_otworzona = True
	        		 	real_czy_fake = random.randint(1,8)
	        		 	print('otwierasz skrzynie...')
	        		 	time.sleep(1)
	        		 	if real_czy_fake == 1:
	        		 		ile_hp_skrzynia = random.randint(1,4)
	        		 		print(f"skrzynia to jednak wrog i dostajesz strzala na morde o {ile_hp_skrzynia} hp!")
	        		 		hp = hp - ile_hp_skrzynia
	        		 		info_staty()
	        		 		info_staty()
	        		 		time.sleep(2)
	        		 	else:
	        		 		ile_gold_skrzynia = random.randint(2, 7)
	        		 		print(f"znajdujesz {ile_gold_skrzynia} golda!")
	        		 		gold = gold + ile_gold_skrzynia
	        		 		info_staty()
	        		 		info_staty()
	        		 		time.sleep(2)
	        		 else:
	        		 	print("juz otworzyles skrzynie, idz dalej lamusie")
	        		elif skrzynia_wybor == "2":
	        			dlugosc_lochow = dlugosc_lochow - 1
	        			mana = max_mana
	        			info_staty()
	        			break
	       else:
	        	print("skonczyles lochy")
	        	print("wiesniacy i ten skurwysyn z mlotem zorganizowali uczte na twoja czesc!!")
	        	time.sleep(3)
	        	ile_lochow_przeszedles = ile_lochow_przeszedles + 1
	        	hp = hp + 3
	        	mana = max_mana
	        	info_staty()
	        	info_staty()
	        	break
def wyzeruj_staty():
			global max_mana, klasa, dur_rece, dur_kule, dur_klata, dur_glowa, odebrane_1, odebrane_2, odebrane_3, odebrane_4, zabezpieczenia, pokonani_wrogowie, ile_lochow_przeszedles, hp, mana, shield, gold, moj_damage, moj_magiczny_dmg, obecny_item_rece, obecny_item_klata, obecny_item_kule, obecny_item_glowa, poziom_trudnosci, dodatek_shield_kowal, dodatek_dmg_kowal, dodatek_mag_dmg_kowal, potka_hp, potka_mana, potka_granat, potka_oslabienie
			do_zapisu = {"hp_jak_cos_edytujesz_to_jestes_pizda": 15,
			"mana": 30,
			"max_mana": 30,
			"shield": 10,
			"gold": 20,
			"moj_damage": 5,
			"moj_magiczny_dmg": 0,
			"obecny_item_rece": "brak",
			"obecny_item_klata": "brak",
			"obecny_item_kule": "brak",
			"obecny_item_glowa": "brak",
			"poziom_trudnosci": 0,
			"dodatek_dmg_kowal": 0,
			"dodatek_shield_kowal": 0,
			"dodatek_mag_dmg_kowal": 0,
			"potka_hp": 0,
			"potka_mana": 0,
			"potka_granat": 0,
			"potka_oslabienie": 0,
			"odebrane_1": False,
			"odebrane_2": False,
			"odebrane_3": False,
			"odebrane_4": False,
			"zabezpieczenia": 0,
			"pokonani_wrogowie": 0,
			"ile_lochow_przeszedles": 0,
			"ile_razy_zwaliles": 0,
			"dur_rece": 0,
			"dur_kule": 0,
			"dur_klata": 0,
			"dur_glowa": 0,
			"klasa": "brak"
			}
			with open('zapis.json', 'w') as plik:
				json.dump(do_zapisu, plik, indent=14)
def miasto():
	global hp, moj_magiczny_dmg, max_mana, dur_rece, dur_kule, dur_glowa, dur_klata, zabezpieczenia, ile_razy_zwaliles, potki, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, moj_damage, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia, lootowanie, hazard, obrona, poziom_trudnosci, info_staty, wyswietl_wybory, obecny_item_rece, obecny_item_klata, obecny_item_kule, obecny_item_glowa, potka_hp, potka_mana, potka_granat, potka_oslabienie
	obecna_lokacja = "miasto"
	info_staty()
	info_staty()
	wybor_miasto = wyswietl_wybory("publiczne obnazanie sie", 'sklep', "wiedzma", "kowal")
	if wybor_miasto == "1":
		ile_razy_zwaliles = ile_razy_zwaliles + 1
		print("")
		print("dopada cie gwardia")
		koszt = ile_razy_zwaliles * 4
		wybor_obnazanie = wyswietl_wybory(f"zaplać {koszt} golda", 'spierdalaj', "oddaj sie w rence wladzy", "wal dalej")
		if wybor_obnazanie == "1":
			if gold <= koszt:
				print("nie masz nawet czym zaplacic fiucie, lecisz do pierdla")
				time.sleep(10)
			else:
				gold = gold - koszt
				info_staty()
				info_staty()
		elif wybor_obnazanie == "2" or wybor_obnazanie == "3":
			print ("lapia cie i wpieradlaj do wiezienia (chwile se poczekasz kutasie)")
			time.sleep(10)
		elif wybor_obnazanie == "4":
			print ("walom cie w lep i budzisz sie w wiezieniu i do tego boli cie dupa")
			hp = hp -2
			info_staty()
			info_staty()
			time.sleep(10)
		else:
			print("probojesz spierdolic? nie tak latwo szmaciarzu")
			gold = gold - koszt - 3
			time.sleep(4)
			print(f"placisz normalne {koszt} i do tego 3 golda mandatu za probe spierdolenia")
			info_staty()
			info_staty()
			time.sleep(6)
	if wybor_miasto == "2":
	  potki_czy_itemy = input("chcesz kupic potki czy itemy? (p/i): ")
	  if potki_czy_itemy == "i":
  	  	if obecna_lokacja == "miasto":
  	  		obecna_lokacja = "sklep"
  	  		info_staty()
  	  		info_staty()
  	  		numer_itemu = 0
  	  		print("perscionek slubny jest magiczny, tak samo jak krwawe ostrze!!")
  	  		print("")
  	  		print("------------------------------------------------------------------")
  	  		print("ID | NAME                 | DMG | SHIELD | MAG_DMG | GOLD | SLOT")
  	  		print("------------------------------------------------------------------")
  	  		#for item in itemy:
  	  			#print(f"{itemy[item]['nr']}. {item}  |  {itemy[item]['dmg']} DMG  |  {itemy[item]['shield']} SHIELD  |  {itemy[item]['magiczne_obrazenia']}  MAG_DMG  |  {itemy[item]['cena_buy']} GOLDA  |")
  	  		for item in itemy:
  	  			print(f"{itemy[item]['nr']:<2} | {item:<20} | {itemy[item]['dmg']:<3} | {itemy[item]['shield']:<6} | {itemy[item]['magiczne_obrazenia']:<7} | {itemy[item]['cena_buy']:<4} | {itemy[item]['slot']:<6}")
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
  	  								na_jaki_slot = itemy[item]['slot'] # glowa, rece, kule, klata
  	  								if na_jaki_slot == "rece":
  	  									dur_rece = 200
  	  									if obecny_item_rece == "brak":
  	  										obecny_item_rece = item
  	  										gold = gold - itemy[item]['cena_buy']
  	  										shield = shield + itemy[item]['shield']
  	  										moj_damage = moj_damage + itemy[item]['dmg']
  	  										moj_magiczny_dmg = moj_magiczny_dmg + itemy[item]['magiczne_obrazenia']
  	  										info_staty()
  	  										info_staty()
  	  										print(f"dodano {itemy[item]['shield']} SH i {itemy[item]['dmg']} DMG")
  	  										print("")
  	  										input("kliknij cokolwiek aby kontynuowac")
  	  									else:
  	  										shield = shield - itemy[obecny_item_rece]['shield']
  	  										moj_damage = moj_damage - itemy[obecny_item_rece]['dmg']
  	  										moj_magiczny_dmg = moj_magiczny_dmg - itemy[obecny_item_rece]['magiczne_obrazenia']
  	  										obecny_item_rece = item
  	  										gold = gold - itemy[item]['cena_buy']
  	  										shield = shield + itemy[item]['shield']
  	  										moj_damage = moj_damage + itemy[item]['dmg']
  	  										moj_magiczny_dmg = moj_magiczny_dmg + itemy[item]['magiczne_obrazenia']
  	  								elif na_jaki_slot == "glowa":
  	  									dur_glowa = 150
  	  									if obecny_item_glowa == "brak":
  	  										obecny_item_glowa = item
  	  										gold = gold - itemy[item]['cena_buy']
  	  										shield = shield + itemy[item]['shield']
  	  										moj_damage = moj_damage + itemy[item]['dmg']
  	  										moj_magiczny_dmg = moj_magiczny_dmg + itemy[item]['magiczne_obrazenia']
  	  										info_staty()
  	  										info_staty()
  	  										print(f"dodano {itemy[item]['shield']} SH i {itemy[item]['dmg']} DMG")
  	  										print("")
  	  										input("kliknij cokolwiek aby kontynuowac")
  	  									else:
  	  										shield = shield - itemy[obecny_item_glowa]['shield']
  	  										moj_damage = moj_damage - itemy[obecny_item_glowa]['dmg']
  	  										moj_magiczny_dmg = moj_magiczny_dmg - itemy[obecny_item_glowa]['magiczne_obrazenia']
  	  										obecny_item_glowa = item
  	  										gold = gold - itemy[item]['cena_buy']
  	  										shield = shield + itemy[item]['shield']
  	  										moj_damage = moj_damage + itemy[item]['dmg']
  	  										moj_magiczny_dmg = moj_magiczny_dmg + itemy[item]['magiczne_obrazenia']
  	  								elif na_jaki_slot == "kule":
  	  									dur_kule = 250
  	  									if obecny_item_kule == "brak":
  	  										if itemy[item]['nr'] != "21":
  	  											obecny_item_kule = item
  	  											gold = gold - itemy[item]['cena_buy']
  	  											shield = shield + itemy[item]['shield']
  	  											moj_damage = moj_damage + itemy[item]['dmg']
  	  											moj_magiczny_dmg = moj_magiczny_dmg + itemy[item]['magiczne_obrazenia']
  	  											info_staty()
  	  											info_staty()
  	  											print(f"dodano {itemy[item]['shield']} SH i {itemy[item]['dmg']} DMG")
  	  											print("")
  	  											input("kliknij cokolwiek aby kontynuowac")
  	  										else:
  	  											h_cipk = input("nie tak latwo, haslo dla cipka poprosze: ")
  	  											## szukasz hasla co nie? spierdalaj, kup cos normalnego a nie cipka xd

  	  											if h_cipk == "dupadupa":
  	  												print("Oki, cipek jest twoj ;3")
  	  												obecny_item_kule = item
  	  												gold = gold - itemy[item]['cena_buy']
  	  												shield = shield + itemy[item]['shield']
  	  												moj_damage = moj_damage + itemy[item]['dmg']
  	  												moj_magiczny_dmg = moj_magiczny_dmg + itemy[item]['magiczne_obrazenia']
  	  												info_staty()
  	  												info_staty()
  	  												print(f"dodano {itemy[item]['shield']} SH i {itemy[item]['dmg']} DMG")
  	  												print("")
  	  												input("kliknij cokolwiek aby kontynuowac")
  	  									else:
  	  										shield = shield - itemy[obecny_item_kule]['shield']
  	  										moj_damage = moj_damage - itemy[obecny_item_kule]['dmg']
  	  										moj_magiczny_dmg = moj_magiczny_dmg - itemy[obecny_item_kule]['magiczne_obrazenia']
  	  										obecny_item_kule = item
  	  										gold = gold - itemy[item]['cena_buy']
  	  										shield = shield + itemy[item]['shield']
  	  										moj_damage = moj_damage + itemy[item]['dmg']
  	  										moj_magiczny_dmg = moj_magiczny_dmg + itemy[item]['magiczne_obrazenia']
  	  								elif na_jaki_slot == "klata":
  	  									dur_klata = 150
  	  									if obecny_item_klata == "brak":
  	  										obecny_item_klata = item
  	  										gold = gold - itemy[item]['cena_buy']
  	  										shield = shield + itemy[item]['shield']
  	  										moj_damage = moj_damage + itemy[item]['dmg']
  	  										moj_magiczny_dmg = moj_magiczny_dmg + itemy[item]['magiczne_obrazenia']
  	  										info_staty()
  	  										info_staty()
  	  										print(f"dodano {itemy[item]['shield']} SH i {itemy[item]['dmg']} DMG")
  	  										print("")
  	  										input("kliknij cokolwiek aby kontynuowac")
  	  									else:
  	  										shield = shield - itemy[obecny_item_klata]['shield']
  	  										moj_magiczny_dmg = moj_magiczny_dmg - itemy[obecny_item_klata]['magiczne_obrazenia']
  	  										moj_damage = moj_damage - itemy[obecny_item_klata]['dmg']
  	  										obecny_item_klata = item
  	  										gold = gold - itemy[item]['cena_buy']
  	  										shield = shield + itemy[item]['shield']
  	  										moj_damage = moj_damage + itemy[item]['dmg']
  	  										moj_magiczny_dmg = moj_magiczny_dmg + itemy[item]['magiczne_obrazenia']
  	  							else:
  	  								print("idz zarob kutasie krzywy")
  	  								print("")
  	  								input("kliknij cokolwiek aby kontynuowac")
  	  						elif tak_nie_kupno == "n":
  	  							print("zdecyduj sie maly kurwiu")
  	  							print("")
  	  							input("kliknij cokolwiek aby kontynuowac")
	  elif potki_czy_itemy == "p":
  	  		print("-----------------------------------------------")
  	  		print("ID | NAME                 | HP | MANA | GOLD ")
  	  		print("-----------------------------------------------")
  	  		for potka in potki:
  	  			print(f"{potki[potka]['nr']:<2} | {potka:<20} | {potki[potka]['hp']:<2} | {potki[potka]['mana']:<4} | {potki[potka]['cena_buy']:<4}")
  	  		wybrany_item_potka = input("wybierz item (numer): ")
  	  		for potka in potki:
  	  			for staty in potki[potka]:
  	  				if staty == "nr":
  	  					if potki[potka]['nr'] == wybrany_item_potka:
  	  						print(f"wybrales {potka}!")
  	  						tak_nie_kupno = input(f"czy chcesz go kupic za {potki[potka]['cena_buy']}? Zostanie ci {gold - potki[potka]['cena_buy']} (t/n): ")
  	  						if tak_nie_kupno == "t":
  	  							if gold >= potki[potka]['cena_buy']:
  	  								if potki[potka]['nr'] == "1":
  	  									potka_hp = potka_hp + 1
  	  									gold = gold - potki[potka]['cena_buy']
  	  									info_staty()
  	  									info_staty()
  	  								elif potki[potka]['nr'] == "2":
  	  									potka_mana = potka_mana + 1
  	  									gold = gold - potki[potka]['cena_buy']
  	  									info_staty()
  	  									info_staty()
  	  								elif potki[potka]['nr'] == "3":
  	  									potka_granat = potka_granat + 1
  	  									gold = gold - potki[potka]['cena_buy']
  	  									info_staty()
  	  									info_staty()
  	  								elif potki[potka]['nr'] == "4":
  	  									potka_oslabienie = potka_oslabienie + 1
  	  									gold = gold - potki[potka]['cena_buy']
  	  									info_staty()
  	  									info_staty()
  	  								info_staty()
  	  								info_staty()
  	  								print(f"masz teraz {potka_hp} potek_hp, {potka_mana} potek_many, {potka_granat} potek_granat i {potka_oslabienie} potek_oslabienie")
  	  								print("")
  	  								print("kliknij ckokolwiek aby kontynuowac")
  	  								input()
  	  							else:
  	  								print("idz zarob kutasie krzywy")
  	  								print("")
  	  								input("kliknij cokolwiek aby kontynuowac")
  	  						elif tak_nie_kupno == "n":
  	  							print("zdecyduj sie maly kurwiu")
  	  							print("")
  	  							input("kliknij cokolwiek aby kontynuowac")
	if wybor_miasto == "3":
  	  if obecna_lokacja == "miasto":
  	  	os.system('cls')
  	  	obecna_lokacja = "wiedzma"
  	  	print("")
  	  	print(f"dodanie 1 dmg kosztuje {13 + round(float(poziom_trudnosci))*2} golda")
  	  	print(f"dodanie 1 shielda kosztuje {19 + round(float(poziom_trudnosci))*2} golda")
  	  	print(f"dodanie 1 max_many kosztuje {8 + round(float(poziom_trudnosci))*2} golda")
  	  	print(f"dodanie 1 hp kosztuje {5 + round(float(poziom_trudnosci))*2} golda ")
  	  	print("")
  	  	wiedzma_wybor = wyswietl_wybory("wiekszy dmg", "wiekszy shield", "dodanie many", "dodanie hp")
  	  	if wiedzma_wybor == "1":
  	  		kup_dmg_ilosc = input("Ile chcesz dodatkowego dmg?: ")
  	  		mnoznik = 12 + float(poziom_trudnosci)*2
  	  		cena_dmg_kup = abs(float(kup_dmg_ilosc)) * mnoznik
  	  		tak_czy_nie_dmg = input(f"czy chcesz kupic {abs(round(float(kup_dmg_ilosc)))} dmg za {abs(round(float(cena_dmg_kup)))} golda? (t/n): ")
  	  		if gold >= cena_dmg_kup:
  	  			if kup_dmg_ilosc.isdigit() == True:
  	  				if tak_czy_nie_dmg == "t":
  	  					gold = abs(round(gold)) - abs(round(cena_dmg_kup))
  	  					moj_damage = abs(round(float(moj_damage))) + abs(round(float(kup_dmg_ilosc)))
  	  					info_staty()
  	  					info_staty()
  	  					print(f"masz teraz {moj_damage} dmg")
  	  					print("")
  	  					input("kliknij cokolwiek aby kontynuowac")
  	  				elif tak_czy_nie_dmg == "n":
  	  					print('namyśl sie kurwa')
  	  					print("")
  	  					input("kliknij cokolwiek aby kontynuowac")
  	  			else:
  	  				print("liczbe calkowita prosze ;3")
  	  				time.sleep(3)
  	  		else:
  	  			print("nie stac cie palo niemyta")
  	  			print("")
  	  			input("kliknij cokolwiek aby kontynuowac")
  	  	if wiedzma_wybor == "2":
  	  		kup_shield_ilosc = input("Ile chcesz dodatkowego shielda?: ")
  	  		mnoznik = 15 + float(poziom_trudnosci)*2
  	  		cena_shield_kup = abs(float(kup_shield_ilosc)) * mnoznik
  	  		tak_czy_nie_shield = input(f"czy chcesz kupic {abs(round(float(kup_shield_ilosc)))} shield za {abs(round(float(cena_shield_kup)))} golda? (t/n): ")
  	  		if gold >= cena_shield_kup:
  	  			if kup_shield_ilosc.isdigit() == True:
  	  				if tak_czy_nie_shield == "t":
  	  					gold = abs(round(gold)) - abs(round(cena_shield_kup))
  	  					shield = abs(round(float(shield))) + abs(round(float(kup_shield_ilosc)))
  	  					info_staty()
  	  					info_staty()
  	  					print(f"masz teraz {shield} shielda")
  	  					print("")
  	  					input("kliknij cokolwiek aby kontynuowac")
  	  				elif tak_czy_nie_shield == "n":
  	  					print('namyśl sie kurwa')
  	  					print("")
  	  					input("kliknij cokolwiek aby kontynuowac")
  	  			else:
  	  				print("liczbe calkowita prosze ;3")
  	  				time.sleep(4)
  	  		else:
  	  			print("nie stac cie palo niemyta")
  	  			print("")
  	  			input("kliknij cokolwiek aby kontynuowac")
  	  	if wiedzma_wybor == "3":
  	  		kup_mana_ilosc = input("Ile chcesz dodatkowej max_many?: ")
  	  		mnoznik = 1 + float(poziom_trudnosci)*2
  	  		cena_mana_kup = abs(float(kup_mana_ilosc)) * mnoznik
  	  		tak_czy_nie_mana = input(f"czy chcesz kupic {abs(round(float(kup_mana_ilosc)))} max_many za {abs(round(float(cena_mana_kup)))} golda? (t/n): ")
  	  		if gold >= cena_mana_kup:
  	  			if kup_mana_ilosc.isdigit() == True:
  	  				if tak_czy_nie_mana == "t":
  	  					gold = abs(round(gold)) - abs(round(cena_mana_kup))
  	  					max_mana = abs(round(float(max_mana))) + abs(round(float(kup_mana_ilosc)))
  	  					info_staty()
  	  					info_staty()
  	  					print(f"masz teraz {max_mana} max_many")
  	  					print("")
  	  					input("kliknij cokolwiek aby kontynuowac")
  	  				elif tak_czy_nie_mana == "n":
  	  					print('namyśl sie kurwa')
  	  					print("")
  	  					input("kliknij cokolwiek aby kontynuowac")
  	  			else:
  	  				print("liczbe calkowita prosze ;3")
  	  				time.sleep(4)
  	  		else:
  	  			print("nie stac cie palo niemyta")
  	  			print("")
  	  			input("kliknij cokolwiek aby kontynuowac")
  	  	if wiedzma_wybor == "4":
  	  		kup_hp_ilosc = input("Ile chcesz dodatkowego hp?: ")
  	  		mnoznik = 5 + float(poziom_trudnosci)*2
  	  		cena_hp_kup = abs(float(kup_hp_ilosc)) * mnoznik
  	  		tak_czy_nie_hp = input(f"czy chcesz kupic {abs(round(float(kup_hp_ilosc)))} hp za {abs(round(float(cena_hp_kup)))} golda? (t/n): ")
  	  		if gold >= cena_hp_kup:
  	  			if kup_hp_ilosc.isdigit() == True:
  	  				if tak_czy_nie_hp == "t":
  	  					gold = abs(round(gold)) - abs(round(cena_hp_kup))
  	  					hp = abs(round(float(hp))) + abs(round(float(kup_hp_ilosc)))
  	  					info_staty()
  	  					info_staty()
  	  					print(f"masz teraz {hp} hp")
  	  					print("")
  	  					input("kliknij cokolwiek aby kontynuowac")
  	  				elif tak_czy_nie_hp == "n":
  	  					print('namyśl sie kurwa')
  	  					print("")
  	  					input("kliknij cokolwiek aby kontynuowac")
  	  			else:
  	  				print("liczbe calkowita prosze ;3")
  	  				time.sleep(4)
  	  		else:
  	  			print("nie stac cie palo niemyta")
  	  			print("")
  	  			input("kliknij cokolwiek aby kontynuowac")
	if wybor_miasto == "4":
	 try:
  	  if obecna_lokacja == "miasto":
  	  	os.system('cls')
  	  	obecna_lokacja = "skurwysyn z mlotem"
  	  	print("")
  	  	print(f"dodanie 1 dmg kosztuje {8 + round(float(poziom_trudnosci))*2} golda")
  	  	print(f"dodanie 1 shielda kosztuje {12 + round(float(poziom_trudnosci))*2} golda")
  	  	print(f"dodanie 1 magicznego dmg kosztuje {4 + round(float(poziom_trudnosci))*2} golda")
  	  	print(f"uwaga: nie isc do kowala bez broni bo ci sprzeda lepe")
  	  	print(f"kowal ulepsza tylko przedmiot w rece")
  	  	print("")
  	  	kowal_wybor = wyswietl_wybory("wiekszy dmg", "wiekszy shield", "wiekszy magiczny dmg", "kup zabezpieczenia na itemy")
  	  	if kowal_wybor == "1":
  	  			kup_dmg_ilosc = input("Ile chcesz dodatkowego dmg?: ")
  	  			mnoznik = 8 + float(poziom_trudnosci)*2
  	  			cena_dmg_kup = abs(float(kup_dmg_ilosc)) * mnoznik
  	  			tak_czy_nie_dmg = input(f"czy chcesz dodac {abs(round(float(kup_dmg_ilosc)))} dmg do broni za {abs(round(float(cena_dmg_kup)))} golda? (t/n): ")
  	  			if gold >= cena_dmg_kup:
  	  				if kup_dmg_ilosc.isdigit() == True:
  	  					if tak_czy_nie_dmg == "t":
  	  						if obecny_item_rece != "brak":
  	  							gold = abs(round(gold)) - abs(round(cena_dmg_kup))
  	  							dodatek_dmg_kowal = abs(round(float(dodatek_dmg_kowal))) + abs(round(float(kup_dmg_ilosc)))
  	  							info_staty()
  	  							info_staty()
  	  							print(f"masz teraz {dodatek_dmg_kowal} dodatkowego dmg w broni")
  	  							print("")
  	  							input("kliknij cokolwiek aby kontynuowac")
  	  						else:
  	  							hp = hp - 2
  	  							info_staty()
  	  							info_staty()
  	  							print("kowal wali ci mlotem po lapach, mowilem zeby nie ulepszac golych rak cepie")
  	  							print("")
  	  							input("kliknij cokolwiek aby kontynuowac")
  	  					elif tak_czy_nie_dmg == "n":
  	  						print('namyśl sie palo')
  	  						print("")
  	  						input("kliknij cokolwiek aby kontynuowac")
  	  				else:
  	  					print("liczbe calkowita prosze ;3")
  	  					time.sleep(3)
  	  			else:
  	  				print("nie stac cie palo niemyta")
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  	if kowal_wybor == "2":
  	  		kup_shield_ilosc = input("Ile chcesz dodatkowego shielda?: ")
  	  		mnoznik = 12 + float(poziom_trudnosci)*2
  	  		cena_shield_kup = abs(float(kup_shield_ilosc)) * mnoznik
  	  		tak_czy_nie_shield = input(f"czy chcesz kupic {abs(round(float(kup_shield_ilosc)))} za {abs(round(float(cena_shield_kup)))} golda? (t/n): ")
  	  		if gold >= cena_shield_kup:

  	  			if tak_czy_nie_shield == "t":
  	  				if kup_shield_ilosc.isdigit() == True:
  	  					if obecny_item_rece != "brak":
  	  						gold = abs(round(gold)) - abs(round(cena_shield_kup))
  	  						dodatek_shield_kowal = abs(round(float(dodatek_shield_kowal))) + abs(round(float(kup_shield_ilosc)))
  	  						info_staty()
  	  						info_staty()
  	  						print(f"masz teraz {dodatek_shield_kowal} dodatkowego shielda do broni!")
  	  						print("")
  	  						input("kliknij cokolwiek aby kontynuowac")
  	  					else:
  	  						hp = hp - 2
  	  						info_staty()
  	  						info_staty()
  	  						print("kowal wali ci mlotem po lapach, mowilem zeby nie ulepszac golych dloni cepie")
  	  						print("")
  	  						input("kliknij cokolwiek aby kontynuowac")
  	  				else:
  	  					print("liczbe calkowita prosze ;3")
  	  					time.sleep(3)
  	  			elif tak_czy_nie_shield == "n":
  	  				print('namyśl sie kurwa')
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
  	  		else:
  	  			print("nie stac cie palo niemyta")
  	  			print("")
  	  			input("kliknij cokolwiek aby kontynuowac")
  	  	if kowal_wybor == "3":
  	  		kup_magicznydmg_ilosc = input("Ile chcesz dodatkowego magicznego dmg?: ")
  	  		mnoznik = 4 + float(poziom_trudnosci)*2
  	  		cena_mag_dmg_kup = abs(float(kup_magicznydmg_ilosc)) * mnoznik
  	  		tak_czy_nie_shield = input(f"czy chcesz kupic {abs(round(float(kup_magicznydmg_ilosc)))} magicznego dmg za {abs(round(float(cena_mag_dmg_kup)))} golda? (t/n): ")
  	  		if gold >= cena_mag_dmg_kup:
  	  			if tak_czy_nie_shield == "t":
  	  				if obecny_item_rece != "brak":
  	  					if kup_magicznydmg_ilosc.isdigit() == True:
  	  						gold = abs(round(gold)) - abs(round(cena_mag_dmg_kup))
  	  						dodatek_mag_dmg_kowal = abs(round(float(dodatek_mag_dmg_kowal))) + abs(round(float(kup_magicznydmg_ilosc)))
  	  						info_staty()
  	  						info_staty()
  	  						print(f"masz teraz {dodatek_mag_dmg_kowal} dodatkowego magicznego damage do broni!")
  	  						print("")
  	  						input("kliknij cokolwiek aby kontynuowac")
  	  					else:
  	  						print("liczbe calkowita prosze ;3")
  	  						time.sleep(3)
  	  				else:
  	  					hp = hp - 2
  	  					info_staty()
  	  					info_staty()
  	  					print("kowal wali ci mlotem po lapach, mowilem zeby nie ulepszac golych dloni cepie")
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
  	  	if kowal_wybor == "4":
  	  			print("zabezpieczenia chronia przed zniszczeniem itemu (i sie zuzywaja) (20g/szt)")
  	  			kup_zabez_ilosc = input("Ile chcesz zabezpieczen?: ")
  	  			mnoznik = 20 + float(poziom_trudnosci)*2
  	  			cena_zabez_kup = abs(float(kup_zabez_ilosc)) * mnoznik
  	  			tak_czy_nie_dmg = input(f"czy chcesz kupic {abs(round(float(kup_zabez_ilosc)))} zabezpieczen za {abs(round(float(cena_zabez_kup)))} golda? (t/n): ")
  	  			if gold >= cena_zabez_kup:
  	  				if kup_zabez_ilosc.isdigit() == True:
  	  					if tak_czy_nie_dmg == "t":
  	  						gold = abs(round(gold)) - abs(round(cena_zabez_kup))
  	  						zabezpieczenia = abs(round(float(zabezpieczenia))) + abs(round(float(kup_zabez_ilosc)))
  	  						info_staty()
  	  						info_staty()
  	  						print(f"masz teraz {zabezpieczenia} zabezpieczen(ie)(ia)")
  	  						print("")
  	  						input("kliknij cokolwiek aby kontynuowac")
  	  					elif tak_czy_nie_dmg == "n":
  	  						print('namyśl sie palo')
  	  						print("")
  	  						input("kliknij cokolwiek aby kontynuowac")
  	  				else:
  	  					print("liczbe calkowita prosze ;3")
  	  					time.sleep(3)
  	  			else:
  	  				print("nie stac cie palo niemyta")
  	  				print("")
  	  				input("kliknij cokolwiek aby kontynuowac")
	 except ValueError:
	 	print("ty kurwa masz liczbe wpisac debilu")
	 	time.sleep(3)
	 except:
	 	pass
def zamek():
	global info_staty, odebrane_1, odebrane_2, odebrane_3, odebrane_4, quick_save, hp, ile_razy_zwaliles, potka_hp, pokonani_wrogowie, moj_magiczny_dmg, boss_fight, ile_razy_zwaliles, potki, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, moj_damage, wrog, obecna_lokacja, dlugosc_lochow, mana, shield, gold, ile_lochow_przeszedles, poziom_trudnosci, itemy, dodatek_dmg_kowal, dodatek_shield_kowal, dodatek_mag_dmg_kowal, walka_wrecz, kula_ognia, lootowanie, hazard, obrona, poziom_trudnosci, info_staty, wyswietl_wybory, obecny_item_rece, obecny_item_klata, obecny_item_kule, obecny_item_glowa, potka_hp, potka_mana, potka_granat, potka_oslabienie
	obecna_lokacja == "zamek"
	info_staty()
	info_staty()
	wybor_zamek = wyswietl_wybory("boss fight", "KKK (komnata krula kazika)", "HAZARD !!!", "brak")
	if wybor_zamek == "1":
		print("król zbiera wojowników z okolicznych miast do walki z wielkim skurwysynem.")
		print("tylko najsilniejsi sa w stanie go pokonac.")
		print("krol daje ci czarodziejska fujarke, dzieki ktorej mozesz spierdolic z miejsca walki w kazdym momencie.")
		print("")
		print("koszt wejscia na arene to 10 golda.")
		walka_boss_tak_nie = input("musisz przejsc 5 lochow (poziom_trudnosci 2) zeby zawalczyc z bossem, chcesz przejsc do walki? (t/n): ")
		if walka_boss_tak_nie == "t":
			if poziom_trudnosci >= 2:
				if gold < 10:
					print("nawet cie nie stac, nie jestes gotowy, spierdalaj")
					time.sleep(3)
				else:
					gold = gold - 10
					info_staty()
					info_staty()
					boss_fight()
			elif poziom_trudnosci < 2:
				print("jestes leszczem lol")
				time.sleep(3)
		elif walka_boss_tak_nie == "n":
			print("ok, przygotuj sie")
			time.sleep(2)
	if wybor_zamek == "2":
		wybor_krol = wyswietl_wybory("odbierz nagrode za 50 shielda", "odbierz nagrode za 250 mobow", "odbierz nagrode za 40 damage", 'odbierz nagrode za duza ilosc wykroczen seksualnych')
		if wybor_krol == "1":
			if odebrane_1 == False:
				if shield >= 50:
					print("gratuluje takiego wyniku maly skurwysynie! oto twoja nagroda")
					print(f"dostajesz 111 golda")
					gold = gold + 111
					info_staty()
					info_staty()
					odebrane_1 = True
					time.sleep(7)
				else:
					print("jak smiesz truc mi dupe! musisz zostac ukarany!!")
					time.sleep(2)
					hp = hp - 1
					info_staty()
					info_staty()
					print("krol strasznie laduje cie w dupe i dosiega ci wątroby. (obrazenia wewnetrzne)")
					print("")
					input("kliknij cokolwiek by pogodzic sie z tym faktem")
			else:
				print('odebrales juz, idz se')
				time.sleep(3)

		if wybor_krol == "2":
			if odebrane_2 == False:
				if pokonani_wrogowie >= 250:
					print("dobra robota maly kurwiu!! oto twoja nagroda")
					print("krol cie poblogoslawil")
					print("dostajesz 69 hp")
					hp = hp + 69
					odebrane_2 = True
					info_staty()
					info_staty()
					time.sleep(7)
				else:
					print("jak smiesz truc mi dupe kutasie")
					print("krol wysysa z ciebie resztki twojej marnej duszy")
					print("tracisz troche many")
					mana = mana - 8
					info_staty()
					info_staty()
					print("")
					input("kliknij cokolwiek by pogodzic sie z tym faktem")
			else:
				print("odebrales juz, idz se")
				time.sleep(3)
		if wybor_krol == "3":
			if odebrane_3 == False:
				if moj_damage >= 40:
					print("gratuluje takiego osiagniecia nygusie")
					print("dostajesz troche many!!")
					mana = mana + 200
					info_staty()
					info_staty()
					odebrane_3 = True
				else:
					print("nie truj mi dupy nygusie")
					print("idz se zanim ci cos zrobie ")
					time.sleep(2)
			else:
				print("odebrales juz, idz se")
				time.sleep(3)
		if wybor_krol == "4":
			if odebrane_4 == False:
				if ile_razy_zwaliles >= 10:
					print("masz tu kilka 5 na hp zeby fiut ci sie zregenerowal troche, podziwiam")
					potka_hp = potka_hp + 5
					info_staty()
					info_staty()
					odebrane_4 = True
					time.sleep(7)
				else:
					print("zbyt malo zwalone jest twoje pracie!")
					time.sleep(4)
			else:
				print("fiut zwalony kolego, idz stad.")
				time.sleep(3)
	if wybor_zamek == "3":
		wybor_gra = wyswietl_wybory("ruletka", "coinflip", "automaty (;3)", "czarny jacek")
		if wybor_gra == '1':
			print("")
			print("ruletka!")
			wybor_kolor = wyswietl_wybory("czarny (x2)", "czerwony (x2)", "zielony (x14)", "brak")
			if wybor_kolor == "1":
				kwota = input("ile chcesz postawic na czarny?: ")
				kwota = abs(int(kwota))
				info_staty()
				info_staty()
				if gold >= kwota:
					gold = gold - kwota
					wylosowany = random.randint(1, 25)
					if wylosowany == 1:
						print("zielony!")
						time.sleep(3)
						quick_save()
					elif 2 <= wylosowany <= 13:
						los2 = random.randint(1,2)
						if los2 == 2:
							print("czarny!")
							print(f"wygrywasz {kwota*2} golda!")
							gold = gold + (kwota*2)
							info_staty()
							info_staty()
						elif los2 == 1:
							print("czerwony!")
							quick_save()
						time.sleep(3)

					if 14 <= wylosowany <= 25:
						print("czerwony!")
						quick_save()
						time.sleep(3)

					#time.sleep(3)
				else:
					print("nie stac cie fiucie")
					time.sleep(2)
			if wybor_kolor == "2":
				kwota = input("ile chcesz postawic na czerwony?: ")
				kwota = abs(int(kwota))
				info_staty()
				info_staty()
				if gold >= kwota:
					gold = gold - kwota
					wylosowany = random.randint(1, 25)
					if wylosowany == 1:
						print("zielony!")
						quick_save()
					elif 2 <= wylosowany <= 13:
						print("czarny!")
						quick_save()
					elif 14 <= wylosowany <= 25:
						los2 = random.randint(1,2)
						if los2 == 2:
							print("czerwony!")
							print(f"wygrywasz {kwota*2} golda!")
							gold = gold + (kwota*2)
							info_staty()
							info_staty()
						elif los2 == 1:
							print("czarny!")
							quick_save()
					time.sleep(3)
				else:
					print("nie stac cie fiucie")
					time.sleep(2)
			if wybor_kolor == "3":
				kwota = input("ile chcesz postawic na zielony?: ")
				kwota = abs(int(kwota))
				info_staty()
				info_staty()
				if gold >= kwota:
					gold = gold - kwota
					wylosowany = random.randint(1, 25)
					if wylosowany == 1:
						print("zielony!")
						print(f"wygrywasz {kwota*14} golda! gratki kutasie")
						gold = gold + (kwota*14)
						info_staty()
						info_staty()
						time.sleep(4)
					elif 2 <= wylosowany <= 13:
						print("czarny!")
						quick_save()
					if 14 <= wylosowany <= 25:
						print("czerwony!")
						quick_save()
					time.sleep(3)
				else:
					print("nie stac cie fiucie")
					time.sleep(2)
		if wybor_gra == "2":
			print("")
			print("coinflip!")
			wybor_rzut = wyswietl_wybory("orzel", "reszka", "brak", "brak")
			if wybor_rzut == "1":
				kwota = input("ile chcesz postawic na orla?: ")
				kwota = abs(int(kwota))
				info_staty()
				info_staty()
				if gold >= kwota:
					gold = gold - kwota
					wylosowany = random.randint(1, 3)
					if wylosowany == 1 or wylosowany == 3:
						print("reszka!")
						quick_save()
					elif wylosowany == 2:
						print("orzel!")
						print(f"wygrywasz {kwota*2} golda!")
						gold = gold + (kwota*2)
						info_staty()
						info_staty()
					time.sleep(3)
				else:
					print("nie stac cie fiucie")
					time.sleep(2)
			if wybor_rzut == "2":
				kwota = input("ile chcesz postawic na reszke?: ")
				kwota = abs(int(kwota))
				info_staty()
				info_staty()
				if gold >= kwota:
					gold = gold - kwota
					wylosowany = random.randint(1, 3)
					if wylosowany == 1 or wylosowany == 3:
						print("orzel!")
						quick_save()
					elif wylosowany == 2:
						print("reszka!")
						print(f"wygrywasz {kwota*2} golda!")
						gold = gold + (kwota*2)
						info_staty()
						info_staty()
					time.sleep(3)
				else:
					print("nie stac cie fiucie")
					time.sleep(2)
		if wybor_gra == "3":
			print("")
			print("witaj w maszynce pieniedzy!!")
			print("koszt wejscia to 5 golda! pamietaj ze kasyno to organizacja charytatywna.")
			wybor_automat = wyswietl_wybory("gold master", "johnny bravo (staty)", "brak", "brak")
			if wybor_automat == "1":
				while True:
					graj_czy_nie = input("graj albo wyjdz (g,w): ")
					if graj_czy_nie == "g":
						if gold >= 5:
							gold = gold - 5
							info_staty()
							numerek = random.randint(1, 1200)
							if 1 <= numerek <= 5: # 0.5%
								dodawanie = random.randint(45, 58)
								print(f"BIG WIN WYGREYWASZ {dodawanie} GOLDA !!!!!!!!!!!!!!!!!!!!")
								gold = gold + dodawanie 
								info_staty()	
							elif 6 <= numerek <= 15: # 1%
								dodawanie = random.randint(8, 12)
								print(f"wygrywasz {dodawanie} golda!")
								gold = gold + dodawanie 
								info_staty()	
							elif 16 <= numerek <= 65: # 5%
								dodawanie = random.randint(1, 7)
								print(f"wygrywasz {dodawanie} golda!")
								gold = gold + dodawanie 
								info_staty()	
							elif 66 <= numerek <= 75: # 1%
								dodawanie = random.randint(15, 40)
								print(f"JACKTOP !!!!!  wygrywasz {dodawanie} golda!")
								gold = gold + dodawanie 
								info_staty()	
							elif 76 <= numerek <= 85: # 1%
								dodawanie = random.randint(25, 40)
								print(f"JACEK GARNEK  wygrywasz {dodawanie} golda!")
								gold = gold + dodawanie 
								info_staty()	
							elif 86 <= numerek <= 95: # 1%
								dodawanie = random.randint(7, 13)
								print(f"wygrywasz {dodawanie} golda!")
								gold = gold + dodawanie 
								info_staty()	
							elif 96 <= numerek <= 105: # 1%
								dodawanie = random.randint(10, 12)
								print(f"wygrywasz {dodawanie} golda!")
								gold = gold + dodawanie 
								info_staty()	
							elif 106 <= numerek <= 205: # 10%
								print(f"wygrywasz ale w kasynie wysetpuje blad techniczny i kasyno wyplaca tylko polowe sory")
								dodawanie = random.randint(1, 2)
								gold = gold + dodawanie
								info_staty()
								time.sleep(2)
							elif 206 <= numerek <= 245:  # 4%
								dodawanie = random.randint(25, 35)
								print(f"DUZA WYGRANA WYGRYWASZ {dodawanie} golda!")
								gold = gold + dodawanie 
								info_staty()	
							elif 246 <= numerek <= 1000: # 50%
								print("nie wygrywasz nic, ale nie poddawaj sie")
								quick_save()
							elif 1001 <= numerek <= 1200: # 25.5%
								dodawanie = random.randint(2, 4)
								print(f"wygrywasz {dodawanie} golda!")
								gold = gold + dodawanie 
								info_staty()
							time.sleep(2)
						else:
							print("NIE STAC CIE NA AUTOMATY wez pozyczke ok")
							time.sleep(2)
					elif graj_czy_nie == "w":
						break
			if wybor_automat == "2":
				while True:
					graj_czy_nie = input("graj albo wyjdz (50/50) (g,w): ")
					if graj_czy_nie == "g":
						losowanie_lista = ["hp", "shield", "dmg", 'magiczny_dmg']
						wylosowana_stata = random.choice(losowanie_lista)
						print(f"losujesz {wylosowana_stata}!")
						if wylosowana_stata == "hp":
							hp = hp - 1
							losuj = random.randint(1, 4)
							if losuj == 1:
								hp = hp + 2
								print("dostajesz 1hp!")
							if losuj == 2 or losuj == 3 or losuj == 4:
								print("chuja dostajesz xd")
								quick_save()
							info_staty()
							info_staty()
							time.sleep(2)
						if wylosowana_stata == "shield":
							shield = shield - 1
							losuj = random.randint(1, 4)
							if losuj == 1:
								shield = shield + 2
								print("dostajesz 1sh!")
							if losuj == 2 or losuj == 3 or losuj == 4:
								print("chuja dostajesz xd")
								quick_save()
							info_staty()
							info_staty()
							time.sleep(2)
						if wylosowana_stata == "dmg":
							moj_damage = moj_damage - 1
							losuj = random.randint(1, 4)
							if losuj == 1:
								moj_damage = moj_damage + 2
								print("dostajesz 1dmg!")
							if losuj == 2 or losuj == 3 or losuj == 4:
								print("chuja dostajesz xd")
								quick_save()
							info_staty()
							info_staty()
							time.sleep(2)
						if wylosowana_stata == "magiczny_dmg":
							moj_magiczny_dmg = moj_magiczny_dmg - 1
							losuj = random.randint(1, 4)
							if losuj == 1:
								moj_magiczny_dmg = moj_magiczny_dmg + 2
								print("dostajesz 1mag_dmg!")
							if losuj == 2 or losuj == 3 or losuj == 4:
								print("chuja dostajesz xd")
								quick_save()
							info_staty()
							info_staty()
							time.sleep(2)
					elif graj_czy_nie == "w":
						break
		if wybor_gra == "4":
			print("")
			print("czarny jacek!!!")
			print("zasady znasz nygusie.")
			obstawa = input("ile obstawiasz?: ")
			obstawa = abs(int(obstawa))
			if gold >= obstawa:
				gold = gold - obstawa
				karta1 = random.randint(2, 11)
				karta2 = random.randint(2, 11)
				suma = karta1 + karta2
				while True:
					if karta1 == 11 and karta2 == 11:
						print("masz 2 asy wygryawsz z automatu")
						gold = gold + (obstawa*2)
						info_staty()
						info_staty()
						time.sleep(2)
						break
					dobieranie = input(f"twoja suma kart to ({suma}), dobierasz? (t/n): ")
					if dobieranie == "t":
						dobrano = random.randint(2, 11)
						suma = suma + dobrano
						print(f"dobrales {dobrano}")
						if suma > 21:
							print("przejebales xd")
							quick_save()
							time.sleep(2)
							break
						print(f"masz teraz {suma}")
					if dobieranie == "n":
						print(f"masz lacznie {suma}")
						time.sleep(1)
						suma_wroga = random.randint(17, 23)
						if suma_wroga > 21:
							print(f"twoj wrog ma {suma_wroga}, przy czym przepierdala ture, wygrywasz")
							gold = gold + (obstawa*2)
							info_staty()
							info_staty()
							time.sleep(2)
							break
						else:
							print(f"twoj wrog ma {suma_wroga}, a ty {suma}.")
							if suma > suma_wroga:
								print("wygrywasz!!!")
								gold = gold + (obstawa*2)
							if suma < suma_wroga:
								print("przegrywasz")
								quick_save()
							if suma == suma_wroga:
								print("remis.")
								gold = gold + obstawa
							time.sleep(2)
							break



			else:
				print("nie stac cie na hazard lamusie")
				time.sleep(2)







# POCZATEK
if __name__ == "__main__":
	if klasa == "brak":
		print('wybierz klase postaci nygusie maly platfusie')
		klasa_wybor = wyswietl_wybory("andrzej", "antek", "czarodziej", "zlodziej")
		if klasa_wybor == "1":
			print("wybierasz andrzeja!")
			print("hp +7")
			hp = hp + 7
			klasa = "andrzej"
			info_staty()
		if klasa_wybor == "2":
			print("wybierasz antka!")
			print("dmg +1")
			moj_damage = moj_damage + 1
			klasa = "antek"
			info_staty()
		if klasa_wybor == "3":
			print('wybierasz czarodzieja')
			print("max_mana +5  mag_damage +1")
			max_mana = max_mana + 5
			moj_magiczny_dmg = moj_magiczny_dmg + 1
			klasa = "czarodziej"
			info_staty()
		if klasa_wybor == "4":
			print("wybierasz zlodzieja")
			print("gold +10")
			gold = gold + 10
			klasa = "zlodziej"
			info_staty()
		time.sleep(2)
	while True:
	 try:
	  os.system('cls')
	  obecna_lokacja = "lonka"
	  info_staty()
	  info_staty()
	  print("u wiedzmy dodajesz staty do postaci (nie stracisz ich)")
	  print("u kowala dodajesz staty do broni (mozesz je stracic)")
	  print("jesli chcesz sie cofnac w jakims wyborze, kliknij enter bez wpisywania liczby")
	  if hp <= 0:
	  	os._exit(1)
	  wybor_lonka = wyswietl_wybory("lochy (wejscie 5 golda)", 'idz do miasta', "zamek", "zapis/reset")
	  if wybor_lonka == "1" or wybor_lonka == "2" or wybor_lonka == "3" or wybor_lonka == "4":
	  	if wybor_lonka == "1":
	  	  if obecna_lokacja == "lonka":
	  	  	obecna_lokacja = "lochy"
	
	  	  	if ile_lochow_przeszedles >= 2:
	  	  		poziom_trudnosci = 1
	  	  	if ile_lochow_przeszedles >= 5:
	  	  		poziom_trudnosci = 2
	  	  	if ile_lochow_przeszedles >= 8:
	  	  		poziom_trudnosci = 3
	  	  	if ile_lochow_przeszedles >= 12:
	  	  		poziom_trudnosci = 4
	  	  	if ile_lochow_przeszedles >= 16:
	  	  		poziom_trudnosci = 5
	  	  	if ile_lochow_przeszedles >= 21:
	  	  		poziom_trudnosci = 6
	  	  	if ile_lochow_przeszedles >= 26:
	  	  		poziom_trudnosci = 7
	  	  	if ile_lochow_przeszedles >= 32:
	  	  		poziom_trudnosci = 8
	  	  	if ile_lochow_przeszedles >= 36:
	  	  		poziom_trudnosci = 9
	  	  	if ile_lochow_przeszedles >= 42:
	  	  		poziom_trudnosci = 10
	  	  	if ile_lochow_przeszedles >= 47:
	  	  		poziom_trudnosci = 11
	  	  	if ile_lochow_przeszedles >= 51:
	  	  		poziom_trudnosci = 12
	  	  	if ile_lochow_przeszedles >= 56:
	  	  		poziom_trudnosci = 13
	  	  	if ile_lochow_przeszedles >= 62:
	  	  		poziom_trudnosci = 14
	  	  	if ile_lochow_przeszedles >= 69:
	  	  		poziom_trudnosci = 15
	  	  	if ile_lochow_przeszedles >= 74:
	  	  		poziom_trudnosci = 16
	  	  	if ile_lochow_przeszedles >= 80:
	  	  		poziom_trudnosci = 17
	  	  	if ile_lochow_przeszedles >= 85:
	  	  		poziom_trudnosci = 18
	  	  	if ile_lochow_przeszedles >= 90:
	  	  		poziom_trudnosci = 19
	  	  	if ile_lochow_przeszedles >= 95:
	  	  		poziom_trudnosci = 20
	  	  	if ile_lochow_przeszedles >= 100:
	  	  		poziom_trudnosci = 21
	  	  	if ile_lochow_przeszedles >= 105:
	  	  		poziom_trudnosci = 22
	  	  	if ile_lochow_przeszedles >= 110:
	  	  		poziom_trudnosci = 23
	  	  	if ile_lochow_przeszedles >= 115:
	  	  		poziom_trudnosci = 24
	  	  	if ile_lochow_przeszedles >= 120:
	  	  		poziom_trudnosci = 25
	  	  	if ile_lochow_przeszedles >= 125:
	  	  		poziom_trudnosci = 26
	  	  	if ile_lochow_przeszedles >= 130:
	  	  		poziom_trudnosci = 27
	  	  	if ile_lochow_przeszedles >= 135:
	  	  		poziom_trudnosci = 28
	  	  	if ile_lochow_przeszedles >= 140:
	  	  		poziom_trudnosci = 29
	  	  	if ile_lochow_przeszedles >= 145:
	  	  		poziom_trudnosci = 30
	  	  	gold = gold - 5
	  	  	os.system('cls')
	  	  	info_staty()
	  	  	info_staty()
	  	  	wybor_lochy = wyswietl_wybory("idz przed siebie", 'zawroc', "brak", "brak")
	  	  	losowanie_dlugosc_lochow = random.randint(6, 8)
	
	  	  	dlugosc_lochow = losowanie_dlugosc_lochow + (poziom_trudnosci * 2)
	  	  	if wybor_lochy == "1":
	  	  		os.system('cls')
	  	  		obecna_lokacja = "walka"
	  	  		info_staty()
	  	  		info_staty()
	  	  		pokoj(wygeneruj_wroga, przeciwnik)
	  	  	if wybor_lochy == "2":
	  	  	  if obecna_lokacja == "lochy":
	  	  	  	print("spierdalasz i tracisz golda lol")
	  	if wybor_lonka == "2":
	  	  	if obecna_lokacja == "lonka":
	  	  		miasto()
	  	if wybor_lonka == "3":
	  		zamek()
	  	if wybor_lonka == "4":
	  		reset_czy_zapis = input("chcesz zapisac czy resetowac staty (enter by cofnac) (z/r): ")
	  		if reset_czy_zapis == "z":
	  			tak_czy_nie_zapis = input("czy na pewno chcesz zapisac? koszt to 5 golda (t/n): ")
	  			if tak_czy_nie_zapis == "t":
	  				print("zapisywanie...")
	  				gold = gold - 5
	  				do_zapisu = {
	  				"hp_jak_cos_edytujesz_to_jestes_pizda": hp,
	  				"mana": mana,
	  				"max_mana": max_mana,
	  				"shield": shield,
	  				"gold": gold,
	  				"moj_damage": moj_damage,
	  				"moj_magiczny_dmg": moj_magiczny_dmg,
	  				"obecny_item_rece": obecny_item_rece,
	  				"obecny_item_klata": obecny_item_klata,
	  				"obecny_item_kule": obecny_item_kule,
	  				"obecny_item_glowa": obecny_item_glowa,
	  				"poziom_trudnosci": poziom_trudnosci,
	  				"dodatek_dmg_kowal": dodatek_dmg_kowal,
	  				"dodatek_shield_kowal": dodatek_shield_kowal,
	  				"dodatek_mag_dmg_kowal": dodatek_mag_dmg_kowal,
	  				"potka_hp":potka_hp,
	  				"potka_mana":potka_mana,
	  				"potka_granat":potka_granat,
	  				"potka_oslabienie":potka_oslabienie,
	  				"odebrane_1":odebrane_1,
	  				"odebrane_2":odebrane_2,
	  				"odebrane_3":odebrane_3,
	  				"odebrane_4":odebrane_4,
	  				"zabezpieczenia": zabezpieczenia,
	  				"pokonani_wrogowie": pokonani_wrogowie,
	  				"ile_lochow_przeszedles": ile_lochow_przeszedles,
	  				"ile_razy_zwaliles": ile_razy_zwaliles,
	  				"dur_rece": dur_rece,
	  				"dur_kule": dur_kule,
	  				"dur_klata": dur_klata,
	  				"dur_glowa": dur_glowa,
	  				"klasa": klasa
	  				}
	  				with open('zapis.json', 'w') as plik:
	  					json.dump(do_zapisu, plik, indent=14)
	  			elif tak_czy_nie_zapis == "n":
	  				print("ok")
	  				time.sleep(2)
	  		elif reset_czy_zapis == "r":
	  			tak_czy_nie_resetowanie = input("na pewno? stracisz wszystko (t/n): ")
	  			if tak_czy_nie_resetowanie == "t":
	  				wyzeruj_staty()
	  				print("ok, wlacz gre ponownie")
	  				time.sleep(2)
	  				os._exit(1)
	  			else:
	  				print("ok")
	  				time.sleep(2)
	
	  else:
	  	print("jestes niedogrzany?")
	 except KeyboardInterrupt:
	 	print("\nspoko, spierdalaj")
	 	time.sleep(2)
	 	break
	 except:
	 	pass
	