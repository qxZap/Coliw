-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Giu 14, 2018 alle 08:48
-- Versione del server: 10.1.31-MariaDB
-- Versione PHP: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aplicatiebd`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `filemanager`
--

CREATE TABLE `filemanager` (
  `istoricComenzi` varchar(255) NOT NULL,
  `indexComanda` int(11) NOT NULL,
  `dataComanda` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `history`
--

CREATE TABLE `history` (
  `username` varchar(255) NOT NULL,
  `command` varchar(255) NOT NULL,
  `output` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `history`
--

INSERT INTO `history` (`username`, `command`, `output`) VALUES
('pla', 'register pla pla pla@bla.ro', 'You`ve been registred and now you`re logged in'),
('pla', 'register pla pla pla@bla.ro', 'You`ve been registred and now you`re logged in'),
('bla', 'history -c', 'History cleared'),
('bla', 'history', 'history -c\n'),
('bla', 'login bla bla', 'Login sucessfull'),
('bla', 'login bla bla', 'Login sucessfull'),
('bla', 'login bla bla', 'Login sucessfull'),
('bla', 'login bla bla', 'Login sucessfull'),
('bla', 'login bla bla', 'Login sucessfull'),
('bla', 'login bla bla', 'Login sucessfull'),
('bla', 'login bla bla', 'Login sucessfull'),
('bla', 'login bla bla', 'Login sucessfull'),
('bla', 'login bla bla', 'Login sucessfull'),
('bla', 'login bla bla', 'Login sucessfull');

-- --------------------------------------------------------

--
-- Struttura della tabella `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `email`) VALUES
(1, 'Olivia', 'olivia', 'olivia@company.com'),
(2, 'Gabi', 'gabi', 'gabi@company.com'),
(3, 'Radu', 'radu', 'radu@company.com'),
(4, 'Mihai', 'mihai', 'mihai@company.com'),
(5, 'Zap', 'Sexmode', 'curwa@da.nu'),
(13, 'Zapzilla', 'zap', 'zap@company.com'),
(14, 'Adevarat', 'zap', 'zap'),
(15, 'Dan', 'amputamica', 'foarte@mica.da'),
(16, 'Robert', 'putamica', 'puta@mica.adevarat'),
(17, 'Dorin', '0cm', '0cm@low.low'),
(18, 'Jimmy', 'jim', 'jim'),
(19, 'yolo', 'yolo', 'yolo'),
(20, 'bla', 'bla', 'bla@gmail.com'),
(21, 'Andrei', 'Pulentor', 'andreiplm@plt.pll'),
(22, 'Salam', 'Gorilla', 'sgm@ssl.ec'),
(23, 'qurtos', 'zap', 'adevarat@qurtos.zap'),
(25, 'pla', 'pla', 'pla@bla.ro');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `filemanager`
--
ALTER TABLE `filemanager`
  ADD PRIMARY KEY (`indexComanda`);

--
-- Indici per le tabelle `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`,`username`,`email`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `filemanager`
--
ALTER TABLE `filemanager`
  MODIFY `indexComanda` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
