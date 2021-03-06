from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('./home.html')

@app.route('/resorts/')
def resorts_page():
	return render_template("./mainpage_resorts.html")

@app.route('/resorts/<resort>/')
def resort_page(resort):
	if resort == '1':
		return render_template('./Steamboat.html')
	if resort == '2':
		return render_template('./Vail.html')
	if resort == '3':
		return render_template('./Breckenridge.html')
	return 'nothing found'

@app.route('/trails/')
def trails_page():
	return render_template("./mainpage_trails.html")

@app.route('/trails/<trail>/')
def trail_page(trail):
	if trail == '1':
		return render_template('./flash_of_gold.html')
	if trail == '2':
		return render_template('./strawberry_lane.html')
	if trail == '3':
		return render_template('./aspen_alley_trail.html')
	return 'nothing found'

@app.route('/photos/')
def photos_page():
	return render_template("./mainpage_photos.html")

@app.route('/photos/<photo>/')
def photo_page(photo):
	if photo == '1':
		return render_template('./flash_of_gold_pic.html')
	if photo == '2':
		return render_template('./strawberry_lane_pic.html')
	if photo == '3':
		return render_template('./aspen_alley_trail_pic.html')
	return 'nothing found'

@app.route('/about/')
def about_page():
	return render_template('./about.html')

@app.route('/carousel/')
def cmove():
	return render_template('./carousel.html')

@app.route('/githubstats/')
def githubstats():
	github_commits = "https://api.github.com/repos/RobertHale/HikingAdventure/stats/contributors"
	github_issues  = "https://api.github.com/repos/RobertHale/HikingAdventure/issues?state=all"

	# Grab Total Commits
	response_c = requests.get(github_commits)
	commit_array = response_c.json()
	person = commit_array[0]
	commits = 0
	commits_each = {};
	for person in commit_array:
		commits = commits + person['total']
		# Stores each person's commit count separately
		commits_each[person['author']['login']] = person['total']


	# Grab Total issues
	response_i = requests.get(github_issues)
	issue_array = response_i.json()
	latest_issue = issue_array[0]
	issues = latest_issue['number']


	# Return data in a string
	data = str(commits) + " " + str(issues) + " " + str(commits_each.get("victor40", 0)) + " " + str(commits_each.get("duoALopez", 0)) + " " + str(commits_each.get("alexdai186", 0)) + " " + str(commits_each.get("RobertHale", 0)) + " " + str(commits_each.get("vponakala", 0)) + " " + str(commits_each.get("davepcast", 0))
	return data

if __name__ == "__main__":
	app.run()
