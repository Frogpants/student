---
toc: false
comments: false
layout: post
title: JS Motion
description: YAHOOO!
type: tangibles
courses: { compsci: {week: 5} }
---

<!DOCTYPE html>
<html>
<head>
    <title>Object Mover</title>
    <style>
        canvas {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <canvas id="canvas" width="400" height="400"></canvas>
    <script>
        const canvas = document.getElementById("canvas");
        const ctx = canvas.getContext("2d");

        // Object properties
        let object = {
            x: 50,
            y: 50,
            width: 30,
            height: 30,
            color: "blue",
            targetX: 200,
            targetY: 200,
            isMoving: false,
            animationProgress: 0,
        };

        // Customize your animation function
        function customAnimation(progress) {
            return Math.sin(progress * Math.PI);
        }

        // Update function
        function update() {
            if (object.isMoving) {
                object.animationProgress += 0.02;
                if (object.animationProgress >= 1) {
                    object.animationProgress = 1;
                    object.isMoving = false;
                }

                const animationValue = customAnimation(object.animationProgress);

                // Interpolate object position based on animation value
                object.x = object.x + (object.targetX - object.x) * animationValue;
                object.y = object.y + (object.targetY - object.y) * animationValue;
            }
        }

        // Draw function
        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Draw the object
            ctx.fillStyle = object.color;
            ctx.fillRect(object.x, object.y, object.width, object.height);

            requestAnimationFrame(draw);
        }

        // Start animation when a button is clicked
        document.addEventListener("click", () => {
            if (!object.isMoving) {
                object.targetX = Math.random() * (canvas.width - object.width);
                object.targetY = Math.random() * (canvas.height - object.height);
                object.isMoving = true;
                object.animationProgress = 0;
            }
        });

        // Game loop
        function gameLoop() {
            update();
            draw();
            requestAnimationFrame(gameLoop);
        }

        gameLoop();
    </script>
</body>
</html>
