package sample;

public class Genre {

    private int genre_id;
    private String name;

    public Genre(int genre_id, String name) {
        this.genre_id = genre_id;
        this.name = name;
    }

    public int getGenre_id() {
        return genre_id;
    }

    public void setGenre_id(int genre_id) {
        this.genre_id = genre_id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
