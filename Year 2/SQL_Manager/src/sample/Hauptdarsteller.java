package sample;

public class Hauptdarsteller {

    private int darsteller_id;
    private String full_name;

    public Hauptdarsteller(int darsteller_id, String full_name) {
        this.darsteller_id = darsteller_id;
        this.full_name = full_name;
    }

    public int getDarsteller_id() {
        return darsteller_id;
    }

    public void setDarsteller_id(int darsteller_id) {
        this.darsteller_id = darsteller_id;
    }

    public String getFull_name() {
        return full_name;
    }

    public void setFull_name(String full_name) {
        this.full_name = full_name;
    }
}
