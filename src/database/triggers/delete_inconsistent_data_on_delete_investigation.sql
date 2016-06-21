CREATE OR REPLACE FUNCTION delete_inconsistent_data_on_delete_investigation()
  RETURNS TRIGGER
  AS
  $X$
    BEGIN
      DELETE FROM is_suspected WHERE is_suspected.investigation_id = NEW.id;
      DELETE FROM is_witness WHERE is_witness.investigation_id = NEW.id;
    END
  $X$ LANGUAGE plpgsql;


CREATE TRIGGER delete_inconsistent_data_on_delete_investigation BEFORE DELETE ON investigation
  FOR EACH ROW
    EXECUTE PROCEDURE delete_inconsistent_data_on_delete_investigation();