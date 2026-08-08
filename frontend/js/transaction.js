document.addEventListener("DOMContentLoaded", async () => {
    const providers = await ApiService.request("/providers/");
    const select = document.getElementById("providerSelect");
    if (providers && select) {
        providers.forEach(p => {
            select.innerHTML += `<option value="${p.id}">${p.name}</option>`;
        });
    }
});

document.getElementById("txForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const payload = {
        provider_id: parseInt(document.getElementById("providerSelect").value),
        transaction_type: document.getElementById("txType").value,
        amount: parseFloat(document.getElementById("txAmount").value),
        reference_number: document.getElementById("refNum").value
    };

    const res = await ApiService.request("/transactions/", "POST", payload);
    if (res && res.id) {
        alert(`Muamala umeingizwa! Kamisheni iliyokadiriwa: TZS ${res.estimated_commission}`);
        document.getElementById("txForm").reset();
    } else {
        alert(res.detail || "Imeshindikana kurekodi muamala.");
    }
});