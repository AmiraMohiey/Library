-- phpMyAdmin SQL Dump
-- version 4.6.4deb1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 25, 2017 at 05:34 PM
-- Server version: 5.7.17-0ubuntu0.16.10.1
-- PHP Version: 7.0.15-0ubuntu0.16.10.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bookstore`
--

-- --------------------------------------------------------

--
-- Table structure for table `library_author`
--

CREATE TABLE `library_author` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `born_at` date DEFAULT NULL,
  `died_at` date DEFAULT NULL,
  `website` varchar(100) DEFAULT NULL,
  `bio` longtext,
  `picture_url` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `library_author`
--

INSERT INTO `library_author` (`id`, `name`, `born_at`, `died_at`, `website`, `bio`, `picture_url`) VALUES
(1, 'H. G. Wells', '1866-09-21', '1946-08-13', 'https://ffrf.org/news/day/dayitems/item/14557-h-g-wells', 'Herbert George Wells was born at Atlas House, 46 High Street in Bromley, Kent,[11] on 21 September 1866.[4] Called "Bertie" in the family, he was the fourth and last child of Joseph Wells (a former domestic gardener, and at the time a shopkeeper and professional cricketer) and his wife, Sarah Neal (a former domestic servant). An inheritance had allowed the family to acquire a shop in which they sold china and sporting goods, although it failed to prosper: the stock was old and worn out, and the location was poor. Joseph Wells managed to earn a meagre income, but little of it came from the shop and he received an unsteady amount of money from playing professional cricket for the Kent county team.[12] Payment for skilled bowlers and batsmen came from voluntary donations afterwards, or from small payments from the clubs where matches were played.', 'library/static/images/author/20170425142853/hgwells.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `library_author`
--
ALTER TABLE `library_author`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `library_author`
--
ALTER TABLE `library_author`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
