document.getElementById("startSessionForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const openingCash = parseFloat(document.getElementById("openingCash").value);

    const payload = {
        opening_cash: openingCash,
        provider_floats: [] // Inaweza kujazwa dynamically
    };

    const res = await ApiService.request("/sessions/start", "POST", payload);
    if (res && res.id) {
        alert("Siku imefunguliwa kikamilifu!");
        window.location.href = "transactions.html";
    } else {
        alert(res.detail || "Kuna kosa limetokea.");
    }
});