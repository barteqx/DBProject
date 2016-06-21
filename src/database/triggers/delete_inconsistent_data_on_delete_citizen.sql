CREATE OR REPLACE FUNCTION delete_inconsistent_data_on_delete_citizen()
  RETURNS TRIGGER
  AS
  $X$
    BEGIN
      DELETE FROM "user" WHERE "user".citizen_id = NEW.id;
      DELETE FROM is_suspected WHERE is_suspected.citizen_id = NEW.id;
      DELETE FROM is_witness WHERE is_witness.citizen_id = NEW.id;
      DELETE FROM policeman WHERE policeman.citizen_id = NEW.id;
      DELETE FROM fine WHERE fine.citizen_id = NEW.id;
      DELETE FROM arrest WHERE arrest.citizen_id = NEW.id;
    END
  $X$ LANGUAGE plpgsql;
CREATE TRIGGER delete_inconsistent_data_on_delete_citizen BEFORE DELETE ON citizen
  FOR EACH ROW
    EXECUTE PROCEDURE delete_inconsistent_data_on_delete_citizen();