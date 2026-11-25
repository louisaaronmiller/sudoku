const cells = document.querySelectorAll('.grid-item'); // r:nodelist & finds all classes named grid-item

function HighlightClick(event){
    console.log(event.target);

    event.target.style.backgroundColor = "Black"
}

cells.forEach(cell => {
    cell.addEventListener('click', HighlightClick);
});


