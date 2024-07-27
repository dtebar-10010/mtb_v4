document.addEventListener("DOMContentLoaded", function () {
  // Initialize the stacked cards
  var stackedCardSlide = new stackedCards({
    selector: ".stacked-cards-slide",
    layout: "slide",
    transformOrigin: "center",
    onClick: function (el) {
      document.querySelectorAll(".stacked-cards video").forEach((video) => {
        if (video.parentElement === el) {
          video.controls = true;
          video.parentElement.classList.add("active");
        } else {
          video.controls = false;
          video.pause();
          video.parentElement.classList.remove("active");
        }
      });
    },
  });
  stackedCardSlide.init();

  // Other elements (accordions, phase selection)
  const accordionHeaders = document.querySelectorAll(".accordion.hide-initially");
  const phaseSelectionContainer = document.querySelector("#phase-selection-container");

  accordionHeaders.forEach(function (header) {
    header.classList.add("show-initially");
  });

  if (phaseSelectionContainer) {
    phaseSelectionContainer.classList.remove("hide-initially");
    phaseSelectionContainer.style.width = "100%";
    phaseSelectionContainer.style.margin = "0 auto";
    phaseSelectionContainer.style.display = "flex";
  }

  // Video Controls Logic
  const videos = document.querySelectorAll(".video-slide");
  videos.forEach(function (video) {
    video.addEventListener("mouseover", function () {
      if (video.closest("li").classList.contains("active")) {
        video.setAttribute("controls", "controls");
      }
    });
    video.addEventListener("mouseout", function () {
      if (!video.paused) {
        video.setAttribute("controls", "controls");
      } else {
        video.removeAttribute("controls");
      }
    });
    video.addEventListener("play", function () {
      document.querySelectorAll(".video-slide").forEach((v) => {
        if (v !== video) {
          v.pause();
          v.removeAttribute("controls");
          v.closest("li").classList.remove("active");
        }
      });
      video.setAttribute("controls", "controls");
      video.closest("li").classList.add("active");
    });
    video.addEventListener("pause", function () {
      video.removeAttribute("controls");
    });
  });

  // Update current year
  const currentYearElement = document.getElementById("currentYear");
  if (currentYearElement) {
    currentYearElement.textContent = String(new Date().getFullYear());
  }

  // Text Container Scrolling and Border Color Fix
  const textContainer = document.querySelector(".text-container");
  const maxAllowedHeight = 111;
  const phaseButtons = document.querySelectorAll(".btn-group .btn");
  let currentPhaseColor;

  // Function to adjust text container and border color
  function adjustTextContainer() {
    textContainer.style.maxHeight = "none"; // Reset max-height
    textContainer.style.overflowY = "hidden"; // Reset overflow

    if (textContainer.scrollHeight > maxAllowedHeight) {
      textContainer.style.maxHeight = maxAllowedHeight + "px";
      textContainer.style.overflowY = "auto";
    }

    if (currentPhaseColor) {
      textContainer.style.borderColor = currentPhaseColor;
    }
  }

  // Get initial active button color
  currentPhaseColor = window
    .getComputedStyle(document.querySelector(".btn.active"))
    .backgroundColor;

  // Wait for the DOM to be fully parsed before adjusting and revealing the text container
  setTimeout(() => {
    adjustTextContainer();
    textContainer.style.display = "block"; // Reveal the text container after styles are applied
  }, 0);

  // Add event listeners to phase buttons
  phaseButtons.forEach((button) => {
    button.addEventListener("click", () => {
      phaseButtons.forEach((btn) => btn.classList.remove("active"));
      button.classList.add("active");

      // Update the current phase color
      currentPhaseColor = window.getComputedStyle(button).backgroundColor;

      // Reset display before adjusting and revealing again
      textContainer.style.display = "none";

      // Wait for all content to load (including images)
      Promise.all(
        Array.from(textContainer.querySelectorAll("img"))
          .filter((img) => !img.complete)
          .map((img) => new Promise((resolve) => (img.onload = img.onerror = resolve)))
      ).then(() => {
        adjustTextContainer();
        textContainer.style.display = "block";
      });
    });
  });

  // Handle window resize
  window.addEventListener("resize", adjustTextContainer);
});
