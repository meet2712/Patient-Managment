-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3302
-- Generation Time: Jan 06, 2021 at 06:24 AM
-- Server version: 5.7.21
-- PHP Version: 5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hms`
--

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
CREATE TABLE IF NOT EXISTS `doctor` (
  `doc_id` int(11) NOT NULL,
  `doc_name` varchar(20) NOT NULL,
  `doc_type` varchar(30) NOT NULL,
  `doc_ph_no` int(11) NOT NULL,
  `doc_email` varchar(30) NOT NULL,
  PRIMARY KEY (`doc_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`doc_id`, `doc_name`, `doc_type`, `doc_ph_no`, `doc_email`) VALUES
(1, 'suresh', 'dentist', 909878675, ''),
(2, 'krishna iyer', 'cardiologist', 923644765, '');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
CREATE TABLE IF NOT EXISTS `patient` (
  `p_id` int(10) NOT NULL,
  `p_name` varchar(20) NOT NULL,
  `p_ph_no` int(11) NOT NULL,
  `report_id` int(10) NOT NULL,
  PRIMARY KEY (`p_id`),
  KEY `report_id` (`report_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`p_id`, `p_name`, `p_ph_no`, `report_id`) VALUES
(1, 'hiren koradiya', 987654321, 1),
(2, 'dixit', 987876567, 2);

-- --------------------------------------------------------

--
-- Table structure for table `reports`
--

DROP TABLE IF EXISTS `reports`;
CREATE TABLE IF NOT EXISTS `reports` (
  `report_id` int(10) NOT NULL,
  `report_type` varchar(30) NOT NULL,
  `p_id` int(10) NOT NULL,
  UNIQUE KEY `p_id` (`p_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reports`
--

INSERT INTO `reports` (`report_id`, `report_type`, `p_id`) VALUES
(1, 'urin test', 1),
(2, 'blood test', 2);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
