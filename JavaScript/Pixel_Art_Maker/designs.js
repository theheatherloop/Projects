var canvas = document.getElementById('pixelCanvas');//variable created for table 

var button = document.getElementById('sButton');//variable created for submit button

button.addEventListener('click', function(event){//listens for the submit button to be clicked 
  event.preventDefault();//prevents the form from being submitted 
  makeGrid();//runs makeGrid function
});

canvas.addEventListener('click',function(event){//listens for a cell to be clicked
  if (event.target.nodeName.toUpperCase() === ('TD'))//verifies the clicked node is a TD element
  var cell = event.target.closest('td');//variable created for verified node
  var color = document.getElementById('colorPicker').value;//variable created for selected color
  cell.style.backgroundColor = color;//applies selected color to node
})

function makeGrid() {
  var width = document.getElementById('inputWidth').value;//variable created for weight  input
  var height = document.getElementById('inputHeight').value;//variable created for height input
  canvas.innerHTML = '';
  
  for (let i = 0; i < height; i++) {//loops through height input creating rows
    let tr = document.createElement('tr');//variable created for rows
      
    for (let j = 0; j < width; j++) {//for each row, loop through width input to create cell
      let td = document.createElement('td');//variable created for cells
      tr.appendChild(td);//add cell to table
      td.id = j;//give cell an ID
    }

    canvas.appendChild(tr);//adds cells to table
  }
} 


