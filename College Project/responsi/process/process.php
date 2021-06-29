<?php
require_once 'connection.php';

if(isset($_POST['add'])) {
  $name = $_POST['name'];
  $id_kategori = $_POST['id_kategori'];
  $description = $_POST['description'];
  $harga = $_POST['harga'];
  $image = $_FILES['image'];
  
  $mysqli->query(
    "INSERT INTO tb_barang (nama, id_kategori, description, harga)
    VALUES('$name','$id_kategori','$description','$harga')") or
    die($mysqli->error);

  $highest_idq = $mysqli->query(
    "SELECT MAX(id_barang) FROM tb_barang");
  $current_id = $highest_idq->fetch_assoc()['MAX(id_barang)'];
  $path_parts = pathinfo($_FILES["image"]["name"]);
  $extension = $path_parts['extension'];
  
  $new_file_name = $current_id.'.'.$extension;
  $tname = $_FILES['image']['tmp_name'];
  $upload_dir = '../assets/images';
  move_uploaded_file($tname, $upload_dir.'/'.$new_file_name);

  $mysqli->query(
    "UPDATE tb_barang
    SET image='$new_file_name' 
    WHERE id_barang='$current_id'");

  header('Location: ../views');
}

if(isset($_POST['edit'])) {
  $id_barang = $_POST['id_barang'];
  $name = $_POST['name'];
  $id_kategori = $_POST['id_kategori'];
  $description = $_POST['description'];
  $harga = $_POST['harga'];
  $mysqli->query(
    "UPDATE tb_barang
    SET nama='$name', id_kategori='$id_kategori', description='$description', harga='$harga'
    WHERE id_barang='$id_barang'");
  header('Location: ../views');
}
if(isset($_GET['delete'])) {
  print_r($_GET);
  $id_barang = $_GET['id_barang'];
  $mysqli->query(
    "DELETE FROM tb_barang WHERE id_barang='$id_barang'") or die($mysqli->error);
  header('Location: ../views');
}
?>