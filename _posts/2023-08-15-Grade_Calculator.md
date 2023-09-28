---
toc: false
comments: false
layout: post
title: Grade Calculator
description: An updated version of the original grade calculator.
type: tangibles
courses: { compsci: {week: 4} }
---

<!DOCTYPE html>
<html>
<head>
  <style>
    /* Modernistic Style */
    body {
      font-family: Arial, sans-serif;
      background-color: #f0f0f0;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    h3 {
      font-size: 1.5rem;
      color: #333;
      margin-bottom: 20px;
    }

    ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }

    li {
      background-color: #fff;
      border: 1px solid #ccc;
      padding: 10px;
      margin-bottom: 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 300px;
    }

    li span {
      font-weight: bold;
    }

    .input-container {
      display: flex;
      align-items: center;
    }

    input[type="number"] {
      padding: 5px;
      margin-right: 10px;
      text-align: right;
      width: 5em;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    .remove-button {
      background-color: #ff4d4d;
      color: white;
      border: none;
      padding: 5px 10px;
      cursor: pointer;
      border-radius: 5px;
    }

    .remove-button:hover {
      background-color: #e60000;
    }

    /* Define styles for green and red classes */
    .green {
      background-color: green;
      color: white;
    }

    .red {
      background-color: red;
      color: white;
    }

    table {
      border-collapse: collapse;
      width: 100%;
      margin-top: 20px;
    }

    th, td {
      border: 1px solid #ccc;
      padding: 8px;
      text-align: center;
    }

    /* Style the Grade section */
    .grade {
      background-color: #eee;
      font-weight: bold;
    }

  </style>
</head>
<body>
  <!-- Help Message -->
  <h3>Input scores, press tab to add each new number.</h3>
  <!-- Totals -->
  <ul>
    <li>
      <span>Total :</span> <span id="total">0.0</span>
      <span>Count :</span> <span id="count">0.0</span>
      <span>Average :</span> <span id="average">0.0</span>
    </li>
  </ul>
  <!-- Rows added using scores ID -->
  <div id="scores">
    <!-- JavaScript-generated inputs -->
  </div>

  <!-- Data Table -->
  <table>
    <thead>
      <tr>
        <th>Index</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody id="dataTable">
      <!-- Table rows will be added dynamically here -->
    </tbody>
  </table>

  <!-- Grade row -->
  <table>
    <tbody id="gradeRow">
      <!-- Grade row will be added dynamically here -->
    </tbody>
  </table>

  <script>
    // Executes on input event and calculates totals
    function calculator(event) {
      var key = event.key;
      // Check if the pressed key is the "Tab" key (key code 9) or "Enter" key (key code 13)
      if (key === "Tab" || key === "Enter") {
        event.preventDefault(); // Prevent default behavior (tabbing to the next element)

        var array = document.getElementsByName('score'); // setup array of scores
        var total = 0;  // running total
        var count = 0;  // count of input elements with valid values

        for (var i = 0; i < array.length; i++) {  // iterate through array
          var value = array[i].value;
          if (parseFloat(value)) {
            var parsedValue = parseFloat(value);
            total += parsedValue;  // add to running total
            count++;

            // Add or remove the "green" and "red" classes based on the value
            if (parsedValue > 60) {
              array[i].classList.remove("red");
              array[i].classList.add("green");
            } else {
              array[i].classList.remove("green");
              array[i].classList.add("red");
            }
          }
        }

        // Calculate the average
        var average = count > 0 ? total / count : 0;
        // Update the average in the table
        document.getElementById('average').textContent = average.toFixed(2);

        // Clear and update the data table
        clearDataTable();
        for (var i = 0; i < count; i++) {
          addToDataTable(i + 1, parseFloat(array[i].value).toFixed(2));
        }

        // Update the grade row
        clearGradeRow();
        addToGradeRow(average);

        // update totals
        document.getElementById('total').innerHTML = total.toFixed(2); // show two decimals
        document.getElementById('count').innerHTML = count;

        // adds a newInputLine, only if all array values satisfy parseFloat 
        if (count === document.getElementsByName('score').length) {
          newInputLine(count); // make a new input line
        }
      }
    }

    // Creates a new input box
    function newInputLine(index) {
      // Add a label for each score element
      var title = document.createElement('label');
      title.htmlFor = index;
      title.innerHTML = index + ". ";
      document.getElementById("scores").appendChild(title); // add to HTML

      // Setup score element and attributes
      var score = document.createElement("input"); // input element
      score.id =  index;  // id of input element
      score.onkeydown = calculator // Each key triggers event (using function as a value)
      score.type = "number"; // Use text type to allow typing multiple characters
      score.name = "score";  // name is used to group all "score" elements (array)
      score.style.textAlign = "right";
      score.style.width = "5em";
      document.getElementById("scores").appendChild(score);  // add to HTML

      // Create a "remove" button
      var removeButton = document.createElement("button");
      removeButton.className = "remove-button";
      removeButton.innerHTML = "X";
      removeButton.onclick = function() {
        // Remove the input and label
        title.remove();
        score.remove();
        removeButton.remove();
      };
      document.getElementById("scores").appendChild(removeButton);

      // Create and add a blank line after the input box
      var br = document.createElement("br");  // line break element
      document.getElementById("scores").appendChild(br); // add to HTML

      // Set focus on the new input line
      document.getElementById(index).focus();
    }

    // Add data to the table
    function addToDataTable(index, value) {
      var table = document.getElementById("dataTable");
      var row = table.insertRow(-1);
      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      cell1.innerHTML = index;
      cell2.innerHTML = value;
    }

    // Clear the data table
    function clearDataTable() {
      var table = document.getElementById("dataTable");
      table.innerHTML = '';
    }

    // Add the grade row to the table
    function addToGradeRow(average) {
      var gradeRow = document.getElementById("gradeRow");
      var row = gradeRow.insertRow(0);
      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      cell1.innerHTML = "Grade";
      cell2.innerHTML = average.toFixed(2);
    }

    // Clear the grade row
    function clearGradeRow() {
      var gradeRow = document.getElementById("gradeRow");
      gradeRow.innerHTML = '';
    }

    // Creates 1st input box on Window load
    newInputLine(0);

  </script>
</body>
</html>
