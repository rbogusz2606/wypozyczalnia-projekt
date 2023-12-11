# wypozyczalnia-projekt

Po zainstalowaniu niezbędnych plików i wystartowaniu lokalnego serwera link przekierowuję nas na strone logowania. Należy tam utworzyć konto i się zalogować.
Po zalogowaniu przekierowujemy się do głównej strony index.html gdzie mamy opcje wyboru poszczególnych samochodów z bazy danych cars.
Po kliknięciu w dany samochód zostajemy przekierowani do strony DetailView danego samochodu gdzie opisane są jego parametry i wyświetlony jest przycisk z pytaniem o dostępność samochodu.
Po przejsciu w adres http z przycisku zostaje wyświetlony formularz w którym podajemy informacje użytkownika i samochód którym jesteśmy zainteresowani i klikamy "send".
Jeżeli formularz jest poprawny zostajemy przekierowani do storny "Succes" i dane użytkownika wraz z wybranym samochodem zostają wysłane metodą post do bazy danych caravailability, którą w moim przypadku wyświetlam w panelu admin.

API:
W projekcie API dotyczy modelu Cars. Pozwala wyświetlić aktualny stan bazy, dodać do bazy obiekt, usunąć obiekt i edytować obiekt.


WYKORZYSTANE METODY W PROJEKCIE:
-PYTHON
-CRUD
-DRF
-MODEL-VIEW-TEMPLATE
-DJANGO
-DJANGO ADMIN
-GIT
