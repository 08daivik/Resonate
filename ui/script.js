const BASE_URL = "http://127.0.0.1:8000";

const dropArea = document.getElementById("dropArea");
const fileNameText = document.getElementById("fileName");
let selectedFile = null;

/* -------- UPLOAD -------- */
dropArea.onclick = () => document.createElement("input").click();

dropArea.addEventListener("click", () => {
    const fileInput = document.createElement("input");
    fileInput.type = "file";
    fileInput.onchange = () => {
        selectedFile = fileInput.files[0];
        fileNameText.innerText = selectedFile.name;
    };
    fileInput.click();
});

// async function uploadFile() {
//     if (!selectedFile) {
//         alert("Please select a file first!");
//         return;
//     }

//     alert("Hey 1")
//     const formData = new FormData();
//     formData.append("file", selectedFile);
//     const res = await fetch(`${BASE_URL}/upload`, {
//         method: "POST",
//         body: formData
//     });
    
//     const data = await res.json();
    
//     document.getElementById("uploadStatus").innerHTML = `
//     <p><b>Status:</b> Processed ✔</p>
//     <p><b>Length:</b> ${data.text_length}</p>
//     <p><b>Chunks:</b> ${data.chunks}</p>
//     `;
//     alert("Hey 3")
// }

async function uploadAlert(){
    await new Promise(r=>{
        setTimeout(()=>{
            alert("File Uploaded Successfully")
            r()
        }, 5000)
    })
}

document.getElementById('upload-btn').addEventListener('click', async(e)=>{
    e.preventDefault()
    if (!selectedFile) {
        alert("Please select a file first!");
        return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);
    fetch(`${BASE_URL}/upload`, {
        method: "POST",
        body: formData
    }).then((res)=>{
        alert("File uploaded successfully")
        return res.json()
    }).then((data)=>{
        document.getElementById("uploadStatus").innerHTML = `
    <p><b>Status:</b> Processed ✔</p>
    <p><b>Length:</b> ${data.text_length}</p>
    <p><b>Chunks:</b> ${data.chunks}</p>
    `
    })
    return false
})

/* -------- SUMMARY -------- */
async function getSummary() {
    const loader = document.getElementById("summaryLoader");
    loader.classList.remove("hidden");

    const res = await fetch(`${BASE_URL}/summary`);
    const data = await res.json();

    loader.classList.add("hidden");

    document.getElementById("summaryBox").innerText = data.summary;
}

/* -------- ASK QUESTION -------- */
async function askQuestion() {
    const q = document.getElementById("question").value;
    if (!q.trim()) return;

    const chatBox = document.getElementById("chatBox");
    chatBox.innerHTML += `<div class="user-msg">${q}</div>`;

    const res = await fetch(`${BASE_URL}/ask?query=${encodeURIComponent(q)}`);
    const data = await res.json();

    chatBox.innerHTML += `<div class="ai-msg">${data.answer}</div>`;
    chatBox.scrollTo({ top: chatBox.scrollHeight, behavior: "smooth" });
}
