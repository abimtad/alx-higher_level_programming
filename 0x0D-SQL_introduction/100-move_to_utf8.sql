-- converts hbtn_0c_0 database to UTF8
-- converts hbtn_0c_0, first_table and field_name specifically
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
