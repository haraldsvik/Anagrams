# Kodeoppgave

Oppgaven er å lage en kodesnutt i Python, koden skal lese inn en av de vedlagte filene, population.txt eller population.parquet.   
Disse filene inneholder en rekke med navn.  Koden skal så finne alle anagrammene i filen. 

  

  

## Må krav:

Koden skal ikke skille mellom store og små bokstaver og koden skal skrive ut alle ord som er anagrammer av hverandre på en linje, ord som er identiske, duplikater skal ikke tas med. 

En linje for hvert anagram.  
Navn som ikke har anagrammer i listen, skal ikke tas med.   
  
F.eks. hvis file inneholder, Erik, Kire, Lars, Lasr, Erik, Knut, så skal det skrives ut:  
erik, kire  
lars, lasr

  

Koden skal være effektivt og skal kunne håndtere store datasett. Du bør velge riktige datastrukturer og algoritmer for å sikre at implementeringen er effektiv.

## Andre ønsker: 
Det er ønskelig at du

-    Dokumentere den Big O-effektiviteten til algoritmen i koden din.

-    Skrive et testskript som bruker unittest-modulen for å verifisere at implementeringen er korrekt og effektiv. Testskriptet bør også varsle eller mislykkes hvis implementeringen ikke er effektiv nok.

Vennligst inkluder tekstfilen med listen over navn og testskriptet i innleveringen.

# Evalueringskriterier

Følgende kriterier vil bli brukt for å evaluere løsningen din:

- Korrekthet: Finner implementeringen de riktige anagrammene?  
- Effektivitet: Er implementeringen effektiv nok til å håndtere store datasett?  
- Kodekvalitet: Er koden ren, lesbar og godt dokumentert?  
- Big O-analyse: Dokumenterte implementeringen den store O-effektiviteten til algoritmen i koden?  
- Testing: Gir testskriptet tilstrekkelig dekning og oppdager feil eller ineffektive løsninger?