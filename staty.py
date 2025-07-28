import json, time, os, time
from colorama import Fore, Back, Style
import threading

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

def wyswietl_staty():
	global itemy
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

	
print("czcionke i wielkosc mozna zwiekszyc klikajac prawym na cmd, i wlasciwosci !!")
print("prosze nie zamykac okna ze statami podczas gry ;D")
print("podczas gdy tabelka ze statystykami ci mryga, sproboj nie grac na szkolnym komputrze ktory nie wyrabia ;3 (minimalne wymagania to 16GB ramu i RTX4090)")
print("")
print("kliknij cokolwiek by kontyunowac")
input()
with open('nie_usuwac.txt', 'r') as x:
	data = x.read()
wyswietl_staty()
while True:
	time.sleep(.3)
	with open('nie_usuwac.txt', 'r') as x:
		data = x.read()
	if data == "t":
		wyswietl_staty()
		with open('nie_usuwac.txt', 'w') as x:
			x.write('n')

def dupa():
	global wyswietl_staty
	while True:
		time.sleep(1)
		wyswietl_staty()
		print("ok")
p1 = threading.Thread(target=dupa)
p1.start()