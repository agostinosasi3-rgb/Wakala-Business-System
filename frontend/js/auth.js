document.getElementById("loginForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);

    try {
        const response = await fetch(`${CONFIG.API_BASE_URL}/auth/login`, {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: formData
        });

        const data = await response.json();
        if (response.ok) {
            localStorage.setItem("token", data.access_token);
            window.location.href = "dashboard.html";
        } else {
            alert(data.detail || "Imeshindikana kuingia, angalia taarifa zakos.");
        }
    } catch (err) {
        alert("Server haijafunguka au kuna shida ya mtandao.");
    }
});