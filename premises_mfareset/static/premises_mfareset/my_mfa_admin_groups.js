document.addEventListener("DOMContentLoaded", function () {
        const form = document.getElementById("reset-mfa-form");
        const statusBox = document.getElementById("reset-status");

        if (!form || !statusBox) return;

        form.addEventListener("submit", async function (event) {
            event.preventDefault();

            statusBox.innerHTML = '<div class="alert alert-info">Resetting MFA...</div>';

            const formData = new FormData(form);

            try {
                const response = await fetch(form.action, {
                    method: "POST",
                    body: formData,
                    headers: {
                        "X-Requested-With": "XMLHttpRequest"
                    }
                });

                const data = await response.json();

                if (response.ok && data.success) {
                    statusBox.innerHTML = `<div class="alert alert-success">${data.message}</div>`;
                } else {
                    statusBox.innerHTML = `<div class="alert alert-danger">${data.message || "Reset failed."}</div>`;
                }
            } catch (error) {
                statusBox.innerHTML = `<div class="alert alert-danger">Unexpected error: ${error}</div>`;
            }
        });
    });