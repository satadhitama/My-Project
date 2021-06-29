-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 24, 2021 at 11:44 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_electronic_store`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_barang`
--

CREATE TABLE `tb_barang` (
  `id_barang` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `id_kategori` int(11) NOT NULL,
  `harga` int(11) NOT NULL,
  `image` varchar(50) NOT NULL,
  `rating` int(5) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_barang`
--

INSERT INTO `tb_barang` (`id_barang`, `nama`, `id_kategori`, `harga`, `image`, `rating`, `description`) VALUES
(1, 'Iphone 12 Pro Max', 0, 26000000, '1.jpg', 5, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, necessitatibus voluptate et recusandae nam quasi? Praesentium, fugit vero cupiditate sit placeat ratione minima, tempore in exercitationem ullam fugiat ducimus natus modi ea quae? Omnis, nesciunt dolorum quas dolore dicta fugiat quisquam quidem veniam quis. Voluptas qui eum sed laboriosam similique obcaecati ad est! Quod odit, optio ea dolorum natus assumenda ut aut doloribus dolores sed quibusdam molestias animi sint nobis expedita fugiat illum? Excepturi ex libero explicabo voluptates velit fuga nihil maiores, consequatur beatae assumenda repellat cumque eveniet dignissimos accusantium nulla labore ducimus? Officiis provident facilis beatae id eius nihil quis amet ea esse? Sint iusto nostrum aliquam laborum voluptatem illum, sapiente voluptatum optio dolore provident reiciendis ratione cum impedit ullam maiores cumque vel exercitationem magnam dicta qui, et saepe incidunt accusantium. Sed perspiciatis eum vitae fugiat ullam quam dolorem laboriosam possimus, ipsa quisquam! Labore tempore modi tenetur qui, ipsum tempora delectus velit mollitia enim aperiam id vel eius adipisci ea illum error deserunt minima nihil. Blanditiis, tenetur, quam, eius dolor quis asperiores atque doloribus incidunt laudantium autem qui. Consectetur, sequi illo assumenda obcaecati quae molestias aliquid perferendis molestiae earum totam neque, nisi quam iusto magni, esse ipsa culpa iste?\r\n'),
(2, 'ROG', 1, 20810000, '2.jpg', 4, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur facere eum dolorem, consequuntur ipsa illum labore voluptates nam ratione eos corrupti reprehenderit vel. Commodi deleniti vel unde culpa, quae quam est ratione. Praesentium ducimus impedit accusamus omnis voluptatibus eaque itaque veniam porro velit, a minima facere, sed, totam non maxime commodi! Architecto hic sint id rerum rem quo beatae nihil. Maxime accusamus in repellendus quam. Eaque velit earum nostrum voluptatibus suscipit magnam dolorem, accusantium animi ea sequi, modi odit ullam vel ratione reiciendis non nemo amet totam! Praesentium ipsum laborum tempore quis vel? Nisi architecto incidunt necessitatibus adipisci omnis quam provident, enim ut corrupti, repudiandae recusandae sit exercitationem magnam officiis, veniam porro hic quidem illum libero possimus eum dignissimos ipsam pariatur? Veniam itaque excepturi voluptates vero accusamus quia error nesciunt officia quisquam. Veniam accusantium, sequi odit reprehenderit, exercitationem nostrum delectus consequatur voluptate provident ut cupiditate culpa maiores? Earum ipsa laborum esse recusandae! Eos error iure molestiae voluptate quibusdam qui odit distinctio ducimus veritatis natus explicabo, impedit nobis architecto aliquam rem minima culpa quo animi laboriosam. Earum cum eius iure voluptas ratione modi laboriosam, quos quasi quas, fuga ex eligendi repudiandae necessitatibus, fugit omnis animi laborm vitae odio nostrum at. Quae.\r\n'),
(8, 'Oppo Reno 5 Pro 5G', 2, 4000000, '8.jpg', 0, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam et reiciendis impedit eos veritatis dolores adipisci perferendis quis magni labore culpa explicabo, quia saepe hic unde aliquam asperiores debitis nam mollitia sed. Et magnam labore eligendi sequi quod. Quod odit esse atque perferendis incidunt blanditiis quo? Inventore, accusamus asperiores! Reiciendis consequuntur excepturi itaque quis reprehenderit mollitia laboriosam delectus vel nobis officiis neque nulla minima aliquid explicabo soluta sit tempora sapiente sed, quasi voluptates optio provident laborum et. Placeat officia iure consequatur totam, nesciunt non assumenda minima dignissimos itaque nobis vero numquam sunt. Eveniet consectetur inventore dolor, deleniti aut necessitatibus earum, cum at, quo perspiciatis quam repudiandae. Aperiam inventore sunt explicabo obcaecati molestiae, maiores reiciendis voluptates cupiditate. Incidunt a asperiores quos quae modi ex, debitis rem facilis reiciendis optio ullam mollitia eligendi, quibusdam deserunt exercitationem delectus molestiae doloribus in doloremque quam, nisi ut! Illo dicta unde itaque, nesciunt recusandae eius quasi, inventore impedit ut adipisci, optio eum aliquam enim. Ipsam, ducimus aperiam impedit aliquid quae voluptatibus, laudantium recusandae a eum dolore maxime eaque et error adipisci tempore rerum odio sed soluta quis ad enim beatae? Deserunt quos autem dignissimos molestiae vitae est quaerat obcaecati error consectetur nostrum consequuntur corrupti, debitis nulla. Minus, provident. Accusamus minima voluptatum eum facilis aperiam cumque dignissimos omnis voluptas hic doloribus neque illo necessitatibus, fugit ducimus. Officia cumque porro quibusdam dolore quaerat. Vero voluptatum voluptas placeat, tempore corrupti perspiciatis ab nostrum sit, laborum quisquam a voluptatem quos! Fugiat officia eveniet cum consequatur, distinctio illo reprehenderit reiciendis voluptate doloremque omnis aliquid deleniti culpa quia suscipit veritatis aut non, ratione dolore laudantium! Repudiandae excepturi molestiae laborum nemo nihil eius aut necessitatibus porro fugiat soluta dolore ab ad enim consequatur modi quod minima aliquid, est doloremque, velit exercitationem. Corporis asperiores sapiente tempora praesentium in, saepe ea, explicabo voluptatem quae sint similique animi facilis inventore sequi cumque doloribus modi distinctio eum cum neque enim rerum libero laborum aliquid! Id, corrupti ex dolorem vero voluptatem et rem soluta temporibus iste repellendus quidem iure aut quam vel, harum doloremque repellat cum? Illum dolorem et corporis quisquam, sequi repudiandae dolorum omnis maiores, soluta magnam nulla officiis doloribus labore repellendus est nobis aut enim iure, laboriosam dicta veniam cum! Aperiam totam odio quam nulla mollitia eum magnam laboriosam voluptas. Odit veritatis nesciunt distinctio voluptate rem rerum quos possimus incidunt, placeat autem provident dolorem reiciendis reprehenderit aliquid quidem deleniti sint ut est ratione? Nemo, aliquam tempore.\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `tb_kategori`
--

CREATE TABLE `tb_kategori` (
  `id_kategori` int(11) NOT NULL,
  `kategori` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_kategori`
--

INSERT INTO `tb_kategori` (`id_kategori`, `kategori`) VALUES
(1, 'Laptop'),
(2, 'Handphone'),
(3, 'Accessories');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_barang`
--
ALTER TABLE `tb_barang`
  ADD PRIMARY KEY (`id_barang`);

--
-- Indexes for table `tb_kategori`
--
ALTER TABLE `tb_kategori`
  ADD PRIMARY KEY (`id_kategori`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_barang`
--
ALTER TABLE `tb_barang`
  MODIFY `id_barang` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tb_kategori`
--
ALTER TABLE `tb_kategori`
  MODIFY `id_kategori` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
