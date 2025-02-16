Python Selenium Test Automation Framework

📌 Opis projektu

Jest to framework do automatyzacji testów UI oparty na Python, Selenium, PyTest. Framework umożliwia testowanie aplikacji webowej https://rahulshettyacademy.com/angularpractice/, obsługując różne przeglądarki oraz generując raporty testowe.

🚀 Technologie użyte w projekcie

Python 3 – język programowania

Selenium WebDriver – automatyzacja testów UI

PyTest – framework do testowania

PyTest HTML Report – generowanie raportów testowych

🛠️ Instalacja i konfiguracja

1. Sklonowanie repozytorium

git clone https://github.com/grzegorzplowiec/e-commerce.git
cd e-commerce

2. Instalacja zależności

Upewnij się, że masz zainstalowanego Python 3 oraz pip, następnie uruchom:

pip install -r requirements.txt

3. Uruchomienie testów

Testy można uruchomić dla różnych przeglądarek.

Uruchomienie testów w domyślnej przeglądarce (Chrome)

pytest -v --html=report.html

Uruchomienie testów w Firefox

pytest -v --browser_name=firefox --html=report.html

Uruchomienie testów w Edge

pytest -v --browser_name=edge --html=report.html

📝 Opis kluczowych plików

1. conftest.py

Konfiguracja testów w PyTest.

Obsługuje uruchamianie testów na różnych przeglądarkach.

Tworzy raporty testowe w formacie HTML i wykonuje screenshoty w przypadku błędów.

2. test_e2e.py (Test End-to-End)

Otwiera stronę główną i przechodzi do sekcji sklepu.

Wybiera produkt „Blackberry” i dodaje go do koszyka.

Finalizuje zakup, wybierając kraj dostawy i akceptując warunki.

Sprawdza, czy pojawił się komunikat o sukcesie zamówienia.

3. test_home_page.py (Test formularza)

Wypełnia formularz użytkownika (imię, e-mail, hasło, płeć).

Kliknięcie przycisku „Submit” i walidacja komunikatu o sukcesie.

📊 Raporty testowe

Framework generuje raporty testowe w formacie HTML, które można znaleźć w katalogu reports/.
Po zakończeniu testów otwórz raport w przeglądarce:

start report.html  # Windows
open report.html    # macOS/Linux

❓ FAQ

1. Jak dodać nowe testy?

Dodaj nowe pliki testowe w katalogu tests/, korzystając z PyTest i metod Page Object Model (POM).

2. Jak zmienić przeglądarkę dla testów?

Dodaj parametr --browser_name=firefox lub --browser_name=edge podczas uruchamiania pytest.

3. Jak poprawić błąd refusing to merge unrelated histories?

Jeśli scalasz dwie niezależne gałęzie, użyj:

git merge main --allow-unrelated-histories

📌 Autor

Projekt stworzony przez Grzegorz Płowiec. 🚀
