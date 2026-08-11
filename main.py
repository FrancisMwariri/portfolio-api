from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def portfolio():

    html_content = """
    <!DOCTYPE html>
    <html lang="en">

    <head>

        <meta charset="UTF-8">

        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">

        <title>Backend Development Portfolio</title>

        <style>

            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }

            body {
                font-family: Arial, Helvetica, sans-serif;
                background: #f4f4f4;
                color: #1f2937;
            }

            .container {
                width: 95%;
                max-width: 720px;
                margin: 10px auto;
                background: white;
                padding: 24px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.12);
            }


            /* HEADER */

            .header {
                margin-bottom: 16px;
            }

            .title {
                display: flex;
                align-items: center;
                gap: 10px;
                padding-bottom: 8px;
                border-bottom: 2px solid #3498db;
            }

            .title-icon {
                font-size: 22px;
            }

            .title h1 {
                font-size: 24px;
                color: #2c3e50;
            }


            /* STUDENT INFORMATION */

            .student-info {
                background: #eaf5fd;
                padding: 20px 10px;
                margin-top: 16px;
                border-radius: 5px;
            }

            .student-info p {
                font-size: 12px;
                margin-bottom: 12px;
            }

            .student-info p:last-child {
                margin-bottom: 0;
            }

            .student-info strong {
                color: #2c3e50;
            }

            .admission {
                color: #2874a6;
                font-weight: bold;
            }


            /* ASSIGNMENTS HEADER */

            .assignments-header {
                display: flex;
                align-items: center;
                gap: 8px;
                margin-top: 18px;
                margin-bottom: 16px;
            }

            .assignments-header span {
                font-size: 20px;
            }

            .assignments-header h2 {
                font-size: 18px;
                color: #111827;
            }

            .instruction {
                font-size: 12px;
                color: #777;
                margin-bottom: 14px;
            }


            /* ASSIGNMENT ROWS */

            .assignments {
                display: flex;
                flex-direction: column;
                gap: 8px;
            }

            .assignment {
                display: flex;
                align-items: center;
                min-height: 38px;

                background: #f8f9fa;

                border-left: 4px solid #3498db;

                border-radius: 5px;

                padding: 7px 10px;

                text-decoration: none;

                transition: 0.2s ease;
            }

            .assignment:hover {
                background: #eef6fc;
                transform: translateX(2px);
            }


            /* LESSON BADGE */

            .lesson {
                background: #3498db;
                color: white;

                border-radius: 12px;

                padding: 3px 9px;

                font-size: 10px;
                font-weight: bold;

                white-space: nowrap;

                margin-right: 10px;
            }


            /* ASSIGNMENT TITLE */

            .assignment-title {
                color: #1769aa;

                font-size: 12px;
                font-weight: bold;

                white-space: nowrap;
            }


            /* DESCRIPTION */

            .description {
                color: #777;

                font-size: 11px;

                margin-left: 8px;

                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            }


            /* FOOTER */

            footer {
                margin-top: 22px;

                padding-top: 18px;

                border-top: 1px solid #e5e7eb;

                text-align: center;

                color: #888;

                font-size: 11px;
            }

            footer p {
                margin-bottom: 10px;
            }

            footer a {
                color: #777;
                text-decoration: none;
            }

            footer a:hover {
                color: #3498db;
            }


            /* MOBILE */

            @media (max-width: 600px) {

                .container {
                    width: 94%;
                    padding: 18px;
                    margin: 10px auto;
                }

                .title h1 {
                    font-size: 21px;
                }

                .assignment {
                    align-items: center;
                }

                .assignment-title {
                    font-size: 11px;
                }

                .description {
                    font-size: 10px;
                }

            }

        </style>

    </head>


    <body>

        <div class="container">


            <!-- HEADER -->

            <div class="header">

                <div class="title">

                    <div class="title-icon">
                        📚
                    </div>

                    <h1>
                        Backend Development Portfolio
                    </h1>

                </div>


                <!-- STUDENT INFORMATION -->

                <div class="student-info">

                    <p>
                        <strong>
                            Student Name:
                        </strong>

                        Francis Mwariri
                    </p>


                    <p>
                        <strong>
                            Admission Number:
                        </strong>

                        <span class="admission">
                            C027-01-0829/2024
                        </span>
                    </p>


                    <p>
                        <strong>
                            Email:
                        </strong>

                        francis.macharia24@students.dkut.ac.ke
                    </p>

                </div>

            </div>


            <!-- BACKEND ASSIGNMENTS -->

            <div class="assignments-header">

                <span>
                    📚
                </span>

                <h2>
                    Backend Assignments
                </h2>

            </div>


            <p class="instruction">
                Click on any completed assignment to view
                the complete code on GitHub.
            </p>


            <!-- ASSIGNMENTS -->

            <div class="assignments">


                <!-- LESSON 4 -->

                <a
                    class="assignment"
                    href="https://github.com/FrancisMwariri/bookstore-api"
                    target="_blank"
                    rel="noopener noreferrer"
                >

                    <span class="lesson">
                        Lesson 4
                    </span>

                    <span class="assignment-title">
                        PostgreSQL & SQLModel – Your First Database
                    </span>

                    <span class="description">
                        — ORM, Database Migrations, SQLModel
                    </span>

                </a>


                <!-- LESSON 5 -->

                <a
                    class="assignment"
                    href="https://github.com/FrancisMwariri/product-api"
                    target="_blank"
                    rel="noopener noreferrer"
                >

                    <span class="lesson">
                        Lesson 5
                    </span>

                    <span class="assignment-title">
                        CRUD Operations
                    </span>

                    <span class="description">
                        — Create, Read, Update, Delete with Error Handling
                    </span>

                </a>


                <!-- LESSON 6 -->

                <a
                    class="assignment"
                    href="https://github.com/FrancisMwariri/techvault-api"
                    target="_blank"
                    rel="noopener noreferrer"
                >

                    <span class="lesson">
                        Lesson 6
                    </span>

                    <span class="assignment-title">
                        Error Handling & Validation
                    </span>

                    <span class="description">
                        — HTTPException, Custom Validators, Global Handlers
                    </span>

                </a>


                <!-- LESSON 7 -->

                <a
                    class="assignment"
                    href="https://github.com/FrancisMwariri/healthtrack-api"
                    target="_blank"
                    rel="noopener noreferrer"
                >

                    <span class="lesson">
                        Lesson 7
                    </span>

                    <span class="assignment-title">
                        User Authentication – JWT & Password Hashing
                    </span>

                    <span class="description">
                        — JWT Tokens, bcrypt, Login/Register Endpoints
                    </span>

                </a>


                <!-- LESSON 8 -->

                <a
                    class="assignment"
                    href="https://github.com/FrancisMwariri/clinicguard-api"
                    target="_blank"
                    rel="noopener noreferrer"
                >

                    <span class="lesson">
                        Lesson 8
                    </span>

                    <span class="assignment-title">
                        Authorization & Rate Limiting
                    </span>

                    <span class="description">
                        — RBAC, Dependency Injection, Rate Limiting
                    </span>

                </a>


                <!-- LESSON 9 -->

                <a
                    class="assignment"
                    href="https://github.com/FrancisMwariri/sendit-api"
                    target="_blank"
                    rel="noopener noreferrer"
                >

                    <span class="lesson">
                        Lesson 9
                    </span>

                    <span class="assignment-title">
                        File Uploads & External APIs
                    </span>

                    <span class="description">
                        — File Validation, httpx, Environment Variables
                    </span>

                </a>


                <!-- LESSON 10 -->

                <a
                    class="assignment"
                    href="https://github.com/FrancisMwariri/product-api-clouddeploy"
                    target="_blank"
                    rel="noopener noreferrer"
                >

                    <span class="lesson">
                        Lesson 10
                    </span>

                    <span class="assignment-title">
                        Testing & Deployment (Cloud)
                    </span>

                    <span class="description">
                        — Pytest, CI/CD, Render Deployment
                    </span>

                </a>


            </div>


            <!-- FOOTER -->

            <footer>

                <p>
                    Deployed on Render |
                    <a
                        href="https://github.com/FrancisMwariri"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        Source Code on GitHub
                    </a>
                </p>

                <p>
                    Last Updated: August 2026
                </p>

            </footer>


        </div>

    </body>

    </html>
    """

    return HTMLResponse(content=html_content)
