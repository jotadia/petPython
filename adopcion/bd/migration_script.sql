-- ----------------------------------------------------------------------------
-- MySQL Workbench Migration
-- Migrated Schemata: biblioteca
-- Source Schemata: biblioteca
-- Created: Tue Aug 18 07:57:07 2026
-- Workbench Version: 8.0.47
-- ----------------------------------------------------------------------------

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------------------------------------------------------
-- Schema biblioteca
-- ----------------------------------------------------------------------------
DROP SCHEMA IF EXISTS `biblioteca` ;
CREATE SCHEMA IF NOT EXISTS `biblioteca` ;

-- ----------------------------------------------------------------------------
-- Table biblioteca.libros
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`libros` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(100) NOT NULL,
  `autor` VARCHAR(100) NOT NULL,
  `anio_publicacion` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table biblioteca.prestamos
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`prestamos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_usuario` INT NOT NULL,
  `id_libro` INT NOT NULL,
  `fecha_prestamo` DATE NOT NULL,
  `fecha_devolucion` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_prestamos_libros_idx` (`id_libro` ASC) VISIBLE,
  INDEX `fk_prestamos_usuario` (`id_usuario` ASC) VISIBLE,
  CONSTRAINT `fk_prestamos_libros`
    FOREIGN KEY (`id_libro`)
    REFERENCES `biblioteca`.`libros` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_prestamos_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `biblioteca`.`usuarios` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table biblioteca.usuarios
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `correo` VARCHAR(100) NULL DEFAULT NULL,
  `telefono` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `correo` (`correo` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;
SET FOREIGN_KEY_CHECKS = 1;
