package sample;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

import java.sql.SQLException;
import java.util.Optional;

public class Controller extends GridPane {

    @FXML
    Button openDatabase, addDvd, closeApplication;
    @FXML
    TableView tableViewer;

    static boolean rent;
    static Dvd rowData;
    static Stage secondaryStage;

    private DVDsDataAccess DVDdataAccessor ;

    public void initialize() throws SQLException, ClassNotFoundException {
        DVDdataAccessor = new DVDsDataAccess("org.sqlite.JDBC", "jdbc:sqlite:DVD.db3");

        TableColumn<Dvd, String> titleCol = new TableColumn<>("Titel");
        titleCol.prefWidthProperty().bind(tableViewer.widthProperty().multiply(0.1));
        titleCol.setResizable(false);
        titleCol.setCellValueFactory(new PropertyValueFactory<>("titel"));          // ValueFactories for insertion of column values.

        TableColumn<Dvd, String> genreCol = new TableColumn<>("Genre");
        genreCol.prefWidthProperty().bind(tableViewer.widthProperty().multiply(0.1));
        genreCol.setResizable(false);
        genreCol.setCellValueFactory(new PropertyValueFactory<>("genre"));

        TableColumn<Dvd, String> mainActorCol = new TableColumn<>("Hauptdarsteller");
        mainActorCol.prefWidthProperty().bind(tableViewer.widthProperty().multiply(0.195));
        /* Fills the table width perfectly with this value. If the sum of the width multipliers is 1.0, the table is a bit wider than it's presentation window. Except for when the window is enlarged,
         * so either it's this and it fits perfectly in its initial look but not enlarged, or it doesn't fit perfectly in both cases.
         * */
        mainActorCol.setResizable(false);
        mainActorCol.setCellValueFactory(new PropertyValueFactory<>("hauptdarsteller"));

        TableColumn<Dvd, String> lengthCol = new TableColumn<>("Dauer");
        lengthCol.prefWidthProperty().bind(tableViewer.widthProperty().multiply(0.1));
        lengthCol.setResizable(false);
        lengthCol.setCellValueFactory(new PropertyValueFactory<>("dauer"));

        TableColumn<Dvd, String> releaseYearCol = new TableColumn<>("Jahr");
        releaseYearCol.prefWidthProperty().bind(tableViewer.widthProperty().multiply(0.1));
        releaseYearCol.setResizable(false);
        releaseYearCol.setCellValueFactory(new PropertyValueFactory<>("jahr"));

        TableColumn<Dvd, String> priceCol = new TableColumn<>("Preis");
        priceCol.prefWidthProperty().bind(tableViewer.widthProperty().multiply(0.1));
        priceCol.setResizable(false);
        priceCol.setCellValueFactory(new PropertyValueFactory<>("preis"));

        TableColumn<Dvd, String> ratingCol = new TableColumn<>("Bewertung");
        ratingCol.prefWidthProperty().bind(tableViewer.widthProperty().multiply(0.1));
        ratingCol.setResizable(false);
        ratingCol.setCellValueFactory(new PropertyValueFactory<>("bewertung"));

        TableColumn<Dvd, String> rentedCol = new TableColumn<>("Verliehen");
        rentedCol.prefWidthProperty().bind(tableViewer.widthProperty().multiply(0.1));
        rentedCol.setResizable(false);
        rentedCol.setCellValueFactory(new PropertyValueFactory<>("verliehen"));

        TableColumn<Dvd, String> rentedByCol = new TableColumn<>("Verliehen von");
        rentedByCol.prefWidthProperty().bind(tableViewer.widthProperty().multiply(0.1));
        rentedByCol.setResizable(false);
        rentedByCol.setCellValueFactory(new PropertyValueFactory<>("rentedBy"));

        tableViewer.getColumns().addAll(titleCol, genreCol, mainActorCol, lengthCol, releaseYearCol, priceCol, ratingCol, rentedCol, rentedByCol);

        Alert alert = new Alert(Alert.AlertType.CONFIRMATION);
        alert.setTitle("Löschen/Ändern");
        alert.setHeaderText("Wollen Sie die Reihe ändern oder löschen?");
        alert.setContentText("Wählen Sie Ihre Option.");

        ButtonType buttonTypeDelete = new ButtonType("Löschen");
        ButtonType buttonTypeChange = new ButtonType("Ändern");
        ButtonType buttonTypeRent = new ButtonType("Ausleihen");
        ButtonType buttonTypeCancel = new ButtonType("Abbrechen");

        alert.getButtonTypes().setAll(buttonTypeDelete, buttonTypeChange, buttonTypeRent, buttonTypeCancel);

        tableViewer.setRowFactory(tv -> {
            TableRow<Dvd> row = new TableRow<>();
            row.setOnMouseClicked(event -> {
                if (event.getClickCount() > 1 && (!row.isEmpty()) ){
                    rowData = row.getItem();
                    try{
                        Optional<ButtonType> result = alert.showAndWait();
                        if (result.get() == buttonTypeDelete){
                            DVDdataAccessor.deleteDvd(rowData);
                            DVDdataAccessor.resetAutoIncrement();           // Resets id column to keep the database happy.
                            openDatabaseOnAction();
                        }else if (result.get() == buttonTypeChange){
                            createWindow();
                            DVDdataAccessor.resetAutoIncrement();
                        }else if (result.get() == buttonTypeRent){
                            rowData.setVerliehen(true);
                            rent = true;
                            createWindow();
                            secondaryStage.close();         // For whatever reason, the addDvd Window opens again after the shutdown in its Controller file. This only happens here, so I invoke the close function again.
                            DVDdataAccessor.resetAutoIncrement();
                            openDatabaseOnAction();
                        }else if (result.get() == buttonTypeCancel){
                            alert.close();
                        }
                    } catch(Exception e){
                        e.printStackTrace();
                    }
                }
            });
            return row;
        });
    }

    private void createWindow() throws Exception{
        secondaryStage = new Stage();
        Parent root = FXMLLoader.load(getClass().getResource("addDvd.fxml"));
        secondaryStage.setTitle("DVD hinzufügen/ändern");
        secondaryStage.setScene(new Scene(root, 900, 600));
        secondaryStage.show();
        openDatabaseOnAction();

        //tableViewer.getItems().clear();             // Clear after add/change window to signify change. addAll doesn't work if it's used here.
    }

    public void openDatabaseOnAction() throws Exception{
        tableViewer.getItems().clear();
        tableViewer.getItems().addAll(DVDdataAccessor.getAllCorrected());
    }

    public void addDvdOnAction() throws Exception{
        createWindow();
    }

    public void closeApplicationOnAction() throws SQLException{
        DVDdataAccessor.shutdown();
        System.exit(0);
    }
}
