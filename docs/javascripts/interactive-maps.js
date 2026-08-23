document.addEventListener("click", (event) => {
  const link = event.target.closest(".interactive-map-link");
  if (link) window.location.assign(link.dataset.href);
});

document.addEventListener("keydown", (event) => {
  if (event.key !== "Enter" && event.key !== " ") return;
  const link = event.target.closest(".interactive-map-link");
  if (!link) return;
  event.preventDefault();
  window.location.assign(link.dataset.href);
});
