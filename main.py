from flask import Flask, render_template

app = Flask(__name__)

teams = [
    "agro_tech", "bio_med_girls", "ctrl_alt_elite", "engineering_innovators", "fly_bee",
    "hogwarts", "mediflora", "quantum_coders", "sky8ive_coders", "spartanz",
    "tech_magic", "tech_spryzen", "tech_titanzz", "techminds", "trojan_terminators"
]

@app.route('/')
def home():
    return render_template('home.html', teams=teams)

def create_team_route(team):
    def team_route():
        return render_template(f"{team}.html")
    return team_route

for team in teams:
    app.add_url_rule(f"/{team}", team, create_team_route(team))

if __name__ == "__main__":
    app.run(debug=True)