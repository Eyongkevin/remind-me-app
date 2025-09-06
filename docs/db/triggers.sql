/*
This trigger will fire before an UPDATE operation on 
reminder and set the modified_at column of the affected row 
to the current timestamp using CURRENT_TIMESTAMP
*/
CREATE TRIGGER update_reminder_modified_at
BEFORE UPDATE ON reminder
FOR EACH ROW -- for each row affected by the update
BEGIN
    UPDATE reminder SET modified_at = CURRENT_TIMESTAMP WHERE id= OLD.id; -- OLD.id is the id of the row before update
END;