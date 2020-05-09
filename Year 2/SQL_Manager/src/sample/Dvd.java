package sample;

public class Dvd {

    private int id;
    private String titel;
    private String genre;
    private String hauptdarsteller;
    private int dauer;
    private int jahr;
    private String preis;           // Preis is saved as String, to accept comma as a decimal separator.
    private int bewertung;
    private boolean verliehen;
    private String rentedBy;

    public Dvd(int id, String titel, String genre, String hauptdarsteller, int dauer, int jahr, String preis, int bewertung, boolean verliehen, String rentedBy) {
        this.id = id;
        this.titel = titel;
        this.genre = genre;
        this.hauptdarsteller = hauptdarsteller;
        this.dauer = dauer;
        this.jahr = jahr;
        this.preis = preis;
        this.bewertung = bewertung;
        this.verliehen = verliehen;
        this.rentedBy = rentedBy;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitel() {
        return titel;
    }

    public void setTitel(String titel) {
        this.titel = titel;
    }

    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }

    public String getHauptdarsteller() {
        return hauptdarsteller;
    }

    public void setHauptdarsteller(String hauptdarsteller) {
        this.hauptdarsteller = hauptdarsteller;
    }

    public int getDauer() {
        return dauer;
    }

    public void setDauer(int dauer) {
        this.dauer = dauer;
    }

    public int getJahr() {
        return jahr;
    }

    public void setJahr(int jahr) {
        this.jahr = jahr;
    }

    public String getPreis() {
        return preis;
    }

    public void setPreis(String preis) {
        this.preis = preis;
    }

    public int getBewertung() {
        return bewertung;
    }

    public void setBewertung(int bewertung) {
        this.bewertung = bewertung;
    }

    public boolean getVerliehen() {
        return verliehen;
    }

    public void setVerliehen(boolean rented) {
        this.verliehen = rented;
    }

    public String getRentedBy() {
        return rentedBy;
    }

    public void setRentedBy(String rentedBy) {
        this.rentedBy = rentedBy;
    }
}
