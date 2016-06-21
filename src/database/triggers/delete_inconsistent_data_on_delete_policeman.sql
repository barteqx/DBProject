CREATE OR REPLACE FUNCTION delete_inconsistent_data_on_delete_policeman()
  RETURNS TRIGGER
  AS
  $X$
    BEGIN
      DELETE FROM "user" WHERE "user".citizen_id = NEW.citizen_id;
      UPDATE fine SET policeman_id = NULL WHERE policeman_id = NEW.id;
      UPDATE investigation SET policeman_id = NULL WHERE policeman_id = NEW.id;

    END
  $X$ LANGUAGE plpgsql;


CREATE TRIGGER delete_inconsistent_data_on_delete_policeman BEFORE DELETE ON policeman
  FOR EACH ROW
    EXECUTE PROCEDURE delete_inconsistent_data_on_delete_policeman();