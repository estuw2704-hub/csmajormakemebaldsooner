-- Database Rumah Sakit (untuk MySQL Workbench 8.0)
DROP SCHEMA IF EXISTS `Rumah_Sakit`;
CREATE SCHEMA `Rumah_Sakit` DEFAULT CHARACTER SET utf8mb4;
USE `Rumah_Sakit`;

-- Entitas Kamar
CREATE TABLE `Kamar` (
  `kode_kamar` VARCHAR(15) NOT NULL,
  `nama_kamar` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`kode_kamar`)
) ENGINE=InnoDB;

-- Entitas Dokter
CREATE TABLE `Dokter` (
  `kode_dokter` VARCHAR(15) NOT NULL,
  `nama_dokter` VARCHAR(25) NOT NULL,
  `notelp_dokter` VARCHAR(20) NULL,
  `keahlian` VARCHAR(20) NULL,
  PRIMARY KEY (`kode_dokter`)
) ENGINE=InnoDB;

-- Entitas Pasien
-- alamat_pasien = atribut composite (jalan, NoRmh, kecamatan, kabupaten)
-- Relasi 1:n Kamar -> Pasien (FK di Pasien)
CREATE TABLE `Pasien` (
  `no_pasien` INT NOT NULL,
  `nama_pasien` VARCHAR(25) NOT NULL,
  `alamat_jalan` VARCHAR(30) NULL,
  `alamat_NoRmh` INT NULL,
  `alamat_kecamatan` VARCHAR(25) NULL,
  `alamat_kabupaten` VARCHAR(25) NULL,
  `Kamar_kode_kamar` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`no_pasien`),
  INDEX `fk_Pasien_Kamar_idx` (`Kamar_kode_kamar`),
  CONSTRAINT `fk_Pasien_Kamar`
    FOREIGN KEY (`Kamar_kode_kamar`) REFERENCES `Kamar` (`kode_kamar`)
    ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB;

-- Atribut multivalue data_penyakit -> tabel tersendiri
CREATE TABLE `Penyakit_Pasien` (
  `penyakit` VARCHAR(30) NOT NULL,
  `Pasien_no_pasien` INT NOT NULL,
  PRIMARY KEY (`penyakit`, `Pasien_no_pasien`),
  INDEX `fk_Penyakit_Pasien_idx` (`Pasien_no_pasien`),
  CONSTRAINT `fk_Penyakit_Pasien`
    FOREIGN KEY (`Pasien_no_pasien`) REFERENCES `Pasien` (`no_pasien`)
    ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB;

-- Entitas Obat
CREATE TABLE `Obat` (
  `kode_obat` VARCHAR(15) NOT NULL,
  `nama_obat` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`kode_obat`)
) ENGINE=InnoDB;

-- Atribut multivalue kegunaan -> tabel tersendiri
CREATE TABLE `Kegunaan_Obat` (
  `kegunaan` VARCHAR(45) NOT NULL,
  `Obat_kode_obat` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`kegunaan`, `Obat_kode_obat`),
  INDEX `fk_Kegunaan_Obat_idx` (`Obat_kode_obat`),
  CONSTRAINT `fk_Kegunaan_Obat`
    FOREIGN KEY (`Obat_kode_obat`) REFERENCES `Obat` (`kode_obat`)
    ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB;

-- Relasi m:n Dokter <-> Pasien
CREATE TABLE `Dokter_has_Pasien` (
  `Dokter_kode_dokter` VARCHAR(15) NOT NULL,
  `Pasien_no_pasien` INT NOT NULL,
  PRIMARY KEY (`Dokter_kode_dokter`, `Pasien_no_pasien`),
  INDEX `fk_DHP_Pasien_idx` (`Pasien_no_pasien`),
  CONSTRAINT `fk_DHP_Dokter`
    FOREIGN KEY (`Dokter_kode_dokter`) REFERENCES `Dokter` (`kode_dokter`)
    ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_DHP_Pasien`
    FOREIGN KEY (`Pasien_no_pasien`) REFERENCES `Pasien` (`no_pasien`)
    ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB;

-- Relasi m:n Pasien <-> Obat
CREATE TABLE `Pasien_has_Obat` (
  `Pasien_no_pasien` INT NOT NULL,
  `Obat_kode_obat` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`Pasien_no_pasien`, `Obat_kode_obat`),
  INDEX `fk_PHO_Obat_idx` (`Obat_kode_obat`),
  CONSTRAINT `fk_PHO_Pasien`
    FOREIGN KEY (`Pasien_no_pasien`) REFERENCES `Pasien` (`no_pasien`)
    ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_PHO_Obat`
    FOREIGN KEY (`Obat_kode_obat`) REFERENCES `Obat` (`kode_obat`)
    ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB;
