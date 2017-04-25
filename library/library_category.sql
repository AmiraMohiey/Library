-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 25, 2017 at 11:41 AM
-- Server version: 5.7.17-0ubuntu1
-- PHP Version: 7.0.15-1ubuntu4

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
-- Table structure for table `library_category`
--

CREATE TABLE `library_category` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `picture_url` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `library_category`
--

INSERT INTO `library_category` (`id`, `name`, `description`, `picture_url`) VALUES
(1, 'Science Fiction', 'Science Fiction is a broad genre that can be set in almost any time and place:  past, present, future, Earth, alien planet, space ship, you name it, sci-fi can encompass it.  Sci-fi writing is often heavily based in technology and usually contains an underlying question—what if society were different in one very fundamental way?  What would happen?  Sub-genres include:  steampunk, cyberpunk, lab-lit, and more.  Also goes by the name Speculative Fiction, or Spec-fic.', 'images/science-fiction.jpg'),
(2, 'Fantasy', 'A genre of fiction usually set in another world and populated with humans as well as non-human creatures.  Elements of mythology are usually present and world building is crucial to this genre.  A good and highly effective fantasy story will transport the reader completely to another world.  That is not to say however, that tough subjects cannot be masterfully covered in the fantasy genre.', 'images/fantasy.jpg'),
(3, 'Paranormal', 'The Paranormal genre of writing deals with the supernatural; things that cannot be easily explained in day to day life.  Ghosts, spirits, and strange happenings are common themes in Paranormal writing.  Paranormal fiction and Mystery fiction are both similar in that they deal with the unexplained, however, the Paranormal genre almost always finds its answers (if any answers are to be found) outside of the norms of everyday life.', 'images/paranormal.jpg'),
(4, 'mystry', 'Mystery novels involve intricate plotting with clues and a combination of gathering information,  deductions derived by reasoning, and inference to solve a puzzle or a crime. The protagonist is unusually challenged by the protagonist such as in the classic Sherlock Holmes Detective series.  Mysteries can also be thrillers when a ticking clock is added to create suspense.  The protagonist faces many close calls and must overcome challenging obstacles before she can save the day.', 'images/mystry.jpg'),
(5, 'Romantic', 'The basis of romantic fiction is that it contains a central love story, has an optimistic ending, and is emotionally satisfying.  There are many categories in this genre from sweet romantic cozy stories to sizzling  romances . The romance genre occupies the largest share of the U.S. consumer fiction market. Its sales double any other category of fiction.', 'images/romance.jpg'),
(6, 'Historical', 'Historical fiction are stories that take place in time at least three generations (roughly 50 to 75 years) ago. They need to  be accurate as far as technology, dress, habits, historical events,  and mores of the time and place in which the stories are situated.', 'images/historical.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `library_category`
--
ALTER TABLE `library_category`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `library_category`
--
ALTER TABLE `library_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
