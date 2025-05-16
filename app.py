from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for session security (flash messages)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Log the message (or store it if needed)
    print(f"Received message from {name} ({email}): {message}")

    flash("Thank you for reaching out! We will get back to you soon.")
    return redirect(url_for("home"))

@app.route("/projects")
def projects():
    project_list = [
        {
            "title": "Flask App on AWS EC2",
            "description": "A portfolio web app hosted on EC2 with Git integration.",
            "link": "https://github.com/Sikandar-dev-s/mydreamapp"
        },
        {
            "title": "Terraform AWS Provisioning",
            "description": "Provision EC2 and S3 buckets using IaC principles.",
            "link": "https://github.com/your-repo/terraform-aws"
        }
    ]
    return render_template("projects.html", projects=project_list)


if __name__ == "__main__":
    app.run(debug=True)
