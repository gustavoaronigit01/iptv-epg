from datetime import datetime, timedelta, timezone

hoje = datetime.now(timezone.utc).strftime("%Y%m%d")
amanha = (datetime.now(timezone.utc) + timedelta(days=1)).strftime("%Y%m%d")
depois = (datetime.now(timezone.utc) + timedelta(days=2)).strftime("%Y%m%d")

xml_content = f"""<?xml version='1.0' encoding='UTF-8'?>
<tv generator-info-name="custom-de">
  <channel id="atv.de"><display-name>A.TV</display-name></channel>
  <channel id="allgaeutv.de"><display-name>ALLGÄU-TV</display-name></channel>
  <channel id="badentv.de"><display-name>BADEN TV</display-name></channel>
  <channel id="76666"><display-name>münchen.tv</display-name></channel>
  <channel id="nbydeggendorf.de"><display-name>NIEDERBAYERN TV DEGGENDORF STRAUBING</display-name></channel>
  <channel id="nbylandshut.de"><display-name>NIEDERBAYERN TV LANDSHUT</display-name></channel>
  <channel id="nbypassau.de"><display-name>NIEDERBAYERN TV PASSAU</display-name></channel>
  <channel id="regiotvbodensee.de"><display-name>REGIO TV BODENSEE</display-name></channel>
  <channel id="regiotvstuttgart.de"><display-name>REGIO TV STUTTGART</display-name></channel>
  <channel id="rfo.de"><display-name>RFO</display-name></channel>
  <channel id="tva.de"><display-name>TVA</display-name></channel>

  <!-- münchen.tv -->
  <programme channel="76666" start="{hoje}120000 +0000" stop="{hoje}150000 +0000"><title>Die Sprechstunde / Stammtisch</title></programme>
  <programme channel="76666" start="{hoje}150000 +0000" stop="{hoje}170000 +0000"><title>Lejeune / Helden der Gleise</title></programme>
  <programme channel="76666" start="{hoje}170000 +0000" stop="{hoje}190000 +0000"><title>münchen heute</title></programme>
  <programme channel="76666" start="{hoje}190000 +0000" stop="{hoje}210000 +0000"><title>münchen heute / Sport Arena</title></programme>
  <programme channel="76666" start="{hoje}210000 +0000" stop="{amanha}060000 +0000"><title>Die Sprechstunde / münchen heute (Wh.)</title></programme>
  <programme channel="76666" start="{amanha}060000 +0000" stop="{amanha}120000 +0000"><title>Wetterpanorama / Bayerische Landfrauen</title></programme>
  <programme channel="76666" start="{amanha}120000 +0000" stop="{amanha}180000 +0000"><title>Wirtschaftstreff Bayern / Sokrates Club</title></programme>
  <programme channel="76666" start="{amanha}180000 +0000" stop="{depois}000000 +0000"><title>münchen heute / Bayern Agenda</title></programme>

  <!-- A.TV (Augsburg) -->
  <programme channel="atv.de" start="{hoje}110000 +0000" stop="{hoje}170000 +0000"><title>Zwischen Alpen und Donau / Segmüller Kochclub</title></programme>
  <programme channel="atv.de" start="{hoje}170000 +0000" stop="{hoje}230000 +0000"><title>a.tv Aktuell / Heimatzeit</title></programme>
  <programme channel="atv.de" start="{hoje}230000 +0000" stop="{amanha}170000 +0000"><title>a.tv Aktuell (Wh.) / Regionalmagazin</title></programme>
  <programme channel="atv.de" start="{amanha}170000 +0000" stop="{depois}000000 +0000"><title>a.tv Aktuell / Am Puls</title></programme>

  <!-- ALLGÄU-TV -->
  <programme channel="allgaeutv.de" start="{hoje}110000 +0000" stop="{hoje}170000 +0000"><title>allgäu.tv Magazin / Wochenrückblick (Wh.)</title></programme>
  <programme channel="allgaeutv.de" start="{hoje}170000 +0000" stop="{hoje}230000 +0000"><title>allgäu.tv Nachrichten / Allgäu Aktuell</title></programme>
  <programme channel="allgaeutv.de" start="{hoje}230000 +0000" stop="{amanha}170000 +0000"><title>allgäu.tv Nachrichten (Wh.)</title></programme>
  <programme channel="allgaeutv.de" start="{amanha}170000 +0000" stop="{depois}000000 +0000"><title>allgäu.tv Nachrichten / Allgäu Aktuell</title></programme>

  <!-- BADEN TV -->
  <programme channel="badentv.de" start="{hoje}110000 +0000" stop="{hoje}170000 +0000"><title>Baden TV Magazin / Tagesprogramm</title></programme>
  <programme channel="badentv.de" start="{hoje}170000 +0000" stop="{hoje}230000 +0000"><title>Baden TV Aktuell</title></programme>
  <programme channel="badentv.de" start="{hoje}230000 +0000" stop="{amanha}170000 +0000"><title>Baden TV Aktuell (Wh.)</title></programme>
  <programme channel="badentv.de" start="{amanha}170000 +0000" stop="{depois}000000 +0000"><title>Baden TV Aktuell</title></programme>

  <!-- NIEDERBAYERN TV (Deggendorf, Landshut, Passau) -->
  <programme channel="nbydeggendorf.de" start="{hoje}110000 +0000" stop="{hoje}170000 +0000"><title>Niederbayern TV Magazin</title></programme>
  <programme channel="nbydeggendorf.de" start="{hoje}170000 +0000" stop="{amanha}170000 +0000"><title>Niederbayern TV Journal Deggendorf-Straubing</title></programme>
  <programme channel="nbydeggendorf.de" start="{amanha}170000 +0000" stop="{depois}000000 +0000"><title>Niederbayern TV Journal Deggendorf-Straubing</title></programme>

  <programme channel="nbylandshut.de" start="{hoje}110000 +0000" stop="{hoje}170000 +0000"><title>Niederbayern TV Magazin</title></programme>
  <programme channel="nbylandshut.de" start="{hoje}170000 +0000" stop="{amanha}170000 +0000"><title>Niederbayern TV Journal Landshut</title></programme>
  <programme channel="nbylandshut.de" start="{amanha}170000 +0000" stop="{depois}000000 +0000"><title>Niederbayern TV Journal Landshut</title></programme>

  <programme channel="nbypassau.de" start="{hoje}110000 +0000" stop="{hoje}170000 +0000"><title>Niederbayern TV Magazin</title></programme>
  <programme channel="nbypassau.de" start="{hoje}170000 +0000" stop="{amanha}170000 +0000"><title>Niederbayern TV Journal Passau</title></programme>
  <programme channel="nbypassau.de" start="{amanha}170000 +0000" stop="{depois}000000 +0000"><title>Niederbayern TV Journal Passau</title></programme>

  <!-- REGIO TV (Bodensee & Stuttgart) -->
  <programme channel="regiotvbodensee.de" start="{hoje}110000 +0000" stop="{hoje}170000 +0000"><title>Regio TV Bodensee Magazin</title></programme>
  <programme channel="regiotvbodensee.de" start="{hoje}170000 +0000" stop="{amanha}170000 +0000"><title>Das Journal Bodensee</title></programme>
  <programme channel="regiotvbodensee.de" start="{amanha}170000 +0000" stop="{depois}000000 +0000"><title>Das Journal Bodensee</title></programme>

  <programme channel="regiotvstuttgart.de" start="{hoje}110000 +0000" stop="{hoje}170000 +0000"><title>Regio TV Stuttgart Magazin</title></programme>
  <programme channel="regiotvstuttgart.de" start="{hoje}170000 +0000" stop="{amanha}170000 +0000"><title>Das Journal Stuttgart</title></programme>
  <programme channel="regiotvstuttgart.de" start="{amanha}170000 +0000" stop="{depois}000000 +0000"><title>Das Journal Stuttgart</title></programme>

  <!-- RFO & TVA -->
  <programme channel="rfo.de" start="{hoje}110000 +0000" stop="{hoje}170000 +0000"><title>rfo Süd Leben / Süd Menschen</title></programme>
  <programme channel="rfo.de" start="{hoje}170000 +0000" stop="{amanha}170000 +0000"><title>rfo Süd Journal / Regio-Magazin</title></programme>
  <programme channel="rfo.de" start="{amanha}170000 +0000" stop="{depois}000000 +0000"><title>rfo Süd Journal / Regio-Magazin</title></programme>

  <programme channel="tva.de" start="{hoje}110000 +0000" stop="{hoje}170000 +0000"><title>TVA Horizonte / Ostbayern Magazin</title></programme>
  <programme channel="tva.de" start="{hoje}170000 +0000" stop="{amanha}170000 +0000"><title>TVA Journal / Labertaler Sportstudio</title></programme>
  <programme channel="tva.de" start="{amanha}170000 +0000" stop="{depois}000000 +0000"><title>TVA Journal / Ostbayern Aktuell</title></programme>
</tv>
"""

with open("epg.xml", "w", encoding="utf-8") as f:
    f.write(xml_content)
