package sample;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class GenreDataAccess {

    private Connection connection;

    public GenreDataAccess(String driverClassName, String dbURL) throws SQLException, ClassNotFoundException{
        Class.forName(driverClassName);
        connection = DriverManager.getConnection(dbURL);
    }

    public void shutdown() throws SQLException {
        if (connection != null) {
            connection.close();
        }
    }

    public List<Genre> getGenreList() throws SQLException {
        try(
                Statement stmnt = connection.createStatement();
                ResultSet rs = stmnt.executeQuery("select * from Genre");
        ){
            List<Genre> genreList = new ArrayList<>();
            while (rs.next()) {
                int genre_id = rs.getInt("genre_id");
                String name = rs.getString("name");
                Genre genre = new Genre(genre_id, name);
                genreList.add(genre);
            }
            return genreList;
        }
    }

    String getGenre(int id){
        try{
            Statement stmnt = connection.createStatement();
            ResultSet rs = stmnt.executeQuery(String.format("SELECT bezeichnung FROM genre where id = %d", id));

            return rs.getString("bezeichnung");
        }catch (SQLException e){
            return null;
        }
    }

    int getGenreId(String genreName){
        try{
            Statement stmnt = connection.createStatement();
            ResultSet rs = stmnt.executeQuery(String.format("SELECT id FROM genre WHERE bezeichnung = '%s'", genreName));

            return rs.getInt("id");
        }catch (SQLException e){
            return 0;
        }
    }

    void addGenre(String genreName) throws SQLException{
        Statement stmnt = connection.createStatement();
        stmnt.executeUpdate(String.format("INSERT INTO genre(bezeichnung) VALUES ('%s')", genreName));

        stmnt.close();
    }

}
