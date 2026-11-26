const cells = document.querySelectorAll('.grid-item'); // r:nodelist & finds all classes named grid-item

const rows = {
    0: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    1: [9, 10, 11, 12, 13, 14, 15, 16, 17],
    2: [18, 19, 20, 21, 22, 23, 24, 25, 26],
    3: [27, 28, 29, 30, 31, 32, 33, 34, 35],
    4: [36, 37, 38, 39, 40, 41, 42, 43, 44],
    5: [45, 46, 47, 48, 49, 50, 51, 52, 53],
    6: [54, 55, 56, 57, 58, 59, 60, 61, 62],
    7: [63, 64, 65, 66, 67, 68, 69, 70, 71],
    8: [72, 73, 74, 75, 76, 77, 78, 79, 80]
};

const columns = {
    0: [0, 9, 18, 27, 36, 45, 54, 63, 72],
    1: [1, 10, 19, 28, 37, 46, 55, 64, 73],
    2: [2, 11, 20, 29, 38, 47, 56, 65, 74],
    3: [3, 12, 21, 30, 39, 48, 57, 66, 75],
    4: [4, 13, 22, 31, 40, 49, 58, 67, 76],
    5: [5, 14, 23, 32, 41, 50, 59, 68, 77],
    6: [6, 15, 24, 33, 42, 51, 60, 69, 78],
    7: [7, 16, 25, 34, 43, 52, 61, 70, 79],
    8: [8, 17, 26, 35, 44, 53, 62, 71, 80]
};


function HighlightClick(event){
    console.log(event.target);

    // will reset all back to original colour - check performance
    cells.forEach(cell => {
        cell.style.backgroundColor = '';
    });


    const index = Array.from(cells).indexOf(event.target); // converts nodelist cells to array, and gets index

    const row = Math.floor(index / 9);
    const col = index % 9;

    const rowCells = rows[row]; // array of the cells indices that should be highlighted
    const colCells = columns[col];

    rowCells.forEach(i => {
        cells[i].style.backgroundColor = "lightgrey";
    });

    colCells.forEach(i => {
        cells[i].style.backgroundColor = "lightgrey";
    });

    event.target.style.backgroundColor = "orange"
}



cells.forEach(cell => {
    cell.addEventListener('click', HighlightClick);
});


