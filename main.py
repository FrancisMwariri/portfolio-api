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
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Francis Mwariri | Backend Development Portfolio</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, Helvetica, sans-serif;
                background: #f4f7fb;
                color: #1f2937;
                line-height: 1.6;
            }

            .container {
                width: 90%;
                max-width: 1000px;
                margin: 40px auto;
            }

            /* HEADER */

            .header {
                background: linear-gradient(135deg, #111827, #1e3a8a);
                color: white;
                padding: 40px;
                border-radius: 15px;
                margin-bottom: 30px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.10);
            }

            .header h1 {
                font-size: 36px;
                margin-bottom: 25px;
            }

            .student-info {
                font-size: 16px;
                line-height: 1.8;
            }

            .admission {
                color: #60a5fa;
                font-weight: bold;
            }

            .email {
                color: #93c5fd;
            }

            /* INTRO */

            .intro {
                text-align: center;
                margin-bottom: 30px;
            }

            .intro h2 {
                font-size: 28px;
                margin-bottom: 10px;
            }

            .intro p {
                color: #6b7280;
            }

            /* ASSIGNMENTS */

            .assignments {
                display: flex;
                flex-direction: column;
                gap: 15px;
            }

            .assignment {
                background: white;
                border: 1px solid #e5e7eb;
                border-radius: 10px;
                padding: 20px;
                transition: 0.3s ease;
            }

            .assignment:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
            }

            .assignment a {
                text-decoration: none;
                color: #1f2937;
                display: block;
            }

            .lesson {
                color: #2563eb;
                font-weight: bold;
                font-size: 14px;
                margin-bottom: 5px;
                text-transform: uppercase;
            }

            .title {
                font-size: 19px;
                font-weight: bold;
                margin-bottom: 5px;
            }

            .description {
                color: #6b7280;
                font-size: 14px;
            }

            .no-repository {
                color: #9ca3af;
                font-size: 14px;
                margin-top: 8px;
            }

            /* FOOTER */

            footer {
                text-align: center;
                margin-top: 40px;
                padding: 25px;
                border-top: 1px solid #e5e7eb;
                color: #6b7280;
            }

            footer p {
                margin: 6px 0;
            }

            footer a {
                color: #2563eb;
                text-decoration: none;
                font-weight: bold;
            }

            /* MOBILE */

            @media (max-width: 600px) {

                .container {
                    width: 94%;
                    margin: 20px auto;
                }

                .header {
                    padding: 25px;
                }

                .header h1 {
                    font-size: 28px;
                }

                .assignment {
                    padding: 18px;
                }

            }

        </style>

    </head>


    <body>

        <div class="container">


            <!-- STUDENT INFORMATION -->

            <div class="header">

                <h1>📚 Backend Development Portfolio</h1>

                <div class="student-info">

                    <p>
                        <strong>Student Name:</strong>
                        Francis Mwariri
                    </p>

                    <p>
                        <strong>Admission Number:</strong>
                        <span class="admission">
                            C027-01-0829/2024
                        </span>
                    </p>

                    <p>
                        <strong>Email:</strong>
                        <span class="email">
                            francis.macharia24@students.dkut.ac.ke
                        </span>
                    </p>

                </div>

            </div>


            <!-- BACKEND ASSIGNMENTS -->

            <div class="intro">

                <h2>💻 Backend Assignments</h2>

                <p>
                    Click on any assignment to view the
                    complete code on GitHub.
                </p>

            </div>


            <div class="assignments">


                <!-- LESSON 1 -->

                <div class="assignment">

                    <a href="#" onclick="return false;">

                        <div class="lesson">
                            Lesson 1
                        </div>

                        <div class="title">
                            HTTP & Your First API
                        </div>

                        <div class="description">
                            FastAPI + Uvicorn, HTTP Methods, Status Codes
                        </div>

                        <div class="no-repository">
                            No Repository
                        </div>

                    </a>

                </div>


                <!-- LESSON 2 -->

                <div class="assignment">

                    <a href="#" onclick="return false;">

                        <div class="lesson">
                            Lesson 2
                        </div>

                        <div class="title">
                            Docker - Packaging Your API
                        </div>

                        <div class="description">
                            Containers, Dockerfiles, Docker Compose
                        </div>

                        <div class="no-repository">
                            No Repository
                        </div>

                    </a>

                </div>


                <!-- LESSON 3 -->

                <div class="assignment">

                    <a href="#" onclick="return false;">

                        <div class="lesson">
                            Lesson 3
                        </div>

                        <div class="title">
                            Routing, Parameters & Request Bodies
                        </div>

                        <div class="description">
                            Path Parameters, Query Parameters,
                            Pydantic Validation
                        </div>

                        <div class="no-repository">
                            No Repository
                        </div>

                    </a>

                </div>


                <!-- LESSON 4 -->

                <div class="assignment">

                    <a
                        href="https://github.com/FrancisMwariri/bookstore-api"
                        target="_blank"
                        rel="noopener noreferrer"
                    >

                        <div class="lesson">
                            Lesson 4
                        </div>

                        <div class="title">
                            PostgreSQL & SQLModel – Your First Database
                        </div>

                        <div class="description">
                            ORM, Database Migrations, SQLModel
                        </div>

                    </a>

                </div>


                <!-- LESSON 5 -->

                <div class="assignment">

                    <a
                        href="https://github.com/FrancisMwariri/product-api"
                        target="_blank"
                        rel="noopener noreferrer"
                    >

                        <div class="lesson">
                            Lesson 5
                        </div>

                        <div class="title">
                            CRUD Operations
                        </div>

                        <div class="description">
                            Create, Read, Update, Delete with Error Handling
                        </div>

                    </a>

                </div>


                <!-- LESSON 6 -->

                <div class="assignment">

                    <a
                        href="https://github.com/FrancisMwariri/techvault-api"
                        target="_blank"
                        rel="noopener noreferrer"
                    >

                        <div class="lesson">
                            Lesson 6
                        </div>

                        <div class="title">
                            Error Handling & Validation
                        </div>

                        <div class="description">
                            HTTPException, Custom Validators, Global Handlers
                        </div>

                    </a>

                </div>


                <!-- LESSON 7 -->

                <div class="assignment">

                    <a
                        href="https://github.com/FrancisMwariri/healthtrack-api"
                        target="_blank"
                        rel="noopener noreferrer"
                    >

                        <div class="lesson">
                            Lesson 7
                        </div>

                        <div class="title">
                            User Authentication – JWT & Password Hashing
                        </div>

                        <div class="description">
                            JWT Tokens, bcrypt, Login/Register Endpoints
                        </div>

                    </a>

                </div>


                <!-- LESSON 8 -->

                <div class="assignment">

                    <a
                        href="https://github.com/FrancisMwariri/clinicguard-api"
                        target="_blank"
                        rel="noopener noreferrer"
                    >

                        <div class="lesson">
                            Lesson 8
                        </div>

                        <div class="title">
                            Authorization & Rate Limiting
                        </div>

                        <div class="description">
                            RBAC, Dependency Injection, Rate Limiting
                        </div>

                    </a>

                </div>


                <!-- LESSON 9 -->

                <div class="assignment">

                    <a
                        href="https://github.com/FrancisMwariri/sendit-api"
                        target="_blank"
                        rel="noopener noreferrer"
                    >

                        <div class="lesson">
                            Lesson 9
                        </div>

                        <div class="title">
                            File Uploads & External APIs
                        </div>

                        <div class="description">
                            File Validation, httpx, Environment Variables
                        </div>

                    </a>

                </div>


                <!-- LESSON 10 -->

                <div class="assignment">

                    <a
                        href="https://github.com/FrancisMwariri/product-api-clouddeploy"
                        target="_blank"
                        rel="noopener noreferrer"
                    >

                        <div class="lesson">
                            Lesson 10
                        </div>

                        <div class="title">
                            Testing & Deployment (Cloud)
                        </div>

                        <div class="description">
                            Pytest, CI/CD, Render Deployment
                        </div>

                    </a>

                </div>


            </div>


            <!-- FOOTER -->

            <footer>

                <p>
                    📅 Last Updated: August 2026
                </p>

                <p>
                    ⚠️ Deployed on Render |
                    <a
                        href="https://github.com/FrancisMwariri"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        Source Code on GitHub
                    </a>
                </p>

            </footer>


        </div>

    </body>

    </html>
    """

    return HTMLResponse(content=html_content)
