# -*- coding: utf-8 -*-

# ...

  import os
  import json
  import cgi
  from incl.xmlator_ankiety import *

  for nazwa_pliku in pliki_src:
    if os.path.isfile(katalog_obf+nazwa_pliku):
      pliki[nazwa_pliku] = katalog_obf+nazwa_pliku
    else:
      pliki[nazwa_pliku] = katalog_src+nazwa_pliku

  nazwa_skryptu = os.path.basename(__file__).split('.')[0]

  dane_klienta = pobierz_dane_klienta()

  lancuch_zapytania = os.getenv("QUERY_STRING")

  if "n" in lancuch_zapytania:
    ajax_wlaczony = False
  else:
    ajax_wlaczony = True

# ...
