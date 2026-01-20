function validateForm() {
    let resume = document.getElementById("resume").value.trim();
    let jobDesc = document.getElementById("job_desc").value.trim();

    if (resume === "" || jobDesc === "") {
        alert("Please fill both Resume and Job Description!");
        return false;
    }

    return true;
}
