package sample;

import javafx.fxml.FXML;
import javafx.scene.control.*;

import java.sql.SQLException;
import java.util.Optional;

public class addDvdController {

    @FXML
    TextField tfTitel, tfGenre, tfDarstellerVorname, tfDarstellerName, tfDauer, tfJahr, tfPreis, tfBewertung, tfVerliehen;
    @FXML
    Button continueButton;

    Dvd row = Controller.rowData;

    private DVDsDataAccess DVDdataAccessor ;
    private GenreDataAccess GenreDataAccessor;
    private HauptdarstellerDataAccess HauptdarstellerDataAccessor;
    private String genre, darsteller;

    public void initialize() {

        if (row != null){
            tfTitel.setText(row.getTitel());
            tfGenre.setText(row.getGenre());

            String[] nameSplit = row.getHauptdarsteller().split("\\s+");
            tfDarstellerVorname.setText(nameSplit[0]);
            tfDarstellerName.setText(nameSplit[1]);
            tfDauer.setText(String.valueOf(row.getDauer()));
            tfJahr.setText(String.valueOf(row.getJahr()));
            tfPreis.setText(row.getPreis());
            tfBewertung.setText(String.valueOf(row.getBewertung()));
            if (row.getVerliehen() == true) tfVerliehen.setText(row.getRentedBy());
        }

        if (Controller.rent){
            continueButton.fire();
        }

    }

    public void continueButtonOnAction() throws SQLException, ClassNotFoundException {
        if((!tfTitel.getText().equals("") && !tfGenre.getText().equals("") && !tfDarstellerVorname.getText().equals("") && !tfDarstellerName.getText().equals("")
                && !tfDauer.getText().equals("") && !tfJahr.getText().equals("") && !tfPreis.getText().equals("") && !tfBewertung.getText().equals("") || Controller.rent)){
            // Checks if all columns/choiceboxes are filled/chosen.

            int verliehen;

            int darstellerId;
            int genreId;

            // The respective tables are accessed one after another, to ensure there are no issues when having multiple accesses open
            while(true){
                GenreDataAccessor = new GenreDataAccess("org.sqlite.JDBC", "jdbc:sqlite:DVD.db3");
                genreId = GenreDataAccessor.getGenreId(tfGenre.getText());          // Controls if the Genre/Hauptdarsteller exists and either returns the corresponding ID or a 0 for a non existing one.
                if (genreId == 0){
                    GenreDataAccessor.addGenre(tfGenre.getText());
                }else{
                    genre = GenreDataAccessor.getGenre(genreId);
                    GenreDataAccessor.shutdown();           // Connections for other accessors are closed.
                    break;
                }
            }

            while (true){
                HauptdarstellerDataAccessor = new HauptdarstellerDataAccess("org.sqlite.JDBC", "jdbc:sqlite:DVD.db3");
                darstellerId = HauptdarstellerDataAccessor.getHauptdarstellerId(tfDarstellerVorname.getText(), tfDarstellerName.getText());

                if (darstellerId == 0){
                    HauptdarstellerDataAccessor.addHauptdarsteller(tfDarstellerVorname.getText(), tfDarstellerName.getText());
                }else{
                    darsteller = HauptdarstellerDataAccessor.getHauptdarsteller(darstellerId);
                    HauptdarstellerDataAccessor.shutdown();
                    break;
                }
            }

            DVDdataAccessor = new DVDsDataAccess("org.sqlite.JDBC", "jdbc:sqlite:DVD.db3");

            if (tfVerliehen.getText() != null) verliehen = 1;          // SQLite saves booleans as 0 or 1, the corresponding variable gets the value here.
            else verliehen = 0;

            if (row != null){          // Changing instead of adding data, still adds a new row in the same matter, but the old data is deleted.
                DVDdataAccessor.deleteDvd(row);
                row = null;
                Controller.rowData = null;
            }

            if (Controller.rent){
                TextInputDialog dialog = new TextInputDialog("");
                dialog.setTitle("Verliehen an");
                dialog.setHeaderText("An welche Person wird die DVD verliehen? (Nur Nachname)");
                dialog.setContentText("Bitte Namen eingeben:");

                Optional<String> result = dialog.showAndWait();
                result.ifPresent(name -> tfVerliehen.setText(name));
            }


            Dvd dvd = createDvdObject(verliehen);
            DVDdataAccessor.addDvd(dvd, genreId, darstellerId, verliehen);

            Controller.rent = false;
            DVDdataAccessor.shutdown();
            Controller.secondaryStage.close();

        }else{
            Alert alert = new Alert(Alert.AlertType.WARNING);           // In case not all columns are filled, a warning message is displayed.
            alert.setContentText("Not all textfields or choiceboxes are filled");
            alert.setTitle("Warning");
            alert.show();
        }
    }

    private Dvd createDvdObject(int verliehen){
        String titel = tfTitel.getText();
        int dauer = Integer.parseInt(tfDauer.getText());
        int jahr = Integer.parseInt(tfJahr.getText());
        String preis = tfPreis.getText();
        int bewertung = Integer.parseInt(tfBewertung.getText());
        String rentedBy = tfVerliehen.getText();

        boolean converted;          // Variable for display for 'verliehen' variable as an boolean (instead of 0/1)
        converted = verliehen == 1;         // Sets converted to true, if 'verliehen' is 1, otherwise to false

        return new Dvd(0, titel, genre, darsteller, dauer, jahr, preis, bewertung, converted, rentedBy);
    }

}
