<?php 

  require_once '../process/connection.php';
  $id_barang = $_GET['id'];
  $result = $mysqli->query(
    "SELECT * FROM tb_barang
    WHERE id_barang='$id_barang'")->fetch_assoc();
  $kategori = $mysqli->query(
    "SELECT * FROM tb_kategori")->fetch_all();
?> 

<div class="main">
  <div class="form-container">
    <h1 class="add-title">Edit Barang</h1>
    <form action="../process/process.php" method="POST">
      <input name='id_barang' value="<?= $id_barang?>" type="hidden">
      <label for="nama">Nama Barang</label> <br>
      <input name="name" id="nama" type="text" value="<?= $result['nama']?>"><br>
      <label for="kategori">Kategori</label><br>
      <select name="id_kategori" id="">
        <option value="">Pilih Kategori</option>
        <?php foreach($kategori as $data):?>
        <option value="<?= $data[0];?>"><?= $data[1];?></option>  
        <?php endforeach?>
      </select><br>
      <label for="harga">Harga</label>
      <input type="text" name="harga" id="harga" value="<?= $result['harga'];?>">
      <label for="description">Deskripsi</label><br>
      <textarea name="description" id="description" cols="30" rows="10" charwidth="23" style="resize:vertical"><?= $result['description'];?></textarea><br>
      <input name="edit" class="btn edit" type="submit">
    </form>
  </div>
</div>