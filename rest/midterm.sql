-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 04, 2021 at 09:33 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `midterm`
--

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `NIM` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `prodi` varchar(50) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `angkatan` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mahasiswa`
--

INSERT INTO `mahasiswa` (`NIM`, `nama`, `prodi`, `gender`, `angkatan`) VALUES
(192102001, 'agnes silvina', 'informatika', 'P', 2019),
(192102002, 'akhmad faizal', 'informatika', 'L', 2019),
(192102003, 'alfabeth danuningrat', 'informatika', 'L', 2019),
(192102004, 'azzahra trista', 'informatika', 'P', 2019);

-- --------------------------------------------------------

--
-- Table structure for table `matakuliah`
--

CREATE TABLE `matakuliah` (
  `kode` int(11) NOT NULL,
  `nama_mk` varchar(200) NOT NULL,
  `sks` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `matakuliah`
--

INSERT INTO `matakuliah` (`kode`, `nama_mk`, `sks`) VALUES
(1, 'PAWL', 4),
(2, 'DWBD', 4),
(3, 'DPAPI', 3),
(4, 'KPL', 4);

-- --------------------------------------------------------

--
-- Table structure for table `nilai_mk`
--

CREATE TABLE `nilai_mk` (
  `id` int(11) NOT NULL,
  `nim` int(11) DEFAULT NULL,
  `kode_mk` int(11) DEFAULT NULL,
  `nilai` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `nilai_mk`
--

INSERT INTO `nilai_mk` (`id`, `nim`, `kode_mk`, `nilai`) VALUES
(2, 192102002, 4, 'A'),
(3, 192102003, 2, 'B'),
(4, 192102004, 3, 'B'),
(7, 192102001, 4, 'A'),
(9, 192102002, 2, 'C'),
(10, 192102002, 1, 'A'),
(11, 192102003, 1, 'A'),
(12, 192102003, 3, 'D'),
(13, 192102003, 4, 'B'),
(14, 192102004, 1, 'B'),
(15, 192102004, 2, 'B'),
(16, 192102004, 4, 'B');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`NIM`);

--
-- Indexes for table `matakuliah`
--
ALTER TABLE `matakuliah`
  ADD PRIMARY KEY (`kode`);

--
-- Indexes for table `nilai_mk`
--
ALTER TABLE `nilai_mk`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nim` (`nim`),
  ADD KEY `kode_mk` (`kode_mk`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  MODIFY `NIM` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=192102011;

--
-- AUTO_INCREMENT for table `matakuliah`
--
ALTER TABLE `matakuliah`
  MODIFY `kode` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `nilai_mk`
--
ALTER TABLE `nilai_mk`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `nilai_mk`
--
ALTER TABLE `nilai_mk`
  ADD CONSTRAINT `nilai_mk_ibfk_1` FOREIGN KEY (`nim`) REFERENCES `mahasiswa` (`NIM`) ON DELETE CASCADE,
  ADD CONSTRAINT `nilai_mk_ibfk_2` FOREIGN KEY (`kode_mk`) REFERENCES `matakuliah` (`kode`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
