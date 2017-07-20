[![Stories in Ready](https://badge.waffle.io/dtekcth/DNollK.se.svg?label=ready&title=Ready)](http://waffle.io/dtekcth/DNollK.se)


# DNollK.se #

Detta repo innehåller källkoden till hemsidan för
Datateknologsektionens (dtek.se) mottagningskommitté DNollK. Målet med
sidan är att vara en samlingsplats för all information som de
nyantagna på utbildningsprogrammet Datateknik på Chalmers tekniska
högskola kommer behöva under de första fyra veckorna på deras
Chalmerstid, mottagningen.

## Python / Django ##

Detta projekt bygger på ramverket Django
[(djangoproject.com)](http://djangoproject.com), och om man är ny på
detta ramverk så finns en jättebra tutorial på
[docs.djangoproject.com](http://docs.djangoproject.com/en), under
tutorials.

### Komma igång ###

#### Installera Python och Django ####

För att komma igång med detta projekt måste man ha Python och Django
installerade. Om man använder Linux så borde Python finnas i
pakethanteraren och i så fall är det bara installera genom
pakethanteraren. Django (och andra python-bibliotek) kan man
installera med Pythons egna pakethanterare, 'pip' (eller easy_install,
men det har jag inte använt så jag kommer inte täcka det) och det gör
man genom att skriva:

    $ pip install -r requirements.txt

För att se att django blivit installerats ordentligt kan man köra
python i en terminal och skriva:

    >>> import django
    >>> print(django.get_version())

Om du inte får något tråkigt felmeddelande så har du nu installerat
django och är redo att komma igång!

#### Konfigurera DNollK.se ####

Nu när allt är installerat så är det bara att klona (eller ladda ner)
projektet och lägga i någon valfri mapp.

Det första man bör göra är att redigera filen dnollkse/settings.py och
konfigurera en databas som du kan använda tillsammans med projektet,
som default används en sqlite-databasfil.

Nästa steg nu när vi har en fungerande databas är att skapa strukturen
för django. Detta gör vi genom att öppna en terminal och navigera till
projektet och skriva:

    $ python manage.py migrate

Django funktionen migrate kollar igenom mappen `migrations` i varje
app som finns med i listan INSTALLED_APPS och kör igenom varje
migration, en efter en.

Om man gör en ändring i någon models.py-fil och därmed ändrar på hur
django vill att databasen ska se ut ska man skapa en migration för sin
ändring genom att skriva:

	$ python manage.py makemigrations

Denna migration sparas med fördel in i versionshanteringssystemets index.

### Hacka på! ###

Om man vill få lite koll på vad som händer så rekommenderar jag som
sagt tutorialen. Om man har frågor kan maila till dnollk@dtek.se. Om
man hittar buggar eller önskar features osv är det bara att skapa en
issue.

Det var troligen det viktigaste för att komma igång, nu är det bara
att hacka på.
