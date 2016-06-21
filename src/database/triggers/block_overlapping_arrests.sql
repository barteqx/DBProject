CREATE OR REPLACE FUNCTION block_overlapping_arrests()
  RETURNS TRIGGER
  AS
  $X$
    DECLARE
      c arrest;
    BEGIN
      FOR c IN (SELECT * FROM arrest WHERE citizen_id = NEW.citizen_id)
      LOOP
        IF (NEW.start_date BETWEEN c.start_date AND c.end_date) OR
          (NEW.end_date BETWEEN c.start_date AND c.end_date) THEN
          raise NOTICE 'One man cannot be in jail twice simultaneously';
          RETURN NULL;
        END IF;
      END LOOP;
    END
  $X$ LANGUAGE plpgsql;
CREATE TRIGGER block_overlapping_arrests BEFORE DELETE ON arrest
  FOR EACH ROW
    EXECUTE PROCEDURE block_overlapping_arrests();