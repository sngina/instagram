document.querySelectorAll("img").forEach((item) => {
    item.addEventListener("click", (event) => {
      const image = event.target.getAttribute("data-src");
      event.target.setAttribute("src", image);
    });
  });