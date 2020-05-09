package sample;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DVDsDataAccess{

    private Connection connection;

    DVDsDataAccess(String driverClassName, String dbURL) throws SQLException, ClassNotFoundException{
        Class.forName(driverClassName);
        connection = DriverManager.getConnection(dbURL);
    }

    List<Dvd> create_table(ResultSet rs, boolean getCorrected) throws SQLException{
        List<Dvd> dvdList = new ArrayList<>();          // Empty Array for storage of DVD Objects.
        while (rs.next()) {         // Works through the whole ResultSet.
            int id = rs.getInt("id");
            String titel = rs.getString("titel");
            int dauer = rs.getInt("dauer");
            int jahr = rs.getInt("jahr");
            String preis = rs.getString("preis");
            int bewertung = rs.getInt("bewertung");
            boolean rented = rs.getBoolean("verliehen");
            String rentedBy = rs.getString("rentedBy");

            String genre, hauptdarsteller;
            if (getCorrected){
                genre = rs.getString("genre");
                String vorname = rs.getString("vorname");
                String nachname = rs.getString("nachname");

                hauptdarsteller = vorname + " " + nachname;
            }else{
                genre = String.valueOf(rs.getInt("genre"));
                hauptdarsteller = String.valueOf(rs.getInt("hauptdarsteller"));
            }

            Dvd dvd = new Dvd(id, titel, genre, hauptdarsteller, dauer, jahr, preis, bewertung, rented, rentedBy);
            dvdList.add(dvd);
        }
        return dvdList;
    }

    List<Dvd> getAll() throws SQLException {
        Statement stmnt = connection.createStatement();
        ResultSet rs = stmnt.executeQuery("select * FROM dvd");

        return create_table(rs, false);
    }

    List<Dvd> getAllCorrected() throws SQLException {
        /*
        * Gets database value with corresponding values of foreign keys.
        * */
        Statement stmnt = connection.createStatement();
        ResultSet rs = stmnt.executeQuery("select dvd.id, titel, genre.bezeichnung AS genre, Darsteller.vorname, " +
                "Darsteller.nachname, dauer, jahr, preis, bewertung, verliehen, rentedBy FROM dvd JOIN Darsteller, " +
                "genre ON dvd.genre = genre.id AND hauptdarsteller = Darsteller.id");

        return create_table(rs, true);
    }

    void addDvd(Dvd dvd, int genre, int hauptdarsteller, int verliehen) throws SQLException{
        Statement stmnt = connection.createStatement();
        stmnt.executeUpdate(String.format(
                "INSERT INTO dvd(titel, genre, hauptdarsteller, dauer, jahr, preis, bewertung, verliehen, rentedBy) VALUES('%s', %d, %d, %d, %d, '%s', %d, %d, '%s')",
                dvd.getTitel(), genre, hauptdarsteller, dvd.getDauer(), dvd.getJahr(), dvd.getPreis(), dvd.getBewertung(), verliehen, dvd.getRentedBy()));          // Since the ID-Column has AUTOINCREMENT activated, only the other values are delivered.
        stmnt.close();
    }

    public void updateDvd(Dvd dvd, int genre, int hauptdarsteller) throws SQLException{
        Statement stmnt = connection.createStatement();
        stmnt.executeUpdate(String.format(
                "update dvd set titel = '%s', genre = %d, hauptdarsteller = %d, dauer = %d, jahr = %d, preis = '%s', bewertung = %d, verliehen = %d where id = %d;",
                dvd.getTitel(), genre, hauptdarsteller, dvd.getDauer(),
                dvd.getJahr(), dvd.getPreis(), dvd.getBewertung(), dvd.getVerliehen(), dvd.getId()
        ));
        stmnt.close();
    }

    public void deleteDvd(Dvd dvd) throws SQLException{
        Statement stmnt = connection.createStatement();
        stmnt.executeUpdate(String.format(
                "delete from dvd where id = %d;",
                dvd.getId()
        ));
        stmnt.close();
    }

    void resetAutoIncrement() throws SQLException{
        List<Dvd> dvdList = getAll();
        Statement stmnt = connection.createStatement();
        stmnt.executeUpdate("DELETE FROM dvd;");
        stmnt.executeUpdate("DELETE FROM sqlite_sequence WHERE name = 'dvd';");

        int converted;

        for (int i = 0; i < dvdList.size(); i++){
            if (dvdList.get(i).getVerliehen()) converted = 1;
            else converted = 0;

            addDvd(dvdList.get(i), Integer.parseInt(dvdList.get(i).getGenre()), Integer.parseInt(dvdList.get(i).getHauptdarsteller()), converted);
        }
    }

    public void shutdown() throws SQLException {
        if (connection != null) {
            connection.close();
        }
    }
}
