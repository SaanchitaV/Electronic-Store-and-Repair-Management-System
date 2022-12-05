------------------------- QUERIES ----------------------------

CREATE TABLE repair( user_id int, item_id int, item_type text, purchase_id int, date_of_purchase date, date_of_service date, item_repair_code int, item_warranty int, warranty_usage text, PRIMARY KEY(item_repair_code));
CREATE TABLE purchase( user_id int, user_name TEXT, item_id int, item_type text, purchase_id int, date_of_purchase date, purchase_amt int,PRIMARY KEY(purchase_id));
CREATE TABLE item_backup ( item_type TEXT, item_id INT, item_brand text, item_version TEXT, item_repair_code INT);
CREATE TABLE person_backup ( user_name TEXT, user_age INT, user_id INT, user_gender TEXT, user_phone TEXT);  

ALTER TABLE purchase ADD CONSTRAINT iid FOREIGN KEY (item_id) REFERENCES item(item_id);
ALTER TABLE repair ADD CONSTRAINT rid FOREIGN KEY (purchase_id) REFERENCES purchase(purchase_id);

-- -----------------------------------------------------------------------------------
-- LOAD DATA INTO TABLES USING THE LOAD DATA INFILE QUERY
-- -----------------------------------------------------------------------------------



-- JOIN OPERATIONS
-- ------------------------------------------------------------------------
-- 1. JOIN OF USER TABLE WITH REPAIR TABLE
SELECT 
    user.user_id,
    user.user_name,
    user.user_phone,
    repair.item_id,
    repair.purchase_id,
    repair.date_of_service
FROM
    electronic_shop_and_repair_management_364.user
        INNER JOIN
    electronic_shop_and_repair_management_364.repair ON user.user_id = repair.user_id;

-- 2. JOIN OF ITEM TABLE AND PURCHASE TABLE
SELECT 
    item.item_id,
    item.item_type,
    item.item_brand,
    item.item_version,
    item.item_supplier,
    purchase.purchase_id,
    purchase.user_name,
    purchase.date_of_purchase,
    purchase.purchase_amt
FROM
    item
        INNER JOIN
    purchase ON item.item_id = purchase.item_id;

-- 3. LEFT JOIN ITEM TABLE AND REPAIR TABLE
SELECT 
    item.item_id,
    item.item_type,
    item.item_brand,
    repair.date_of_service
FROM
    item
        LEFT JOIN
    repair ON item.item_id = repair.item_id;

-- 4. INNER JOIN USER AND PURCHASE TABLE
SELECT 
    user.user_name,
    user.user_feedback,
    purchase.purchase_id,
    purchase.item_id,
    purchase.item_type,
    item.item_brand,
    item.item_version,
    item.item_warranty
FROM ((user INNER JOIN purchase ON user.user_name = purchase.user_name) INNER JOIN item ON purchase.item_id=item.item_id);

-- ------------------------------------------------------------------------

-- AGGREGATE OPERATIONS
-- ------------------------------------------------------------------------

-- 1. MIN
-- To find least amount sold
  
SELECT * FROM purchase WHERE purchase_amt=(SELECT MIN(purchase_amt) FROM purchase);
    
    
-- 2. MAX
SELECT * FROM purchase WHERE purchase_amt=(SELECT MAX(purchase_amt) FROM purchase);
   
   
-- 3. SUM
SELECT 
    SUM(purchase_amt) AS Total_Sales
FROM
    electronic_shop_and_repair_management_364.purchase;
   
   
-- 4. GROUP BY - Based on item_type
SELECT 
    item_type, SUM(purchase_amt)
FROM
    electronic_shop_and_repair_management_364.purchase
GROUP BY item_type;


-- 5. AVG
SELECT 
    AVG(purchase_amt) AS Average_Sales
FROM
    electronic_shop_and_repair_management_364.purchase;
-- ------------------------------------------------------------------------


-- SET OPERATIONS
-- ------------------------------------------------------------------------

-- 1. INTERSECTION OF REPAIR AND PURCHASE TABLES
SELECT user_id,item_id,item_type,purchase_id,date_of_purchase FROM electronic_shop_and_repair_management_364.repair
INTERSECT
SELECT user_id,item_id,item_type,purchase_id,date_of_purchase FROM electronic_shop_and_repair_management_364.purchase;


-- 2. MINUS OF PURCHASE AND REPAIR TABLEs
SELECT user_id,item_id,item_type,purchase_id,date_of_purchase FROM electronic_shop_and_repair_management_364.purchase
EXCEPT
SELECT user_id,item_id,item_type,purchase_id,date_of_purchase FROM electronic_shop_and_repair_management_364.repair;


-- 3. UNION ALL OF REPAIR AND USER TABLEs
SELECT user_id FROM electronic_shop_and_repair_management_364.user UNION ALL SELECT user_id FROM electronic_shop_and_repair_management_364.repair; 


-- 4. MINUS OF USER AND PURCHASE TABLEs
SELECT user_id,user_name FROM electronic_shop_and_repair_management_364.user EXCEPT SELECT user_id,user_name FROM electronic_shop_and_repair_management_364.purchase;

-- ------------------------------------------------------------------------



-- TRIGGERS
-- ------------------------------------------------------------------------



-- 1. Before Insert Trigger

delimiter //
CREATE TRIGGER add_user BEFORE INSERT
ON user
FOR EACH ROW
IF NEW.user_age < 18 THEN
SIGNAL SQLSTATE '50001' SET MESSAGE_TEXT = "User must be older than 18 ";
END IF; //
delimiter;

-- 2. Before Update Trigger
delimiter //
CREATE TRIGGER update_user BEFORE UPDATE
ON user
FOR EACH ROW
IF NEW.user_age < 18 THEN
SIGNAL SQLSTATE '50002' SET MESSAGE_TEXT = "User must be older than 18 ";
END IF; //
delimiter;

-- 3. Before Delete Trigger - User Table
delimiter //
CREATE TRIGGER store_user_bd BEFORE DELETE
ON user
FOR EACH ROW
INSERT INTO person_backup (user_name,user_age,user_id,user_gender,user_phone)
VALUES (OLD.user_name, OLD.user_age, OLD.user_id, OLD.user_gender, OLD.user_phone);//

-- create table person_backup ( user_name TEXT, user_age INT, user_id INT, user_gender TEXT, user_phone TEXT);  
-- DELETE FROM electronic_shop_and_repair_management_364.user WHERE user_id=2;

delimiter;

-- 4. Before Delete Trigger - Item Table
delimiter //
CREATE TRIGGER store_item_bd BEFORE DELETE
ON item
FOR EACH ROW
INSERT INTO item_backup (item_type,item_id,item_brand,item_version,item_repair_code)
VALUES (OLD.item_type, OLD.item_id, OLD.item_brand, OLD.item_version, OLD.item_repair_code);//
delimiter;

-- create table item_backup ( item_type TEXT, item_id INT, item_brand text, item_version TEXT, item_repair_code INT);
-- DELETE FROM electronic_shop_and_repair_management_364.item WHERE item_id=8;

-- ------------------------------------------------------------------------



-- CURSOR
-- ------------------------------------------------------------------------


DELIMITER $$
CREATE PROCEDURE set_warranty()
BEGIN
DECLARE res1 INT;
DECLARE res INT;
DECLARE irc INT;
DECLARE iw INT;
DECLARE dop DATE;
DECLARE dos DATE;
DECLARE finish INT DEFAULT 0;
DECLARE cur2 CURSOR FOR SELECT item_repair_code, item_warranty, date_of_purchase,date_of_service FROM repair;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET finish=1;
OPEN cur2;
a:LOOP
FETCH cur2 INTO irc,iw,dop,dos;
SET res = DATEDIFF(dos,dop) DIV 365;
SET res1 = DATEDIFF(NOW(),dop) DIV 365;
IF finish!=1 THEN
IF res<iw THEN
UPDATE repair SET repair.warranty_usage = 'Applied' WHERE item_repair_code = irc;
ELSEIF res>=iw THEN
UPDATE repair SET repair.warranty_usage = 'Not Applied' WHERE item_repair_code = irc;
END IF;
IF res1<iw THEN
UPDATE repair SET repair.current_item_warranty_status = 'Warranty is still Valid' WHERE item_repair_code = irc;
ELSEIF res1>=iw THEN
UPDATE repair SET repair.current_item_warranty_status = 'Warranty has Expired' WHERE item_repair_code = irc;
END IF;
END IF;
IF finish=1 THEN
LEAVE a;
END IF;
END LOOP a;
END $$

DELIMITER;

-- ------------------------------------------------------------------------


-- STORED PROCEDURE
-- ------------------------------------------------------------------------

DELIMITER $$
CREATE PROCEDURE userfeedback(IN fdbc TEXT)
BEGIN
DECLARE feedback TEXT;
DECLARE username TEXT;
DECLARE mail TEXT;
DECLARE pid INT;
DECLARE item_type TEXT;
DECLARE piid INT;
DECLARE riid INT;
DECLARE irc INT;
DECLARE finish INT DEFAULT 0;
DECLARE cur_1 CURSOR FOR SELECT user.user_feedback,user.user_name,user.user_mail,purchase.purchase_id,
purchase.item_type,purchase.item_id,repair.item_repair_code,repair.item_id 
from ((electronic_shop_and_repair_management_364.user INNER JOIN repair ON user.user_id=repair.user_id)
INNER JOIN purchase ON user.user_id=purchase.user_id)
WHERE user_feedback=fdbc;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET finish=1;
OPEN cur_1;
get_user:LOOP
FETCH cur_1 into feedback,username,mail,pid,item_type,piid,irc,riid;
SELECT feedback, username, mail, pid, item_type, piid, irc, riid;
IF finish=1 THEN
LEAVE get_user;
END IF;
END LOOP get_user;
END$$

DELIMITER;

-- ------------------------------------------------------------------------



-- FUNCTIONS
-- ------------------------------------------------------------------------

DELIMITER $$
CREATE FUNCTION Discount_on_Purchase (pid_old INT,pid_new INT)
RETURNS TEXT DETERMINISTIC
BEGIN
DECLARE message TEXT;
DECLARE amt INT;
DECLARE amt2 INT;
SET message = 'Discount has been Applied';
SELECT purchase_amt INTO amt FROM purchase WHERE purchase_id = pid_old;
SELECT purchase_amt INTO amt2 FROM purchase WHERE purchase_id = pid_new;
IF amt<=30000 THEN
SET amt2 = amt2 - amt2*0.1;
ELSEIF (amt > 30000 and amt < 60000) THEN
SET amt2 = amt2 - amt2*0.2;
ELSEIF (amt >= 60000) THEN
SET amt2 = amt2 - amt2*0.3;
END IF;
UPDATE purchase SET purchase_amt=amt2 WHERE purchase_id = pid_new;
RETURN(message);
END$$

DELIMITER ;


DELIMITER $$
CREATE FUNCTION View_discount (pid INT)
RETURNS TEXT DETERMINISTIC
BEGIN 
DECLARE message TEXT;
DECLARE amt INT;
SELECT purchase_amt INTO amt FROM purchase WHERE purchase_id=pid;  
if amt <= 30000 THEN
		SET message = 'You get 10% discount on your next purchase';
	elseif (amt > 30000 and amt < 60000) THEN
		SET message = 'You get 20% discount on your next purchase';
	elseif (amt >= 60000) THEN
		SET message = 'You get 30% discount on your next purchase';
END IF;
RETURN(message);
END $$




 














