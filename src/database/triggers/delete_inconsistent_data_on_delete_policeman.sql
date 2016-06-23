CREATE OR REPLACE FUNCTION delete_inconsistent_data_on_delete_policeman()
  RETURNS TRIGGER
  AS
  $X$
    BEGIN
      DELETE FROM "user" WHERE "user".citizen_id = OLD.citizen_id;
      UPDATE fine SET policeman_id = NULL WHERE policeman_id = OLD.id;
      UPDATE investigation SET policeman_id = NULL WHERE policeman_id = OLD.id;
      RETURN OLD;
    END
  $X$ LANGUAGE plpgsql;
CREATE TRIGGER delete_inconsistent_data_on_delete_policeman BEFORE DELETE ON policeman
  FOR EACH ROW
    EXECUTE PROCEDURE delete_inconsistent_data_on_delete_policeman();