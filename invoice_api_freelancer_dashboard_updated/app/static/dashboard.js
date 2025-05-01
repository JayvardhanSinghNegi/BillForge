
function showToast(message, success=true) {
    const toast = document.createElement('div');
    toast.className = 'toast' + (success ? '' : ' error');
    toast.innerText = message;
    document.body.appendChild(toast);
    setTimeout(() => toast.classList.add('show'), 10);
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => document.body.removeChild(toast), 500);
    }, 3000);
}

async function postData(url = '', data = {}) {
    const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    if (!response.ok) throw new Error('Failed to submit');
    return response.json();
}

document.getElementById('client-form').onsubmit = async (e) => {
    e.preventDefault();
    const form = e.target;
    if (!form.name.value || !form.email.value || !form.company.value) return showToast("Fill all client fields", false);
    try {
        const data = { name: form.name.value, email: form.email.value, company: form.company.value };
        const res = await postData('/clients', data);
        document.getElementById('client-list').innerHTML += `<li>${res.name} (${res.company})</li>`;
        form.reset();
        showToast("Client added!");
    } catch {
        showToast("Failed to add client", false);
    }
};

document.getElementById('project-form').onsubmit = async (e) => {
    e.preventDefault();
    const form = e.target;
    if (!form.title.value || !form.rate.value || !form.client_id.value) return showToast("Fill all project fields", false);
    try {
        const data = { title: form.title.value, hourly_rate: parseFloat(form.rate.value), client_id: parseInt(form.client_id.value) };
        const res = await postData('/projects', data);
        document.getElementById('project-list').innerHTML += `<li>${res.title} (Rate: $${res.hourly_rate})</li>`;
        form.reset();
        showToast("Project added!");
    } catch {
        showToast("Failed to add project", false);
    }
};

document.getElementById('timelog-form').onsubmit = async (e) => {
    e.preventDefault();
    const form = e.target;
    if (!form.project_id.value || !form.hours.value) return showToast("Fill all time log fields", false);
    try {
        const data = { project_id: parseInt(form.project_id.value), hours: parseFloat(form.hours.value) };
        const res = await postData('/timelogs', data);
        document.getElementById('timelog-list').innerHTML += `<li>Project ${res.project_id}: ${res.hours} hours</li>`;
        form.reset();
        showToast("Time logged!");
    } catch {
        showToast("Failed to log time", false);
    }
};


function downloadInvoice() {
    const projectId = document.getElementById("invoice-project-id").value;
    if (!projectId) return showToast("Please enter a project ID", false);
    const url = `/invoices/${projectId}`;
    window.open(url, "_blank");
}
