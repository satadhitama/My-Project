const closeModal = document.querySelector(".close-modal");
const sidebar = document.querySelector(".sidebar");
const modalPop = document.querySelector(".side-pop");
const modalButton = document.querySelector(".open-sidebar");
const sidePop = document.querySelector(".side-pop");

// Opening sidebar
modalButton.addEventListener("click", ()=> {
  sidebar.classList.add("sidebar-active");
  modalPop.classList.add("active")
  closeModal.classList.add("active");
});

// Closing sidebar
closeModal.addEventListener("click", ()=> {
  sidebar.classList.remove("sidebar-active");
  modalPop.classList.remove("active")
  closeModal.classList.remove("active");
});

sidePop.addEventListener("click", ()=>{
  sidebar.classList.remove("sidebar-active");
  modalPop.classList.remove("active")
  closeModal.classList.remove("active");
});

// Sidebar category
const categoryTitle = document.querySelector(".sidebar-category");
const categoryContent = document.querySelector(".category-content");
categoryTitle.addEventListener("click", ()=> {
  categoryContent.classList.toggle("category-active");
});
