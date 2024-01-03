
const canvas = document.getElementById('drawCanvas');
const context = canvas.getContext('2d');




canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);

let isDrawing = false;

function initializeCanvas() {
    context.fillStyle = 'black';
    context.fillRect(0, 0, canvas.width, canvas.height);
}

initializeCanvas();


function startDrawing(e) {
    isDrawing = true;
    draw(e);
}

// function draw(e) {
//     if (!isDrawing) return;

//     context.lineWidth = 10;
//     context.lineCap = 'round';
//     context.strokeStyle = 'white';

//     context.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
//     context.stroke();
//     context.beginPath();
//     context.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
// }
function draw(e) {
    if (!isDrawing) return;

    const rect = canvas.getBoundingClientRect();
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;

    context.lineWidth = 10;
    context.lineCap = 'round';
    context.strokeStyle = 'white';

    context.lineTo(mouseX, mouseY);
    context.stroke();
    context.beginPath();
    context.moveTo(mouseX, mouseY);
}

function stopDrawing() {
    isDrawing = false;
    context.beginPath();
}

function clearCanvas() {
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle='black';
    context.fillRect(0,0,canvas.width,canvas.height);
}
function save(){
    console.log("Save function called");
    
    var canvas = document.getElementById('drawCanvas');
    document.getElementById("hiddenData").value = canvas.toDataURL('image/png');
    document.forms["canvas-form"].submit();
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle='black';
    context.fillRect(0,0,canvas.width,canvas.height);
}


