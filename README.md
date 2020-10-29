# Beste ....

## TODO

- [ ] Design states (writen)
  - [x] Vind de Schoenen
  - [x] Steek de weg over
  - [ ] Tripwire
  - [x] Door het Riool
  - [ ] Final
- [ ] 3D design
  - [ ] Vind de Schoenen
  - [ ] Steek de weg over
  - [ ] Tripwire
  - [ ] Door het Riool
  - [ ] Final
- [ ] Electronics
  - [ ] Mainbord -> ESP32 + SD Card
  - [ ] Front control board
  - [ ] Shoe Light
  - [ ] Water Matrix
  - [ ] Tripwire lasers
  - [ ] Riool lichten
  - [ ] Finale
- [ ] Painting
- [ ] Test
- [ ] Finalize

## Intro Text

> Het is weer zo ver BLA BLA BLA` Laten we beginnen: er moet een route afgelegd worden maar deze zal niet zonder obstakels zijn! **Muhahahahahaha**`
> De niet nader genoemde postbode heeft een pakketje voor je, echter er zijn wat problemen onderweg. Daardoor heb ik een missie voor je: Red het pakketje en je zal beloond worden.`

## States

---

### Vind de schoenen :shoe:

- #### Achtergond:
  - :musical_note: \_snel liedje\*
- #### Scenario:
  - `Voordat het pad afgelegd kan worden moet je goede schoenen hebben. Verkrijg de schoenen en de zoektocht kan verder gaan`
- #### Hardware:
  - Ledstrip onder de weg
  - 2 knoppen aan de zijkant
- #### Todo:
  - Rennen ==> druk de knop op zijkant zeer snel in.
  - als het te langzaam is dan error en moet je opnieuw beginnen
- #### Uitkomst:
  - :musical_note: \_walking\*
  - **Schoenen worden belicht**

---

### Steek de weg over :walking:

- #### Achtergond:
  - :musical_note: \_Rijdende auto's\*
- #### Scenario:
  - `Nu je goede schoenen hebt kan de zoektocht voortgezet worden`
  - :musical_note: \_voetstappen\* voor 5 seconden ==> **pad verlicht naar Weg**
  - `Ow nee.. helemaal vergeten, het is spits! Om de zoektocht verder te zetten moeten we de weg oversteken....`
- #### Hardware:
  - Led matrix die de weg met auto's simuleren
  - 3 knoppen
- #### Todo:
  - pijltjes gebruiken om over te steken.
- #### Uitkomst:
  - Weg gaat **groen pulseren**

---

### Tripwires ==> (title) :flashlight:

- #### Achtergond:
  - :musical_note: \_Mission impossible\*
- #### Scenario:
- #### Hardware:
- #### Todo:

---

### Door het Riool :potable_water:

- #### Achtergrond:
  - :musical_note: \_Druipend water\*
- #### Scenario:
  - `Mission update: er zijn sporen gevonden in het riool. Betreed het Riool en zoek verder`
  - Sleep 1 seconden
  - **riool licht aan**
  - :musical_note: \_water voetstappen\* voor 5 seconden
  - `De uigang wordt geblokkeerd door een deur met een cijferslot! ontcijfer het om verder te kunnen`
- #### Hardware:
  - Ledjes Riool
  - Segment display of LCD
  - 2 knoppen (+ enter misschien)
- #### Todo:
  - Code kraken.
  - er zijjn hints te vekrijgen over het bord of via de text
- #### Uitkomst:
  - **Segment slaat op hol**
  - Riool aan de andere kant wordt **belicht**
  - Ingang riool **gaat uit**

---

### Finale :checkered_flag:

- #### Achtergond:
  - :musical_note: \*\*
- #### Scenario:
- #### Hardware:
- #### Todo:
