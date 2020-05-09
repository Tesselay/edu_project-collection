package sample;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class HauptdarstellerDataAccess {

    private Connection connection;

    public HauptdarstellerDataAccess(String driverClassName, String dbURL) throws SQLException, ClassNotFoundException{
        Class.forName(driverClassName);
        connection = DriverManager.getConnection(dbURL);
    }

    public void shutdown() throws SQLException {
        if (connection != null) {
            connection.close();
        }
    }

    public List<Hauptdarsteller> getHdList() throws SQLException {
        try(
                Statement stmnt = connection.createStatement();
                ResultSet rs = stmnt.executeQuery("select * from Hauptdarsteller");
        ){
            List<Hauptdarsteller> hdList = new ArrayList<>();
            while (rs.next()) {
                int darsteller_id = rs.getInt("darsteller_id");
                String full_name = rs.getString("full_name");
                Hauptdarsteller hd = new Hauptdarsteller(darsteller_id, full_name);
                hdList.add(hd);
            }
            return hdList;
        }
    }

    String getHauptdarsteller(int id){
        try{
            Statement stmnt = connection.createStatement();
            ResultSet rs = stmnt.executeQuery(String.format("SELECT [vorname || ' ' || nachname] AS name FROM genre where id = %d", id));

            return rs.getString("name");
        }catch (SQLException e){
            return null;
        }
    }

    int getHauptdarstellerId(String vorname, String name){
        try{
            Statement stmnt = connection.createStatement();
            ResultSet rs = stmnt.executeQuery(String.format("SELECT id FROM Darsteller WHERE vorname = '%s' AND nachname = '%s'", vorname, name));

            return rs.getInt("id");
        }catch (SQLException e){
            return 0;
        }
    }

    void addHauptdarsteller(String vorname, String name) throws SQLException{
        Statement stmnt = connection.createStatement();
        stmnt.executeUpdate(String.format("INSERT INTO Darsteller(vorname, nachname) VALUES('%s', '%s')", vorname, name));

        stmnt.close();
    }
}
