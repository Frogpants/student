---
toc: false
comments: false
layout: post
title: Main Calculator
description: A visual calculator which has more uses than the grade calculator.
type: tangibles
courses: { compsci: {week: 4} }
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visual Calculator</title>
    <style>
        /* Define a color palette */
        :root {
            --primary-color: #3498db; /* Blue color for the calculator background */
            --secondary-color: #e74c3c; /* Red color for the "C" button */
            --button-bg: #ecf0f1;
            --button-hover-bg: #bdc3c7;
        }

        /* Add some basic styling */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: linear-gradient(45deg, rgba(52, 152, 219, 0.5), rgba(231, 76, 60, 0.5), rgba(241, 196, 15, 0.5), rgba(46, 204, 113, 0.5));
            background-size: cover;
        }

        .calculator {
            background-color: var(--primary-color); /* Blue background color for the calculator */
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
            width: 90%;
            max-width: 500px; /* Increased maximum width */
        }

        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 2px solid black;
            border-radius: 5px;
            font-size: 24px; /* Increased font size */
        }

        .button-container {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            grid-gap: 5px;
        }

        button {
            width: 70px; /* Increased button width */
            height: 70px; /* Increased button height */
            font-size: 24px; /* Increased font size */
            border: 2px solid black;
            border-radius: 10px;
            background-color: var(--button-bg);
            cursor: pointer;
            transition: transform 0.2s;
        }

        /* Styling for the "C" button */
        button:nth-child(13) {
            background-color: var(--secondary-color); /* Orange background color for the "C" button */
        }

        button:hover {
            background-color: var(--button-hover-bg);
            transform: scale(calc((140px - 70px) / 8)); /* Gradual size change on hover */
        }
    </style>
</head>
<body>
    <div class="calculator">
        <input type="text" id="result" readonly onkeydown="handleKeyPress(event)">
        <div class="button-container">
            <!-- Numbers and Operators -->
            <button onclick="appendToResult('7')">7</button>
            <button onclick="appendToResult('8')">8</button>
            <button onclick="appendToResult('9')">9</button>
            <button onclick="appendToResult('+')">+</button>
            <button onclick="appendToResult('4')">4</button>
            <button onclick="appendToResult('5')">5</button>
            <button onclick="appendToResult('6')">6</button>
            <button onclick="appendToResult('-')">-</button>
            <button onclick="appendToResult('1')">1</button>
            <button onclick="appendToResult('2')">2</button>
            <button onclick="appendToResult('3')">3</button>
            <button onclick="appendToResult('*')">*</button>
            <button onclick="clearResult()">C</button> <!-- Color changed to orange -->
            <button onclick="appendToResult('0')">0</button>
            <button onclick="calculateResult()">=</button>
            <button onclick="appendToResult('/')">/</button>
            <!-- New Buttons: Square Root, Exponent, and Pi -->
            <button onclick="appendToResult('Math.sqrt(')">√</button> <!-- Square Root -->
            <button onclick="appendToResult('**')">^</button> <!-- Exponent -->
            <button onclick="appendToResult('Math.PI')">π</button> <!-- Pi -->
        </div>
    </div>

    <script>
        // Calculator functions

        function handleKeyPress(event) {
            const key = event.key;
            if (key.match(/[0-9+\-*/()]|Enter/) || key === 'Escape') {
                document.getElementById('result').value += key;
            }
        }

        function appendToResult(value) {
            document.getElementById('result').value += value;
        }

        function clearResult() {
            document.getElementById('result').value = '';
        }

        function calculateResult() {
            const resultElement = document.getElementById('result');
            try {
                // Use the "eval" function to evaluate mathematical expressions
                resultElement.value = eval(resultElement.value);
            } catch (error) {
                resultElement.value = 'Error';
            }
        }
    </script>
</body>
</html>
