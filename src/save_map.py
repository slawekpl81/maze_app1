import os
import json
def save_next_map(grid_data: list):
    """
    Sprawdza pliki map1.json, map2.json, itd. i tworzy następny
    plik w kolejności (np. map4.json), zapisując do niego dane z listy.

    :param grid_data: Lista zawierająca dane (np. [0, 1, 1, 0, ...])
    :return: Nazwa zapisanego pliku lub None w przypadku błędu.
    """
    base_name = "map"
    extension = ".json"
    map_number = 1

    # 1. Znajdowanie następnego wolnego numeru
    while True:
        filename = f"{base_name}{map_number}{extension}"

        # Sprawdzamy, czy plik o tej nazwie istnieje
        if not os.path.exists(filename):
            print(f"Znaleziono wolny numer: {map_number}. Tworzenie pliku: {filename}")
            break

        map_number += 1

        # Ograniczenie bezpieczeństwa, aby uniknąć nieskończonej pętli
        if map_number > 1000:
            print("Osiągnięto limit 1000 plików. Przerwanie.")
            return None

    # 2. Zapisywanie danych do nowego pliku
    try:
        # Użycie json do zapisywania struktur danych jest najlepszą praktyką
        with open(filename, 'w') as f:
            json.dump(grid_data, f)

        print(f"Dane zapisane pomyślnie do pliku: {filename}")
        return filename

    except IOError as e:
        print(f"Błąd zapisu pliku {filename}: {e}")
        return None