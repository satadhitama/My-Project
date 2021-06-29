<?php 
  require_once '../process/connection.php';
  $kategori = $mysqli->query(
    "SELECT * FROM tb_kategori")->fetch_all();
?> 

<div class="main">
  <div class="form-container">
    <h1 class="add-title">Tambah Barang</h1>
    <form action="../process/process.php" method="POST" enctype="multipart/form-data">
      <label for="nama">Nama Barang</label> <br>
      <input name="name" id="nama" type="text"><br>
      <label for="kategori">Kategori</label><br>
      <select name="id_kategori" id="">
        <option value="">Pilih Kategori</option>
        <?php foreach($kategori as $data):?>
        <option value="<?= $data[0];?>"><?= $data[1];?></option>  
        <?php endforeach?>
      </select><br>
      <label for="harga">Harga</label>
      <input type="text" name="harga" id="harga">
      <label for="description">Deskripsi</label><br>
      <textarea name="description" id="description" cols="30" rows="10" charwidth="23" style="resize:vertical"></textarea><br>
      <label for="image">Unggah Gambar</label> <br>
      <input method="file" type="File" name="image">
      <input name="add" class="btn add" type="submit">
    </form>
  </div>
</div>