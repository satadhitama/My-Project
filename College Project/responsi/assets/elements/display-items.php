<?php require_once '../process/connection.php';?> 

<div class="main">
  <div class="display-container">
    <?php 
      $result = array();
      if(count($_GET) > 0) {
        $id_kategori = $_GET['id_kategori'];
        $result_kategori = $mysqli->query(
          "SELECT * FROM tb_barang
          JOIN tb_kategori
          ON  tb_kategori.id_kategori =  tb_barang.id_kategori
          WHERE tb_barang.id_kategori = '$id_kategori'
          ORDER BY tb_barang.id_barang ASC");
        $result = mysqli_fetch_all($result_kategori, MYSQLI_ASSOC);
      }
      else if (count($_GET) === 0){
        $result_all = $mysqli->query(
          "SELECT * FROM tb_barang
          JOIN tb_kategori
          ON tb_kategori.id_kategori =  tb_barang.id_kategori
          ORDER BY tb_barang.id_barang ASC");
        $result = mysqli_fetch_all($result_all, MYSQLI_ASSOC);
      }
        foreach ($result as $data):
      ?>
    <div class="card">
      <div class="card-container">
        <div class="image-container" style="background-image: url(../assets/images/<?= $data['image'];?>);"></div>
        <div class="card-content">
          <a href="http://localhost/responsi/views/item-detail.php?id=<?= $data['id_barang'];?>"> <h1 class="card-title"><?= $data['nama'];?></h1></a>
          <h3 class="card-category"><?= $data['kategori'];?></h3>
          <div class="rating">
            <?php for ($i=0; $i < $data['rating']; $i++): ?>
            <h5 class="star"><i class="fa fa-star"></i></h5>
            <?php endfor;?>
          </div>
          <h2 class="price">IDR<?= $data['harga']?></h2>
        </div>
      </div>
    </div>
    <?php endforeach;?>
  </div>
</div>