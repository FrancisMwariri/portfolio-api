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

        <title>Backend Development Portfolio</title>

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
                width: 92%;
                max-width: 1100px;
                margin: 40px auto;
            }

            /* HEADER */

            .header {
                background: linear-gradient(135deg, #111827, #1e3a8a);
                color: white;
                padding: 45px;
                border-radius: 18px;
                margin-bottom: 35px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.10);
            }

            .header h1 {
                font-size: 38px;
                margin-bottom: 25px;
            }

            .student-info p {
                margin: 10px 0;
                font-size: 16px;
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
                margin: 40px 0 30px;
            }

            .intro h2 {
                font-size: 30px;
                margin-bottom: 10px;
            }

            .intro p {
                color: #6b7280;
            }

            /* ASSIGNMENTS */

            .assignments {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
            }

            .assignment {
                background: white;
                padding: 25px;
                border-radius: 14px;
                border: 1px solid #e5e7eb;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
                transition: 0.3s ease;
            }

            .assignment:hover {
                transform: translateY(-5px);
                box-shadow: 0 12px 25px rgba(0, 0, 0, 0.09);
            }

            .lesson {
                color: #2563eb;
                font-size: 15px;
                font-weight: bold;
                margin-bottom: 6px;
                text-transform: uppercase;
            }

            .assignment h3 {
                font-size: 20px;
                margin-bottom: 10px;
            }

            .assignment p {
                color: #6b7280;
                font-size: 14px;
                margin-bottom: 18px;
            }

            .github-link {
                display: inline-block;
                background: #2563eb;
                color: white;
                padding: 9px 16px;
                border-radius: 7px;
                text-decoration: none;
                font-size: 14px;
                font-weight: bold;
                transition: 0.2s;
            }

            .github-link:hover {
                background: #1d4ed8;
            }

            .not-available {
                display: inline-block;
                background: #e5e7eb;
                color: #6b7280;
                padding: 9px 16px;
                border-radius: 7px;
                font-size: 14px;
            }

            /* FOOTER */

            footer {
                text-align: center;
                margin-top: 50px;
                padding: 30px 10px;
                border-top: 1px solid #e5e7eb;
                color: #6b7280;
                font-size: 14px;
            }

            footer p {
                margin: 6px 0;
            }

            footer a {
                color: #2563eb;
                text-decoration: none;
            }

            /* MOBILE */

            @media (max-width: 600px) {

                .container {
                    width: 94%;
                    margin: 20px auto;
                }

                .header {
                    padding: 30px 22px;
                }

                .header h1 {
                    font-size: 29px;
                }

                .assignments {
                    grid-template-columns: 1fr;
                }

            }

        </style>

    </head>


    <body>

        <div class="container">


            <!-- STUDENT INFORMATION -->

            <div class="header">

                <h1>Backend Development Portfolio</h1>

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


            <!-- ASSIGNMENTS INTRODUCTION -->

            <div class="intro">

                <h2>Backend Assignments</h2>

                <p>
                    Click on any assignment to view the
                    complete code on GitHub.
                </p>

            </div>


            <!-- ASSIGNMENTS -->

            <div class="assignments">


                <!-- LESSON 1 -->

                <div class="assignment">

                    <div class="lesson">
                        Lesson 1
                    </div>

                    <h3>
                        HTTP & Your First API
                    </h3>

                    <p>
                        FastAPI + Uvicorn, HTTP Methods,
                        Status Codes
                    </p>

                    <span class="not-available">
                        No Repository
                    </span>

                </div>


                <!-- LESSON 2 -->

                <div class="assignment">

                    <div class="lesson">
                        Lesson 2
                    </div>

                    <h3>
                        Docker - Packaging Your API
                    </h3>

                    <p>
                        Containers, Dockerfiles,
                        Docker Compose
                    </p>

                    <span class="not-available">
                        No Repository
                    </span>

                </div>


                <!-- LESSON 3 -->

                <div class="assignment">

                    <div class="lesson">
                        Lesson 3
                    </div>

                    <h3>
                        Routing, Parameters & Request Bodies
                    </h3>

                    <p>
                        Path Parameters, Query Parameters,
                        Pydantic Validation
                    </p>

                    <span class="not-available">
                        No Repository
                    </span>

                </div>


                <!-- LESSON 4 -->

                <div class="assignment">

                    <div class="lesson">
                        Lesson 4
                    </div>

                    <h3>
                        PostgreSQL & SQLModel – Your First Database
                    </h3>

                    <p>
                        ORM, Database Migrations,
                        SQLModel
                    </p>

                    <a
                        class="github-link"
                        href="https://github.com/FrancisMwariri/bookstore-api"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        View on GitHub
                    </a>

                </div>


                <!-- LESSON 5 -->

                <div class="assignment">

                    <div class="lesson">
                        Lesson 5
                    </div>

                    <h3>
                        CRUD Operations
                    </h3>

                    <p>
                        Create, Read, Update, Delete
                        with Error Handling
                    </p>

                    <a
                        class="github-link"
                        href="https://github.com/FrancisMwariri/product-api"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        View on GitHub
                    </a>

                </div>


                <!-- LESSON 6 -->

                <div class="assignment">

                    <div class="lesson">
                        Lesson 6
                    </div>

                    <h3>
                        Error Handling & Validation
                    </h3>

                    <p>
                        HTTPException, Custom Validators,
                        Global Handlers
                    </p>

                    <a
                        class="github-link"
                        href="https://github.com/FrancisMwariri/techvault-api"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        View on GitHub
                    </a>

                </div>


                <!-- LESSON 7 -->

                <div class="assignment">

                    <div class="lesson">
                        Lesson 7
                    </div>

                    <h3>
                        User Authentication – JWT & Password Hashing
                    </h3>

                    <p>
                        JWT Tokens, bcrypt,
                        Login/Register Endpoints
                    </p>

                    <a
                        class="github-link"
                        href="https://github.com/FrancisMwariri/healthtrack-api"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        View on GitHub
                    </a>

                </div>


                <!-- LESSON 8 -->

                <div class="assignment">

                    <div class="lesson">
                        Lesson 8
                    </div>

                    <h3>
                        Authorization & Rate Limiting
                    </h3>

                    <p>
                        RBAC, Dependency Injection,
                        Rate Limiting
                    </p>

                    <a
                        class="github-link"
                        href="https://github.com/FrancisMwariri/clinicguard-api"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        View on GitHub
                    </a>

                </div>


                <!-- LESSON 9 -->

                <div class="assignment">

                    <div class="lesson">
                        Lesson 9
                    </div>

                    <h3>
                        File Uploads & External APIs
                    </h3>

                    <p>
                        File Validation, httpx,
                        Environment Variables
                    </p>

                    <a
                        class="github-link"
                        href="https://github.com/FrancisMwariri/sendit-api"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        View on GitHub
                    </a>

                </div>


                <!-- LESSON 10 -->

                <div class="assignment">

                    <div class="lesson">
                        Lesson 10
                    </div>

                    <h3>
                        Testing & Deployment (Cloud)
                    </h3>

                    <p>
                        Pytest, CI/CD,
                        Render Deployment
                    </p>

                    <a
                        class="github-link"
                        href="https://github.com/FrancisMwariri/product-api-clouddeploy"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        View on GitHub
                    </a>

                </div>


            </div>


            <!-- FOOTER -->

            <footer>

                <p>
                    📅 Last Updated: August 2026
                </p>

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

            </footer>


        </div>

    </body>

    </html>
    """

    return HTMLResponse(content=html_content)
