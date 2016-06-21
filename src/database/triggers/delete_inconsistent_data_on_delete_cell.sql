CREATE OR REPLACE FUNCTION delete_inconsistent_data_on_delete_cell()
  RETURNS TRIGGER
  AS
  $X$
    BEGIN
      DELETE FROM arrest WHERE arrest.cell_id = NEW.id;
    END
  $X$ LANGUAGE plpgsql;
CREATE TRIGGER delete_inconsistent_data_on_delete_cell BEFORE DELETE ON policeman
  FOR EACH ROW
    EXECUTE PROCEDURE delete_inconsistent_data_on_delete_cell();