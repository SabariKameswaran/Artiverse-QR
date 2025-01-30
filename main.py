from flask import Flask, render_template
import qrcode
import os

app = Flask(__name__)

def generate_qr(team_name, url="https://www.google.com"):
    img = qrcode.make(url)
    img_path = f"static/images/{team_name}.png"
    os.makedirs(os.path.dirname(img_path), exist_ok=True)
    img.save(img_path)
    return img_path

teams = [
    "agro_tech","bio_med_girls", "ctrl_alt_elite", "engineering_innovators", "fly_bee",
    "hogwarts", "mediflora", "quantum_coders", "sky8ive_coders", "spartanz",
    "tech_magic", "tech_spryzen", "tech_titanzz", "techminds", "trojan_terminators"
]


def create_team_route(team):
    def team_route():
        img_path = generate_qr(team)
        return render_template(f"{team}.html", qr_code=img_path)
    return team_route

for team in teams:
    app.add_url_rule(f"/{team}", team, create_team_route(team))

if __name__ == "__main__":
    app.run(debug=True)