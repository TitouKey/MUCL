(function () {
  var forms = document.querySelectorAll("[data-newsletter]");

  function msgEl(form) {
    var section = form.closest(".newsletter");
    return section && section.querySelector(".newsletter-msg");
  }

  forms.forEach(function (form) {
    var input = form.querySelector('input[name="email"]');
    var btn = form.querySelector('button[type="submit"]');
    var msg = msgEl(form);
    var label = btn ? btn.textContent.trim() : "";

    form.addEventListener("submit", function (e) {
      e.preventDefault();

      if (msg) {
        msg.hidden = true;
        msg.classList.remove("is-error", "is-ok");
      }
      if (btn) {
        btn.disabled = true;
      }

      fetch(form.action, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8" },
        body: new URLSearchParams(new FormData(form)).toString()
      })
        .then(function (r) {
          return r.json().then(function (j) {
            return { ok: r.ok, body: j };
          });
        })
        .then(function (res) {
          if (res.ok && res.body.ok) {
            form.reset();
            if (msg) {
              msg.textContent = res.body.message;
              msg.classList.add("is-ok");
              msg.hidden = false;
            }
          } else if (msg) {
            msg.textContent = (res.body && res.body.message) || label;
            msg.classList.add("is-error");
            msg.hidden = false;
          }
        })
        .catch(function () {
          if (msg) {
            msg.textContent = label;
            msg.classList.add("is-error");
            msg.hidden = false;
          }
        })
        .then(function () {
          if (btn) {
            btn.disabled = false;
          }
        });
    });
  });
})();
