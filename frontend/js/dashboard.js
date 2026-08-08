document.addEventListener("DOMContentLoaded", async () => {
    document.getElementById("logoutBtn")?.addEventListener("click", () => {
        localStorage.removeItem("token");
        window.location.href = "login.html";
    });
});