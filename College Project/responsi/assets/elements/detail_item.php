<?php
    require_once '../process/connection.php';
    $id_barang = $_GET['id'];
    $result = $mysqli->query(
      "SELECT * FROM tb_barang
      WHERE id_barang='$id_barang'")->fetch_assoc();
    $kategori = $mysqli->query(
      "SELECT kategori FROM tb_kategori
      WHERE id_kategori = $result[id_kategori]")->fetch_assoc();
  ?>
  <div class="main">
    <div class="detail">
      <div class="detail-header">
      <div class="image-container" style="background-image: url(../assets/images/<?= $result['image'];?>);"></div>
       <div class="item-detail">
         <h1 class="card-title"><?= $result['nama'];?></h1>
         <h3 class="card-category"><?= $kategori['kategori'];?></h3>
         <div class="rating">
            <?php for ($i=0; $i < $result['rating']; $i++): ?>
            <h5 class="star"><i class="fa fa-star"></i></h5>
            <?php endfor;?>
          </div>
         <h2 class="price">IDR<?= $result['harga']?></h2>
       </div>
      </div>
      <div class="description">
        <p><?= $result['description']?></p>
      </div>
      <div class="button-container">
        <a class="btn edit" href="../views/edit-item.php?id=<?= $result['id_barang'];?>">Edit</a>
        <form action="../process/process.php" method="GET">
          <input name="id_barang" value="<?= $result['id_barang'];?>" type="hidden">
          <input onclick="return confirm('Do you want to delete?')" name="delete" type="submit" class="btn delete" value="Delete" style="">
        </form>
      </div>
    </div> 
  </div>