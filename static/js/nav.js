(function () {
  var nav = document.querySelector(".site-nav");
  if (!nav) return;

  var drop = document.createElement("span");
  drop.className = "nav-drop";
  nav.appendChild(drop);

  var links = Array.prototype.slice.call(nav.querySelectorAll("a"));

  function getActive() {
    for (var i = 0; i < links.length; i++) {
      if (links[i].getAttribute("aria-current") === "page") return links[i];
    }
    return null;
  }

  var current = getActive();
  var REST_DURATION = "0.6s";

  function position(el) {
    if (!el) {
      drop.style.opacity = "0";
      return;
    }
    var pad = parseFloat(getComputedStyle(nav).paddingLeft) || 7;
    drop.style.left = pad + "px";
    drop.style.top = pad + "px";
    drop.style.bottom = pad + "px";
    drop.style.width = el.offsetWidth + "px";
    drop.style.transform = "translateX(" + (el.offsetLeft - pad) + "px)";
    drop.style.opacity = "1";
  }

  position(current);

  links.forEach(function (link) {
    link.addEventListener("mouseenter", function () {
      drop.style.transitionDuration = REST_DURATION;
      position(link);
    });

    link.addEventListener("click", function (ev) {
      if (ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey || ev.button !== 0) return;
      if (!/^https?:$/.test(link.protocol)) return;
      var sameOrigin = link.hostname === window.location.hostname;
      if (!sameOrigin) return;

      ev.preventDefault();
      drop.style.transitionDuration = "0.32s";
      position(link);
      setTimeout(function () {
        window.location.href = link.href;
      }, 300);
    });
  });

  nav.addEventListener("mouseleave", function () {
    drop.style.transitionDuration = REST_DURATION;
    position(current);
  });

  window.addEventListener("resize", function () {
    position(current);
  });
  window.addEventListener("load", function () {
    position(current);
  });
})();
