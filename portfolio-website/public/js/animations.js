document.addEventListener("DOMContentLoaded", function() {
    gsap.from("#welcome-text", { duration: 1, y: -50, opacity: 0, ease: "bounce" });
  
    gsap.to(".circle", {
      duration: 2,
      x: 150,
      ease: "power1.inOut",
      repeat: -1,
      yoyo: true,
      stagger: 0.2
    });
  
    gsap.to("#welcome-text", {
      duration: 2,
      text: "Welcome to My Modern Portfolio!",
      delay: 1,
      ease: "power1.inOut"
    });
  
    const popup = document.getElementById("popup");
    popup.addEventListener("click", function() {
      window.location.href = "/contact";
    });
  });
  