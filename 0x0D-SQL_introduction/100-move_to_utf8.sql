-- converts hbtn_0c-0 DB to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- convert hbtn_0c_0, first_table, name 

USE `hbtn_0c_0`
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

