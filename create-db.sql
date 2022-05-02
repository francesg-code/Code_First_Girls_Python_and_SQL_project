CREATE DATABASE python_cookbook;
USE python_cookbook;

-- ------------------------------------------------------------------------------------
--Create tables.
-- ------------------------------------------------------------------------------------

CREATE TABLE `recipes` (
  `recipe_id` int NOT NULL AUTO_INCREMENT,
  `recipe_hash` varchar(200) DEFAULT NULL,
  `recipe_label` varchar(200) DEFAULT NULL,
  `recipe_url` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`recipe_id`),
  UNIQUE KEY `recipe_uri_UNIQUE` (`recipe_hash`)
) ENGINE=InnoDB AUTO_INCREMENT=173 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `ingredients` (
  `ingredient_id` int NOT NULL AUTO_INCREMENT,
  `ingredient` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ingredient_id`),
  UNIQUE KEY `ingredient_UNIQUE` (`ingredient`)
) ENGINE=InnoDB AUTO_INCREMENT=710 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `recipes` (CREATE TABLE `measurements` (
  `measurement_id` int NOT NULL AUTO_INCREMENT,
  `measurement` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`measurement_id`),
  UNIQUE KEY `measurement_UNIQUE` (`measurement`)
) ENGINE=InnoDB AUTO_INCREMENT=473 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `units` (
  `unit_id` int NOT NULL AUTO_INCREMENT,
  `unit` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`unit_id`),
  UNIQUE KEY `units_UNIQUE` (`unit`)
) ENGINE=InnoDB AUTO_INCREMENT=443 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `dietary_requirements` (
  `dietary_requirement_id` int NOT NULL AUTO_INCREMENT,
  `dietary_requirement` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`dietary_requirement_id`),
  UNIQUE KEY `dietary_requirement_UNIQUE` (`dietary_requirement`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `recipe_ingredients` (
  `recipe_id` int DEFAULT NULL,
  `ingredient_id` int DEFAULT NULL,
  `measurement_id` int DEFAULT NULL,
  `unit_id` int DEFAULT NULL,
  KEY `ingredient_id_idx` (`ingredient_id`),
  KEY `recipe_id_idx` (`recipe_id`),
  KEY `measurement_id_idx` (`measurement_id`),
  KEY `unit_id_idx` (`unit_id`),
  CONSTRAINT `ri_ingredient_id` FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`ingredient_id`),
  CONSTRAINT `ri_measurement_id` FOREIGN KEY (`measurement_id`) REFERENCES `measurements` (`measurement_id`),
  CONSTRAINT `ri_recipe_id` FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`recipe_id`),
  CONSTRAINT `ri_unit_id` FOREIGN KEY (`unit_id`) REFERENCES `units` (`unit_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `recipe_dietary_req` (
  `recipe_id` int DEFAULT NULL,
  `dietary_requirement_id` int DEFAULT NULL,
  KEY `recipe_id_idx` (`recipe_id`),
  KEY `dietary_requirement_id_idx` (`dietary_requirement_id`),
  CONSTRAINT `dietary_requirement_id` FOREIGN KEY (`dietary_requirement_id`) REFERENCES `dietary_requirements` (`dietary_requirement_id`),
  CONSTRAINT `dr_recipe_id` FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`recipe_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
