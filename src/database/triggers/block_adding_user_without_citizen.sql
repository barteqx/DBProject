CREATE OR REPLACE FUNCTION block_adding_user_without_citizen()
  RETURNS TRIGGER
  AS
  $X$
    BEGIN
      IF NOT EXISTS(SELECT * FROM citizen WHERE id = NEW.citizen_id) THEN
        raise NOTICE 'User must have corresponding citizen first.';
        RETURN NULL;
      END IF;
      RETURN NEW;
    END
  $X$ LANGUAGE plpgsql;
CREATE TRIGGER block_adding_user_without_citizen BEFORE INSERT OR UPDATE ON "user"
  FOR EACH ROW
    EXECUTE PROCEDURE block_adding_user_without_citizen();