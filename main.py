from mojabiblioteka import PDFmanager

def main():
    pdf = PDFmanager()

    # Wypełnianie formularza
    form_data = {
        "name": "imie",
        "email": "email",
        "zgoda": True
    }

    try:
        pdf.fill_form("formularz_wejsciowy.pdf", "formularz_wypelniony.pdf", form_data)
        print("Formularz został wypełniony.")
    except Exception as e:
        print(f"Błąd: {e}")

    # Łączenie PDFów
    pdfy_do_polaczenia = ["plik1.pdf", "plik2.pdf", "plik3.pdf"]

    try:
        pdf.merge_pdfs(pdfy_do_polaczenia, "polaczony.pdf")
        print("PDFy zostały połączone.")
    except Exception as e:
        print(f"Błąd: {e}")

if __name__ == "__main__":
    main()