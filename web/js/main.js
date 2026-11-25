// Panel visibility toggles, persisted in localStorage.
const KEY = "owasp-panels";
const saved = JSON.parse(localStorage.getItem(KEY) || "{}");
const toggles = document.querySelectorAll(".panel-toggle");

function apply(toggle) {
    const panel = document.getElementById(toggle.dataset.target);
    panel.classList.toggle("d-none", !toggle.checked);
    saved[toggle.dataset.target] = toggle.checked;
    localStorage.setItem(KEY, JSON.stringify(saved));
}

toggles.forEach(toggle => {
    if (saved[toggle.dataset.target] === false) toggle.checked = false;
    apply(toggle);
    toggle.addEventListener("change", () => apply(toggle));
});

const showAll = document.getElementById("show-all");
if (showAll) {
    showAll.addEventListener("click", () => {
        toggles.forEach(toggle => { toggle.checked = true; apply(toggle); });
    });
}
