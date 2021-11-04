-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Nov 03, 2021 at 11:27 PM
-- Server version: 5.7.34
-- PHP Version: 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `srijas`
--

-- --------------------------------------------------------

--
-- Table structure for table `job_master`
--

CREATE TABLE `job_master` (
  `job_id` int(11) NOT NULL,
  `job_title` varchar(100) NOT NULL,
  `is_active` bit(1) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` int(11) NOT NULL,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `job_master`
--

INSERT INTO `job_master` (`job_id`, `job_title`, `is_active`, `created_by`, `created_at`, `updated_by`, `updated_at`) VALUES
(1, 'Software Engineer', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(2, 'Software Developer', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(3, 'Software Engineer Intern', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(4, 'Software Developer Intern', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04');

-- --------------------------------------------------------

--
-- Table structure for table `resume_master`
--

CREATE TABLE `resume_master` (
  `resume_id` int(11) NOT NULL,
  `resume_json` longtext NOT NULL,
  `resume_universities` varchar(1000) DEFAULT NULL,
  `resume_degrees` varchar(1000) NOT NULL,
  `resume_links` varchar(1000) NOT NULL,
  `resume_summary` varchar(1000) NOT NULL,
  `is_active` bit(1) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` int(11) NOT NULL,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `resume_skills`
--

CREATE TABLE `resume_skills` (
  `resume_skill_id` int(11) NOT NULL,
  `resume_id` int(11) NOT NULL,
  `skill_id` int(11) NOT NULL,
  `is_active` bit(1) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` int(11) NOT NULL,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `skill_master`
--

CREATE TABLE `skill_master` (
  `skill_id` int(11) NOT NULL,
  `skill_title` varchar(100) NOT NULL,
  `is_active` bit(1) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` int(11) NOT NULL,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `skill_master`
--

INSERT INTO `skill_master` (`skill_id`, `skill_title`, `is_active`, `created_by`, `created_at`, `updated_by`, `updated_at`) VALUES
(1, 'C', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(2, 'Java', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(3, 'Python', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(4, 'C++', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(5, 'C#', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(6, 'Visual Basic', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(7, 'JavaScript', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(8, 'Assembly Language', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(9, 'PHP', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(10, 'SQL', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(11, 'Classic Visual Basic', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(12, 'Delphi/Object Pascal', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(13, 'Ruby', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(14, 'Go', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(15, 'Swift', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(16, 'R', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(17, 'Groovy', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(18, 'Perl', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(19, 'MATLAB', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04'),
(20, 'Fortran', b'1', -1, '2021-11-02 04:39:04', 0, '2021-11-02 04:39:04');

-- --------------------------------------------------------

--
-- Table structure for table `user_master`
--

CREATE TABLE `user_master` (
  `user_id` int(11) NOT NULL,
  `user_fname` varchar(50) NOT NULL,
  `user_lname` varchar(50) DEFAULT NULL,
  `user_email` varchar(50) NOT NULL,
  `location` varchar(50) DEFAULT NULL,
  `user_preferred_job_id` int(11) NOT NULL,
  `is_active` bit(1) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_resume`
--

CREATE TABLE `user_resume` (
  `user_resume_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `resume_id` int(11) NOT NULL,
  `is_active` bit(1) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` int(11) NOT NULL,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `job_master`
--
ALTER TABLE `job_master`
  ADD PRIMARY KEY (`job_id`);

--
-- Indexes for table `resume_master`
--
ALTER TABLE `resume_master`
  ADD PRIMARY KEY (`resume_id`);

--
-- Indexes for table `resume_skills`
--
ALTER TABLE `resume_skills`
  ADD PRIMARY KEY (`resume_skill_id`),
  ADD KEY `resume_skills_resume_fk` (`resume_id`),
  ADD KEY `resume_skills_skills_fk` (`skill_id`);

--
-- Indexes for table `skill_master`
--
ALTER TABLE `skill_master`
  ADD PRIMARY KEY (`skill_id`);

--
-- Indexes for table `user_master`
--
ALTER TABLE `user_master`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `user_job_fk` (`user_preferred_job_id`);

--
-- Indexes for table `user_resume`
--
ALTER TABLE `user_resume`
  ADD PRIMARY KEY (`user_resume_id`),
  ADD KEY `user_resume_user_fk` (`user_id`),
  ADD KEY `user_resume_resume_fk` (`resume_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `job_master`
--
ALTER TABLE `job_master`
  MODIFY `job_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `resume_master`
--
ALTER TABLE `resume_master`
  MODIFY `resume_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `resume_skills`
--
ALTER TABLE `resume_skills`
  MODIFY `resume_skill_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `skill_master`
--
ALTER TABLE `skill_master`
  MODIFY `skill_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `user_master`
--
ALTER TABLE `user_master`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_resume`
--
ALTER TABLE `user_resume`
  MODIFY `user_resume_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `resume_skills`
--
ALTER TABLE `resume_skills`
  ADD CONSTRAINT `resume_skills_resume_fk` FOREIGN KEY (`resume_id`) REFERENCES `resume_master` (`resume_id`),
  ADD CONSTRAINT `resume_skills_skills_fk` FOREIGN KEY (`skill_id`) REFERENCES `skill_master` (`skill_id`);

--
-- Constraints for table `user_master`
--
ALTER TABLE `user_master`
  ADD CONSTRAINT `user_job_fk` FOREIGN KEY (`user_preferred_job_id`) REFERENCES `job_master` (`job_id`);

--
-- Constraints for table `user_resume`
--
ALTER TABLE `user_resume`
  ADD CONSTRAINT `user_resume_resume_fk` FOREIGN KEY (`resume_id`) REFERENCES `resume_master` (`resume_id`),
  ADD CONSTRAINT `user_resume_user_fk` FOREIGN KEY (`user_id`) REFERENCES `user_master` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
