document.addEventListener("DOMContentLoaded", async () => {
    const report = await ApiService.request("/reports/weekly");
    const container = document.getElementById("reportContent");
    if (report && container) {
        container.innerHTML = `
            <div class="dashboard-grid">
                <div class="stat-card"><h4>Cash In Volume</h4><p>TZS ${report.total_cash_in_volume}</p></div>
                <div class="stat-card"><h4>Cash Out Volume</h4><p>TZS ${report.total_cash_out_volume}</p></div>
                <div class="stat-card"><h4>Jumla ya Kamisheni</h4><p>TZS ${report.total_commission_earned}</p></div>
                <div class="stat-card"><h4>Faida Halisi (Net Profit)</h4><p style="color:green;">TZS ${report.net_profit_loss}</p></div>
            </div>
        `;
    }
});