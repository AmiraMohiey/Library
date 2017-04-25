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
-- Table structure for table `library_book`
--

CREATE TABLE `library_book` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `published_at` date DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `link` varchar(200) DEFAULT NULL,
  `picture_url` varchar(100) DEFAULT NULL,
  `author_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `library_book`
--

INSERT INTO `library_book` (`id`, `title`, `published_at`, `country`, `link`, `picture_url`, `author_id`, `category_id`) VALUES
(1, 'The Time Machine', '1895-01-01', 'United Kingdom', 'https://books.google.com.eg/books?id=dQ5Yjz02uuIC&dq=the+time+machine&hl=en&sa=X&ved=0ahUKEwjfs52h_K3TAhWJORoKHUh2CigQ6AEIIDAA', 'library/static/images/book/20170425142421/time.jpg', 1, 1),
(2, 'The War of the Worlds', '1898-01-01', 'United Kingdom', 'https://books.google.com.eg/books?id=q7yKBAAAQBAJ&printsec=frontcover&dq=The+War+of+the+Worlds&hl=en&sa=X&ved=0ahUKEwj4hubH_K3TAhXHExoKHQQmBRIQ6AEIIDAA#v=onepage&q=The%20War%20of%20the%20Worlds&f=fals', 'library/static/images/book/20170425143257/warofworlds.jpg', 1, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `library_book`
--
ALTER TABLE `library_book`
  ADD PRIMARY KEY (`id`),
  ADD KEY `library_book_author_id_d9a3b67e_fk_library_author_id` (`author_id`),
  ADD KEY `library_book_category_id_c90a2d6d_fk_library_category_id` (`category_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `library_book`
--
ALTER TABLE `library_book`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `library_book`
--
ALTER TABLE `library_book`
  ADD CONSTRAINT `library_book_author_id_d9a3b67e_fk_library_author_id` FOREIGN KEY (`author_id`) REFERENCES `library_author` (`id`),
  ADD CONSTRAINT `library_book_category_id_c90a2d6d_fk_library_category_id` FOREIGN KEY (`category_id`) REFERENCES `library_category` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
