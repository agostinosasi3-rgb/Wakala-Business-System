class ApiService {
    static getToken() {
        return localStorage.getItem("token");
    }

    static async request(endpoint, method = "GET", body = null) {
        const headers = {
            "Content-Type": "application/json",
        };
        const token = this.getToken();
        if (token) {
            headers["Authorization"] = `Bearer ${token}`;
        }

        const options = { method, headers };
        if (body) {
            options.body = JSON.stringify(body);
        }

        const response = await fetch(`${CONFIG.API_BASE_URL}${endpoint}`, options);
        if (response.status === 401) {
            localStorage.removeItem("token");
            window.location.href = "login.html";
            return;
        }
        return response.json();
    }
}