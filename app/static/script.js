function submitClient() {
    const name = document.getElementById("client-name").value;
    const email = document.getElementById("client-email").value;
    fetch("/api/clients/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name, email: email })
    }).then(res => res.json()).then(data => {
        document.getElementById("client-message").innerText = "Client added successfully!";
    }).catch(err => {
        console.error(err);
        document.getElementById("client-message").innerText = "Failed to add client.";
    });
}

function submitFreelancer() {
    const name = document.getElementById("freelancer-name").value;
    const email = document.getElementById("freelancer-email").value;
    fetch("/api/freelancers/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name, email: email })
    }).then(res => res.json()).then(data => {
        document.getElementById("freelancer-message").innerText = "Freelancer added successfully!";
    }).catch(err => {
        console.error(err);
        document.getElementById("freelancer-message").innerText = "Failed to add freelancer.";
    });
}

function downloadInvoice() {
    const clientName = document.getElementById("client-name").value;
    const clientEmail = document.getElementById("client-email").value;
    const freelancerName = document.getElementById("freelancer-name").value;
    const freelancerEmail = document.getElementById("freelancer-email").value;
    const projectDescription = document.getElementById("project-description").value;
    const hours = parseFloat(document.getElementById("hours").value);
    const rate = parseFloat(document.getElementById("rate").value);

    fetch("/api/invoices/download", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            client_name: clientName,
            client_email: clientEmail,
            freelancer_name: freelancerName,
            freelancer_email: freelancerEmail,
            project_description: projectDescription,
            hours: hours,
            rate: rate
        })
    })
    .then(res => {
        if (!res.ok) throw new Error("Failed to download");
        return res.blob();
    })
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "invoice.pdf";
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url);
    })
    .catch(err => {
        console.error(err);
        alert("Failed to download invoice.");
    });
}
