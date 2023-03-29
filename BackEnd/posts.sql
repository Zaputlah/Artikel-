-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 29 Mar 2023 pada 12.52
-- Versi server: 10.4.27-MariaDB
-- Versi PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `posts`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `posts`
--

CREATE TABLE `posts` (
  `Id` int(100) NOT NULL,
  `Title` varchar(200) NOT NULL,
  `Content` text NOT NULL,
  `Category` varchar(100) NOT NULL,
  `Created_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Updated_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `Status` enum('Publish','Draft','Thrash','') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `posts`
--

INSERT INTO `posts` (`Id`, `Title`, `Content`, `Category`, `Created_date`, `Updated_date`, `Status`) VALUES
(1, 'Article 1', 'This is the content of article 1', 'Technology', '2023-03-29 07:46:01', '2023-03-29 07:46:01', 'Publish'),
(2, 'Article 2', 'This is the content of article 2', 'Sports', '2023-03-29 07:47:54', '2023-03-29 07:47:54', 'Draft'),
(3, 'Article 3', 'This is the content of article 3', 'Lifestyle', '2023-03-29 07:48:47', '2023-03-29 07:48:47', 'Publish'),
(4, 'Article 4', 'This is the content of article 4', 'Entertainment', '2023-03-29 07:49:42', '2023-03-29 07:49:42', 'Publish'),
(5, 'Article 5', 'This is the content of article 5', 'Education', '2023-03-29 07:50:33', '2023-03-29 07:50:33', 'Draft');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `posts`
--
ALTER TABLE `posts`
  MODIFY `Id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
