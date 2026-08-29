// Verhaal-carrousel: projectcover opent een schermvullende fotoviewer.
// Geen bibliotheek; scroll-snap doet het swipen, dit script doet de rest.
document.querySelectorAll("[data-lightbox]").forEach(function (cover) {
  var dlg = document.getElementById(cover.getAttribute("data-lightbox"));
  if (!dlg) return;
  var track = dlg.querySelector(".lb-track");
  var slides = dlg.querySelectorAll(".lb-slide");
  var dots = dlg.querySelectorAll(".lb-dots span");

  function index() {
    return Math.round(track.scrollLeft / track.clientWidth);
  }
  function sync() {
    var i = index();
    dots.forEach(function (d, n) { d.classList.toggle("on", n === i); });
  }
  function go(delta) {
    var i = Math.min(slides.length - 1, Math.max(0, index() + delta));
    track.scrollTo({ left: i * track.clientWidth, behavior: "smooth" });
  }
  function open() {
    dlg.showModal();
    track.scrollTo({ left: 0 });
    sync();
  }

  cover.addEventListener("click", open);
  cover.addEventListener("keydown", function (e) {
    if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(); }
  });
  dlg.querySelector(".lb-close").addEventListener("click", function () { dlg.close(); });
  dlg.querySelector(".lb-prev").addEventListener("click", function () { go(-1); });
  dlg.querySelector(".lb-next").addEventListener("click", function () { go(1); });
  track.addEventListener("scroll", function () { requestAnimationFrame(sync); });
  dlg.addEventListener("keydown", function (e) {
    if (e.key === "ArrowRight") go(1);
    if (e.key === "ArrowLeft") go(-1);
  });
});
