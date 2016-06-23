CREATE OR REPLACE FUNCTION block_more_than_one_prisoner_in_one_cell()
  RETURNS TRIGGER
  AS
  $X$
   DECLARE
      c arrest;
    BEGIN
      FOR c IN (SELECT * FROM arrest WHERE cell_id = NEW.cell_id
                                           AND citizen_id <> NEW.citizen_id)
      LOOP
        IF ((NEW.start_date BETWEEN c.start_date AND c.end_date) OR
          (NEW.end_date BETWEEN c.start_date AND c.end_date)) THEN
          raise NOTICE 'Cannot put two prisoners in one cell simultaneously.';
          RETURN NULL;
        END IF;
      END LOOP;
      RETURN NEW;
    END
  $X$ LANGUAGE plpgsql;
CREATE TRIGGER block_more_than_one_prisoner_in_one_cell BEFORE INSERT ON arrest
  FOR EACH ROW
    EXECUTE PROCEDURE block_more_than_one_prisoner_in_one_cell();