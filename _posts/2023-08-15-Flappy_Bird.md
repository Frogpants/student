---
toc: false
comments: false
layout: post
title: Flappy Bird
description: The most common game to ever be made by programmers!
type: tangibles
courses: { compsci: {week: 0} }
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flappy Bird</title>
    <style>
        canvas {
            border: 2px solid black;
            display: block;
            margin: 0 auto;
        }
        .start-screen, .end-screen {
            display: none;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 255, 0.5);
            text-align: center;
            font-size: 24px;
            color: white;
            padding-top: 100px;
        }
        .end-screen {
            background-color: rgba(0, 0, 0, 0.5);
        }
    </style>
</head>
<body>
    <canvas id="flappyBird" width="700" height="400"></canvas>
    <div class="start-screen" id="startScreen">
        <p>Press Spacebar to Start</p>
    </div>
    <div class="end-screen" id="endScreen">
        <p>Game Over</p>
        <p id="scoreText"></p>
        <button onclick="restartGame()">Restart</button>
    </div>

    <script>
        const canvas = document.getElementById("flappyBird");
        const ctx = canvas.getContext("2d");

        const bird = {
            x: 50,
            y: canvas.height / 2 - 10,
            radius: 10,
            velocity: 0,
            gravity: 0.1,
            jumpStrength: -3,
        };

        const pipes = [];
        const pipeWidth = 40;
        const pipeGap = 100;
        const pipeSpeed = 2;
        const pipeSpawnInterval = 120;

        let score = 0;
        let gameInterval;
        let gameStarted = false;

        const startScreen = document.getElementById("startScreen");
        const endScreen = document.getElementById("endScreen");
        const scoreText = document.getElementById("scoreText");

        function drawBird() {
            ctx.beginPath();
            ctx.arc(bird.x, bird.y, bird.radius, 0, Math.PI * 2);
            ctx.fillStyle = "blue";
            ctx.fill();
            ctx.closePath();
        }

        function drawPipe(x, height) {
            ctx.fillStyle = "green";
            ctx.fillRect(x, 0, pipeWidth, height);
            ctx.fillRect(x, height + pipeGap, pipeWidth, canvas.height - height - pipeGap);
        }

        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            if (gameStarted) {
                bird.velocity += bird.gravity;
                bird.y += bird.velocity;

                if (bird.y + bird.radius > canvas.height || bird.y - bird.radius < 0) {
                    gameOver();
                }

                if (pipes.length === 0 || pipes[pipes.length - 1].x <= canvas.width - pipeSpawnInterval) {
                    const pipeHeight = Math.floor(Math.random() * (canvas.height - pipeGap));
                    pipes.push({ x: canvas.width, height: pipeHeight });
                }

                for (let i = 0; i < pipes.length; i++) {
                    const pipe = pipes[i];
                    pipe.x -= pipeSpeed;
                    drawPipe(pipe.x, pipe.height);

                    if (
                        bird.x + bird.radius > pipe.x &&
                        bird.x - bird.radius < pipe.x + pipeWidth &&
                        (bird.y - bird.radius < pipe.height || bird.y + bird.radius > pipe.height + pipeGap)
                    ) {
                        gameOver();
                    }

                    if (pipe.x + pipeWidth < bird.x - bird.radius && !pipe.passed) {
                        pipe.passed = true;
                        score++;
                    }
                }

                drawBird();
            } else {
                drawStartScreen();
            }

            // Display the score
            ctx.fillStyle = "black";
            ctx.font = "20px Arial";
            ctx.fillText("Score: " + score, 10, 30);
        }

        function drawStartScreen() {
            startScreen.style.display = "block";
        }

        function startGame() {
            gameStarted = true;
            startScreen.style.display = "none";
            gameInterval = setInterval(draw, 10);
        }

        function gameOver() {
            clearInterval(gameInterval);
            endScreen.style.display = "block";
            scoreText.textContent = "Score: " + score;
        }

        function restartGame() {
            bird.y = canvas.height / 2 - 10;
            pipes.length = 0;
            score = 0;
            gameStarted = false;
            endScreen.style.display = "none";
            startGame();
        }

        document.addEventListener("keydown", (event) => {
            if (event.key === " " && !gameStarted) {
                startGame();
            }
            if (event.key === " " && gameStarted) {
                bird.velocity = bird.jumpStrength;
            }
        });
    </script>
</body>
</html>
