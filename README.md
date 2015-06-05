[![Stories in Ready](https://badge.waffle.io/Jassob/DNollK.se.png?label=ready&title=Ready)](https://waffle.io/Jassob/DNollK.se)
DNollK.se
====================
DNollK Chalmers hemsida
-------------------
Detta kommer till slut, i sinom tid, kanske, förhoppningsvis bli en hemsida som är klar före jul.
Absolut göttigast hade vart att ha den klar till mottagningen 2015.

Detta är den Python-specifika branchen av detta repo.

Det finns en del olika branches man kan titta på om man känner för det, men det är troligen denna som kommer bli den färdiga sidan till slut.

 * php-old till  DNollK '14s sida
 * design till en ren html/css implementation av designen
 * ruby till en eventuell ruby/sinatra/rails-implementation
 * haskell till en eventuell haskell/yesod-implementation
 * python till en eventuell python/django-implementation
 
## Python / Django ##
Detta projekt bygger på ramverket Django [(djangoproject.com)](http://djangoproject.com), och om man är ny på detta ramverk så finns en jättebra tutorial (som jag använt mig av till typ 90% av tiden då jag pysslat med sidan) på [docs.djangoproject.com](http://docs.djangoproject.com/en), under tutorials.

### Komma igång ###
#### Installera Python och Django ####
För att komma igång med detta projekt måste man ha Python och Django installerade. Om man använder Linux så borde Python finnas i pakethanteraren och i så fall är det bara installera genom pakethanteraren. Django (och andra python-bibliotek) kan man installera med Pythons egna pakethanterare, 'pip' (eller easy_install, men det har jag inte använt så jag kommer inte täcka det) och det gör man genom att skriva:

    $ pip install django

För att se att django blivit installerats ordentligt kan man köra python i en terminal och skriva:

    >>> import django
    >>> print(django.get_version())

Om du inte får något tråkigt felmeddelande så har du nu installerat django och är redo att komma igång!

#### Konfigurera DNollK.se ####
Nu när allt är installerat så är det bara att klona (eller ladda ner) projektet och lägga i någon valfri mapp (glöm inte att öppna Python branchen!).

Det första man bör göra är att redigera filen dnollkse/settings.py och konfigurera en databas som du kan använda tillsammans med projektet.

Nästa steg nu när vi har en fungerande databas är att skapa strukturen för django. Detta gör vi genom att öppna en terminal och navigera till projektet och skriva:

    $ python manage.py migrate

Detta kommer skapa lite django-tabeller i databasen.
Vi vill också lägga till tabeller för news-appen, vilket vi gör genom att skriva:

    $ python manage.py makemigrations news
    $ python manage.py migrate

Kommandot 'makemigrations news' kollar igenom newsapplikationens models.py efter förändringar i databasmodellerna och eftersom vi för närvarande inte har skapat de modellerna i vår databas så kommer den skapa allt från grunden.
Kommandot 'migrate' utför de nya migrationerna som skapades på steget innan.

### Hacka på! ###
Det var troligen det viktigaste för att komma igång, nu är det bara att hacka på.
Om man vill få lite koll på vad som händer så rekommenderar jag som sagt tutorialen, men jag försöker också kommentera ordentligt så har man bara lite koll så kan man försöka läsa lite i källkoden och kanske sätta sig in i sidan igenom den.

//Jassob
