const flowerDivs = document.querySelectorAll(".flower");

function toggleColour(e) {
  if (
    e.currentTarget.style.backgroundColor === e.currentTarget.style.borderColor
  ) {
    e.currentTarget.style.backgroundColor = "#333";
  } else {
    e.currentTarget.style.backgroundColor = e.currentTarget.style.borderColor;
  }
}

flowerDivs.forEach((singleFlowerDiv) => {
  singleFlowerDiv.addEventListener("click", toggleColour);
});
