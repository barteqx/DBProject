CREATE OR REPLACE FUNCTION block_policeman_addition_without_account()
  RETURNS TRIGGER
  AS
  $X$
    BEGIN
      IF NOT EXISTS(SELECT * FROM "user" WHERE citizen_id = NEW.citizen_id) THEN
        raise NOTICE 'Policeman must have an account first.';
        RETURN NULL;
      END IF;
    END
  $X$ LANGUAGE plpgsql;
CREATE TRIGGER block_policeman_addition_without_account BEFORE DELETE ON policeman
  FOR EACH ROW
    EXECUTE PROCEDURE block_policeman_addition_without_account();