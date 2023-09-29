---
toc: false
comments: true
layout: post
title: Web Programming Basics
description: The basics of web programing (Mind Blown)
type: hacks
courses: { compsci: {week: 5} }
---

# A guide to basic concepts in Web Notebook
- Making a menu
- Use menu to Guide topics
- Make your own custom page and menu
- Making a page dynamic through JavaScript
- Review usage of Styles in GitHub Pages

# How to import this setup into your student repository
- NOTE: To copy files between repostories, open two vscode windows and you can drag and drop
- Copy the file _includes/nav_basics.html into the _includes folder of your student repository
- This creates the navigation between the different pages in the Web Dev Basics
- Copy the following files from _notebooks into your _notebooks folder
  - 2023-03-28-basics-home.ipynb, 2023-03-28-basics-html.ipynb,2023-03-29-basics-of-js.ipynb, 2023-08-30-basics-of-js-data-types.ipynb, 2023-08-30-basics-js-with-html.ipynb, 2023-09-20-1_4-js-errors.ipynb
- In the basics homepage (2023-03-28-basics-home.ipynb), you need to make an edit
- In the top cell, modify the courses to say { compsci: { week: 5 } } (this will move this into your schedule page)

# Seeing javascript console output in visual studio
- When printing outputs from javascript to the console you will need to open the developer console
- Go to Help->Toggle Developer Tools and click console on the top bar of the developer window

<!DOCTYPE html>
<html lang="en">
%%html
<!DOCTYPE html>
<html>

<head>
    <style>
        .div1 {
            border: none;
            background-color: white;
            text-align: left;
            color: black;
            padding-top: 5px;
            padding-bottom: 10px;
            padding-left: 15px;
            padding-right: 15px;
            margin-bottom: 10px;
        }

        .div2 {
            border: 5px outset blue;
            background-color: white;
            text-align: left;
            color: black;
            padding-top: 15px;
            padding-bottom: 5px;
            padding-left: 15px;
            padding-right: 15px;
        }
    </style>
    
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Code Editor</title>
    <style>
        #editor {
            width: 100%;
            height: 400px;
        }
    </style>
</head>
<body>
    <h1>JavaScript Code Editor</h1>
    <textarea id="editor">console.log("Hello, World!");</textarea>
    <button onclick="runCode()">Run</button>
    <h2>Output:</h2>
    <div id="output">
    
        <p id="toggleParagraph">Click this button to toggle visibility</p>
        <button onclick="toggleVisibility()">This is a button</button>

        <a target="_blank" href="https://frogpants.github.io/student/">Link to Spencer's page</a><br>
        <a target="_blank" href="https://seannakagawa.github.io/student/">Link to Sean's page</a><br>
        <a target="_blank" href="https://github.com/Trystan-Schmits/Student1">Link to Trystan's page</a><br>
        <a target="_blank" href="https://zafeera123.github.io/ZafeerA123/">Link to Zafeer's page</a><br>
        <a target="_blank" href="INPUT GAME LINK">Link to our game</a>
        <p>The name of our game is...</p>
    
    </div>

    <script>
        function runCode() {
            const code = document.getElementById("editor").value;
            const outputDiv = document.getElementById("output");

            try {
                // Execute the JavaScript code
                const result = eval(code);
                outputDiv.innerHTML = "<pre>" + result + "</pre>";
            } catch (error) {
                outputDiv.innerHTML = "<pre style='color: red;'>" + error + "</pre>";
            }
        }

        function toggleVisibility() {
            // Get the paragraph element
            var paragraph = document.getElementById('toggleParagraph');

            // Toggle visibility
            paragraph.style.display = (paragraph.style.display === 'none') ? 'block' : 'none';
        }

    </script>
</body>
</html>