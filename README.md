# Beste ....

## TODO

- [ ] Design states (written)
  - [x] Vind de Schoenen
  - [x] Steek de weg over
  - [x] Door het Riool
  - [ ] Final
- [ ] 3D design
  - [x] Vind de Schoenen
    - [x] Schoenen
    - [x] Knoppen
  - [x] Steek de weg over
  - [x] Door het Riool
    - [x] Riool
    - [x] Ladder
    - [x] Cijferslot
  - [ ] Final
- [ ] Coding
  - [ ] Sounds with SD Card
    - [ ] Speech
    - [ ] Shoe Scene
    - [ ] Street Scene
    - [x] Sewer Scene
    - [ ] Final Scene
  - [ ] Stages
    - [x] Shoe Scene
    - [x] Street Scene
    - [x] Sewer Scene
    - [ ] Final Scene
  - [ ] Final
- [ ] Electronics
  - [x] Mainbord -> ESP32 + SD Card
  - [x] Create Speaker + Amplifier
  - [x] Front control board
  - [x] Shoe Light
  - [x] Street Matrix
  - [x] Riool lights
  - [ ] Finale
- [ ] Painting
- [ ] Test
- [ ] Finalize

## Intro Text :loudspeaker:

> Het is weer zo ver BLA BLA BLA Laten we beginnen: er moet een route afgelegd worden maar deze zal niet zonder obstakels zijn! **Muhahahahahaha**
> De niet nader genoemde postbode heeft een pakketje voor je, echter er zijn wat problemen onderweg. Daardoor heb ik een missie voor je: Red het pakketje en je zal beloond worden.`

## States

---

### Vind de schoenen :shoe:

- #### Achtergond:
  - :musical_note: snel liedje
- #### Scenario:
  - :loudspeaker: `Voordat het pad afgelegd kan worden moet je goede schoenen hebben. Verkrijg de schoenen en de zoektocht kan verder gaan`
- #### Hardware:
  - Ledstrip onder de weg
  - 2 knoppen aan de zijkant
- #### Todo:
  - Rennen ==> druk de knop op zijkant zeer snel in.
  - als het te langzaam is dan error en moet je opnieuw beginnen
- #### Uitkomst:
  - :musical_note: walking
  - :zzz: Sleep 5 seconden
  - :bulb: **Schoenen worden belicht**

---

### Steek de weg over :walking:

- #### Achtergond:
  - :musical_note: Rijdende auto's
- #### Scenario:
  - :loudspeaker: `Nu je goede schoenen hebt kan de zoektocht voortgezet worden`
  - :musical_note: voetstappen
  - :zzz: Sleep 5 seconden
  - :bulb: **pad verlicht naar Weg**
  - :loudspeaker: `Ow nee.. helemaal vergeten, het is spits! Om de zoektocht verder te zetten moeten we de weg oversteken....`
- #### Hardware::
  - Led matrix die de weg met auto's simuleren
  - 3 knoppen
- #### Todo:
  - pijltjes gebruiken om over te steken.
- #### Uitkomst:
  - :bulb: Weg gaat **groen pulseren**

---

### Door het Riool :potable_water:

- #### Achtergrond:
  - :musical_note: Druipend water
- #### Scenario:
  - :loudspeaker: `Mission update: er zijn sporen gevonden in het riool. Betreed het Riool en zoek verder`
  - :zzz: Sleep 1 seconden
  - :bulb: **riool licht aan**
  - :musical_note: water voetstappen
  - :zzz: Sleep 5 seconden
  - :loudspeaker: `De uigang wordt geblokkeerd door een deur met een cijferslot! ontcijfer het om verder te kunnen`
- #### Hardware:
  - Ledjes Riool
  - Segment display of LCD
  - 2 knoppen (+ enter misschien)
- #### Todo:
  - Code kraken.
  - er zijjn hints te vekrijgen over het bord of via de text
- #### Uitkomst:
  - **Segment slaat op hol**
  - :bulb: Riool aan de andere kant wordt **belicht**
  - :zzz: Sleep 2 seconden
  - :bulb: Ingang riool **gaat uit**

---

### Finale :checkered_flag:

- #### Achtergond:
  - :musical_note:
- #### Scenario:
- #### Hardware:
- #### Todo:
